import state
from auction.auction_main import auction_main
from zoltan.zoltan_main import zoltan_main

async def game_router(message):
    if state.game == "ddbay":
        await auction_main(message)
    if state.game == "zoltan":
        await zoltan_main()