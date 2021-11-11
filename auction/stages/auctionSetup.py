import math
import state
from state import init_state
from assets.responses import positiveResponses, negativeResponses, exit_responses
from assets.functions import set_current_user


async def welcome(message):
    set_current_user()
    welcomeMessage = ("Welcome to the Drecker & Dee Bay auction center, " + state.current_user + "! \n"
    "Let's turn your item into today's hot-ticket-item! \n")
    await message.channel.send(welcomeMessage)
    await auctionSetup(message)

async def goodbye(message):
    goodbyeMessage = ("You've chosen to back-out of the auction, " + state.current_user + "! \n"
    "We at Drecker & Dee are sure you have your reasons. \n"
    "Have a Dee-liteful day!")
    init_state()
    state.auction_stage = 0
    state.auctionSelected = False
    await message.channel.send(goodbyeMessage)

async def confirm(message):
    if (any(word in str(message.content.lower()) for word in positiveResponses)):
        await message.channel.send("Ok!")
        state.auction_stage = math.floor(state.auction_stage) + 1
        await auctionSetup(message)
    elif (any(word in str(message.content.lower()) for word in negativeResponses)):
        await message.channel.send("Ok, let's try again!")
        state.auction_stage = state.return_to_step
        await auctionSetup(message)

async def auctionSetup(message):
    latestMessage = message.content.lower()

    # If any exit words are entered, exit the program
    if (any(word in str(message.content) for word in exit_responses)):
        await goodbye(message)

    # Floats go to confirm()
    elif type(state.auction_stage) == float:
        await confirm(message)

    # Item name
    elif state.auction_stage == 0:
        await message.channel.send("What is the item that you would like to auction today?")
        state.auction_stage = 1

    elif state.auction_stage == 1:
        itemName = latestMessage.strip()
        await message.channel.send("The item that you'd like to auction is called " + itemName.title() + ". Is that right?")
        state.potential_state = itemName
        state.return_to_step = 0
        state.auction_stage = 1.1

    # Item rarity
    elif state.auction_stage == 2:
        if not state.item:
            state.item = state.potential_state
            state.potential_state = ""
        await message.channel.send("What is the rarity of the item -- common, uncommon, or rare? (If unsure, ask a Game Mom!)")
        state.auction_stage = 3

    elif state.auction_stage == 3:
        if latestMessage.strip() in ['common', 'uncommon', 'rare']:
            if latestMessage.startswith('com'):
                await message.channel.send("Common! Okie doke.")
                state.rarity = "common"
                state.auction_stage = 4
            elif latestMessage.startswith('uncom'):
                await message.channel.send("Uncommon! Fantastic. Everyone loves an uncommon thing.")
                state.rarity = "uncommon"
                state.auction_stage = 4
            elif latestMessage.startswith('rar'):
                await message.channel.send("Rare! How thrilling!")
                state.rarity = "rare"
                state.auction_stage = 4
            await message.channel.send("What is the full value of that item, in silver? (Ensure that you use the full value, rather than selling value)")
        else:
            await message.channel.send("Sorry, I didn't get that. Is your item common, uncommon, or rare?")

    # Item value
    elif state.auction_stage == 4:
        try:
            await message.channel.send("Your item's full value is " + str(int(latestMessage)) + " silver!\nIs that correct?")
            state.potential_state = int(latestMessage)
            state.return_to_step = 4
            state.auction_stage = 4.1
        except ValueError:
            await message.channel.send("What's the value in silver? (Make sure to use a whole number!)")

    # Hype modifier
    elif state.auction_stage == 5:
        if not state.item_value:
            state.item_value = state.potential_state
            state.potential_state = ""
        await message.channel.send("Do you want to hype up your item using performance, diplomacy, or other?")
        state.auction_stage = 6

    elif state.auction_stage == 6:        
        if latestMessage.startswith('perf'):
            await message.channel.send("Performance. Perf. What's your modifier?")
            state.hype = "performance"
            state.auction_stage = 10
        elif latestMessage.startswith('dipl'):
            await message.channel.send("Diplomacy. You cheeky so-and-so! What's your modifier?")
            state.hype = "diplomacy"
            state.auction_stage = 10
        elif latestMessage.startswith('oth'):
            await message.channel.send("Other. OK! As long as it's cleared by a GM! Which skill are you using?")
            state.auction_stage = 8
        else:
            await message.channel.send("Sorry, I didn't get that. Enter either \"performance\", \"diplomacy\", or \"other\"!")

    elif state.auction_stage == 7:
        await message.channel.send("Which skill are you using?")
        state.auction_stage = 8
    
    elif state.auction_stage == 8:
        await message.channel.send("You're using " + str(latestMessage) + ". Is that right?")
        state.potential_state = str(latestMessage)
        state.return_to_step = 7
        state.auction_stage = 8.1

    elif state.auction_stage == 9:
        if not state.hype:
            state.hype = state.potential_state
            state.potential_state = ""
        await message.channel.send("What's your ability's modifier?")
        state.auction_stage = 10

    # Percent starting value
    elif state.auction_stage == 10:
        try:
            await message.channel.send("Your modifier is " + str(int(latestMessage)) + "!\nIs that correct?")
            state.potential_state = int(latestMessage)
            state.return_to_step = 9
            state.auction_stage = 10.1
        except ValueError:
            await message.channel.send("Sorry, I didn't get that. What's your modifier? Be sure to use a whole number!")

    elif state.auction_stage == 11:
        if not state.modifier:
            state.modifier = state.potential_state
            state.potential_state = ""
        await message.channel.send("Let's choose a value to start the bidding at!\n"+
            "You can choose 10, 25, or 50 percent of the item's value.\n"+
            "(Starting at 10 percent will attract at least two bidders, which guarentees the auction will run!)\n"+
            "How high should we start the bid? (10, 25, or 50)")
        state.auction_stage = 12

    # Start the auction
    elif state.auction_stage == 12:
        try:
            if int(latestMessage.strip()) in [10, 25, 50]:
                await message.channel.send("Alright! Let's start the bidding at " + str(int(latestMessage)) + " percent!")
                state.item_percent = int(latestMessage)
                await message.channel.send("Are you ready to start the auction, or would you like to cancel or restart? (Type \"start\", \"restart\", or \"cancel\"!)")
                state.auction_stage = 13
            else:
                await message.channel.send("Sorry, I didn't get that. Enter either 10, 25, or 50!")
        except ValueError:
            await message.channel.send("Sorry, I didn't get that. Enter either 10, 25, or 50!")

    elif state.auction_stage == 13:
        if latestMessage.startswith('sta'):
            await message.channel.send("Let the bidding begin!")
            state.auction_stage = 14
        elif latestMessage.startswith('rest'):
            await message.channel.send("Ok! Let's restart.")
            init_state()
            state.auction = True
            set_current_user()
            state.auction_stage = 0
            await auctionSetup(message)
    else:
        if not state.game_running:
            await message.channel.send("Sorry, I didn't get that. Try again?")