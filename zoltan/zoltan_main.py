import state
from assets.functions import exit_response, toggle_game_running, help_response, info_response
from zoltan.stages.zoltan import zoltan_welcome, zoltan_goodbye, zoltan_start, zoltan_misunderstand
from zoltan.info.info_and_help import zoltan_help, zoltan_info
from zoltan.debug.debug_functions import zoltan_debug


async def zoltan_main():
    toggle_game_running(1)

    if exit_response():
        await zoltan_goodbye()

    elif help_response():
        await zoltan_help()

    elif info_response():
        await zoltan_info()

    elif "$zoltan" in state.message.content:
        await zoltan_welcome()

    elif "$debug" in state.message.content:
        await zoltan_debug()

    elif state.zoltan_stage == 1:
        await zoltan_start()

    else:
        await zoltan_misunderstand()

    toggle_game_running(-1)
