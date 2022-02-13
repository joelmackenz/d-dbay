from auction.stages.auctionSetup import welcome, goodbye, auctionSetup
from auction.info.info_and_help import auctionHelp, auctionInfo
from auction.stages.auction import auction
from assets.responses import *
import state

async def auction_main(message):
    if ("$help") in message.content:
        await auctionHelp(message)
    
    if ("$info") in message.content:
        await auctionInfo(message)

    if ("$auction") in message.content:
        await welcome(message)

    elif (1 <= state.auction_stage):
        await auctionSetup(message)

    # Exit 
    elif ((state.current_user == str(message.author)) and (any(word in str(message.content) for word in exit_responses))):
        await goodbye(message)

    if state.auction_stage == 14:
        await auction(message)