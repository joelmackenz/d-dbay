import state
from assets.functions import paused_send, long_paused_send


async def zoltan_info():
    await long_paused_send([
        "I am the Almighty Zoltan.",
        "If you wish to see into the future, insert 10 sp.",
        "If you wish to see the even cooler future, insert 5 gp.",
        "Every future gives you a perk you can use in the next game.",
        "Standard future perks offer either a +1 or +2 bonus.",
        "Cooler future perks offer either a +3 or +4 bonus, *and they're cooler*.",
        "For the full code and more info, see the whole project at <https://github.com/joelmackenz/dreckerdee#readme>"
    ])


async def zoltan_help():
    await long_paused_send(["Dare you ask the mighty Zoltan for help?!"])
    await paused_send([
        "that's fine.",
        "Enter any of the following, " + state.current_user + ":",
        "**$info** - info on how the game works",
        "**standard** or **cooler** - select a future for the Almighty Zoltan to tell, and pay either 10 sp or 5 gp",
        "**stop** or **quit** - end the game"
    ])
