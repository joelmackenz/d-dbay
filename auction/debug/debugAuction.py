import state
from state import init_state
import time
import random
from auction.assets.calculators import getHypedBidders, getItemStartingPrice, getBiddersAttractedByPercent, getterminus_price, d20Roll, d6Roll
from assets.functions import half_sec_pause, one_sec_pause, twoSecPause, resetStates
from assets.databaseCalls import saveToDatabase
from assets.names import names

async def revealBuyer(message):
    pass

async def auctionComplete(message):
    fivePercentOfitem_value = round((state.item_value * .05), 2)
    state.finalPrizeMoney = round((state.winning_bid - fivePercentOfitem_value), 2)
    print(state.terminus_price)
    if state.finalPrizeMoney >= state.terminus_price:
        print(str(state.finalPrizeMoney) + " " + str(state.terminus_price))
    # print("total rounds: " + str(state.auctionRound))

async def auctionDidntRun(message):
    pass

async def debugAuction(message):
    hypedBidders = getHypedBidders()
    itemStartingPrice = getItemStartingPrice()
    state.going_bid = itemStartingPrice
    biddersAttractedByPercent = getBiddersAttractedByPercent()
    state.total_bidders = hypedBidders + biddersAttractedByPercent
    state.current_bidders = state.total_bidders
    state.terminus_price = getterminus_price()
    state.auctionRound = 1

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
           
    async def auctionStart():
        if state.total_bidders <= 1:
            await auctionDidntRun(message)
        else:
            await nextAuctionRound()

    await auctionStart()

    saveToDatabase()

    init_state()
