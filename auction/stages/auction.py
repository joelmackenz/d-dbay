import state
from state import init_state
import random
from auction.assets.calculators import getHypedBidders, getItemStartingPrice, getBiddersAttractedByPercent, getterminus_price, d20Roll, d6Roll
from assets.functions import half_sec_pause, one_sec_pause, twoSecPause
from assets.databaseCalls import saveToDatabase
from auction.assets.names import names


async def revealBuyer(message):
    randomNum = random.randint(0, (len(names) - 1))
    randomName = names[randomNum]
    await message.channel.send("Our winner today is\n.")
    half_sec_pause()
    await message.channel.send(".")
    half_sec_pause()
    await message.channel.send(".")
    half_sec_pause()
    await message.channel.send(randomName + ", heading home with the " + state.rarity + " " + state.item.title() + " for " + str(state.winning_bid) + " sp!\n_ _")
    twoSecPause()

async def auctionComplete(message):
    fivePercentOfitem_value = round((state.item_value * .05), 2)
    state.finalPrizeMoney = state.winning_bid - fivePercentOfitem_value
    await message.channel.send("Thank you for taking part of the auction today! What a wild ride that was. As per our agreement, "+
    "Drecker & Dee's fee is 5 percent of the item's value: " + str(fivePercentOfitem_value) + " sp.\n\nThat leaves you with " + str(state.finalPrizeMoney) +
    " sp in your pocket!\n\nThank you so much for playing, " + state.current_user + "! \nDo come again soon!\nHave a Dee-Lightful Day!")
    state.game_running = False

async def auctionDidntRun(message):
    await message.channel.send("Oh no! No one seems interested in the " + state.item + "!\n"+
    "Luckily, we here at D&D Bay aren't interested in taking your item, so you can have the thing back!\n"+
    "Well, aren't you lucky? You get to keep the thing!\n"+
    "We here at D&D Bay wish you well, and look forward to seeing you again!\n"+
    "Just not with that thing.\n"+
    "Have a Dee-Lightful Day!")

async def auction(message):
    hypedBidders = getHypedBidders()
    itemStartingPrice = getItemStartingPrice()
    state.going_bid = itemStartingPrice
    biddersAttractedByPercent = getBiddersAttractedByPercent()
    state.total_bidders = hypedBidders + biddersAttractedByPercent
    state.current_bidders = state.total_bidders
    state.terminus_price = getterminus_price()
    state.auctionRound = 1

    def pluralS(num):
        if num > 1:
            return "s"
        else:
            return ""
    
    def vowelN(word):
        vowelList = ["a","e","i","o","u"]
        wordStartsWithVowel = word.lower().startswith(tuple(vowelList))
        if wordStartsWithVowel:
            return "n"
        else:
            return ""

    def pluralToBe(number):
        if number > 1:
            return "are"
        else:
            return "is"

    async def nextAuctionRound():
        await bidCheck()
        noMoreRounds = bool()
        if state.going_bid >= state.terminus_price:
            state.winning_bid = state.terminus_price
            noMoreRounds = True
        elif state.current_bidders > 1:
            await nextAuctionRound()
        else:
            state.winning_bid = state.going_bid
            noMoreRounds = True
        if noMoreRounds:
            twoSecPause()
            await message.channel.send("Going once ... going twice ... sold!\n")
            await revealBuyer(message)
            await auctionComplete(message)

    async def bidCheck():
        roll = d20Roll()
        bidCheckStopDC = int()

        if state.rarity == "rare":
            bidCheckStopDC = 10
        else:
            bidCheckStopDC = 9

        if roll < bidCheckStopDC:
            await stopBiddingCheck()
        else:
            if roll <= 13:
                state.going_bid += state.item_value * .0315
            elif roll <= 19:
                state.going_bid += state.item_value * .0615
            elif roll == 20:
                state.going_bid += state.item_value * .09
            state.going_bid = round(state.going_bid, 2)
            if state.going_bid >= state.terminus_price:
                state.going_bid = state.terminus_price
            await message.channel.send(str(state.going_bid) + "! We are at " + str(state.going_bid) + " sp!")
            state.auctionRound += 1

    async def stopBiddingCheck():
        roll = d20Roll()
        droppedOut = bool()

        # Higher values make the dropout chance higher. Number equivalent to DC.
        if state.auctionRound <= 4:
            if (state.rarity == "common" and roll < 16) or (state.rarity == "uncommon" and roll < 12) or (state.rarity == "rare" and roll < 8):
                droppedOut = True
        elif state.auctionRound <= 7:
            if (state.rarity == "common" and roll < 18) or (state.rarity == "uncommon" and roll < 16) or (state.rarity == "rare" and roll < 13):
                droppedOut = True
        elif state.auctionRound >= 8:
            if (state.rarity == "common" and roll < 19) or (state.rarity == "uncommon" and roll < 18) or (state.rarity == "rare" and roll < (13 + d6Roll())):
                droppedOut = True

        if droppedOut == True:
            state.current_bidders -= 1
            if state.current_bidders == 1:
                await message.channel.send("A bidder dropped out!")
            else:
                await message.channel.send("A bidder dropped out! There " + pluralToBe(state.current_bidders) + " " + str(state.current_bidders) + " bidder" + pluralS(state.current_bidders) + " left!")

    async def auctionStart():
        state.game_running = True
        one_sec_pause()
        await message.channel.send("Up for auction today: a" + vowelN(state.item) + " " + state.item.title() + "!")

        one_sec_pause()
        if hypedBidders < 0:
            await message.channel.send("Whuh-oh, your attempts at swaying the town with " + state.hype + " scared off " + str(abs(hypedBidders)) + " bidder" + pluralS(hypedBidders) + "! Oops.")
        elif hypedBidders == 0:
            await message.channel.send("Unfortunately, your feats of " + state.hype + " didn't seem to attract any bidders!")
        elif hypedBidders > 0:
            await message.channel.send("Looks like your feats of " + state.hype + " attracted " + str(hypedBidders) + " bidder" + pluralS(hypedBidders) + "! Woohoo!")

        twoSecPause()
        if state.total_bidders > 1:
            await message.channel.send("We have " + str(state.total_bidders) + " bidders total in the auction room!")
            twoSecPause()
        await message.channel.send("Let's start the bidding at " + str(itemStartingPrice) + " sp!\n_ _")
        twoSecPause()

        if state.total_bidders <= 1:
            await auctionDidntRun(message)
        else:
            await nextAuctionRound()

    if not state.game_running:
        await auctionStart()
        saveToDatabase()
        init_state()
