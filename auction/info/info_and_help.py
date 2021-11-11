async def auctionInfo(message):
    await message.channel.send("Auction off your item with Drecker & Dee!\n\n"+
    "Can’t find a buyer? Can’t talk fast enough to hold your own auction? Want to turn your bounty into gold?\n"+
    "Put your item up for bid, and be guaranteed to receive at least over your asking price, or your item back!\n"+
    "We’ll only auction your item if it has at least two bidders, and we’ll do it all for the low-low cost of 5 percent of the item's value!\n\n"+
    "To start, type **$auction**. This will initiate the auction prompts to auction your item!\n"+
    "You will input your item's name and value, what price you would like the bidding to start at, and how you will hype-up your item around the town (using performance, diplomacy, or something else!)\n\n"+
    "You can start the bidding at these values:\n\n"+
    "- 10%: *safe*. Attracts 1d6 + 1 bidders (auction is guaranteed to run).\n"+
    "- 25%: *difficult*. Attracts 1d4 bidders.\n"+
    "- 50%: *very difficult*. Attracts 1d4 - 1 bidders.\n\n"+
    "The number of bidders, then, is determined by the bidders attracted from the *starting bid* and by the *hype modifier*.\n"+
    "If zero or one bidder is attracted, the auction will not commence, and the PC gets the item back from D&D Bay.\n"+
    "D&D Bay is no longer interested in that item at all, as it has proven itself unsellable.\n\n"+
    "If there are bidders, the auction commences!\n\n"
    "If you'd like more in-depth details on the auction, go to <https://github.com/joelmackenz/d-dbay#readme>\n")

async def auctionHelp(message):
    await message.channel.send("Need some help? Here's what you can do:\n\n"+
        "**$auction** - runs the auction\n"+
        "**$info** - info on how the auction works\n"+
        "If at any time you would like to cancel an auction, type **\"stop\"** or **\"quit\"**")