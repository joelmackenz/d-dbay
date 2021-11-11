import state
import time
from assets.responses import exit_responses, positiveResponses, negativeResponses, help_responses, info_responses

def set_current_user():
    terminatingIndex = str(state.message.author).index('#')
    state.current_user = str(state.message.author)[:terminatingIndex]

def toggle_game_running(forceState = 0):
    if (forceState > 0):
        state.game_running = True
    elif forceState < 0:
        state.game_running = False
    else:
        state.game_running = not state.game_running

def positiveResponse():
    if (any(word in str(state.message.content.lower()) for word in positiveResponses)):
        return True
    return False

def negativeResponse():
    if (any(word in str(state.message.content.lower()) for word in negativeResponses)):
        return True
    return False

def exit_response():
    if (any(word in str(state.message.content.lower()) for word in exit_responses)):
        return True
    return False

def help_response():
    if (any(word in str(state.message.content.lower()) for word in help_responses)):
        return True
    return False

def info_response():
    if (any(word in str(state.message.content.lower()) for word in info_responses)):
        return True
    return False

def messageWriterIsAuthor():
    if state.current_user == str(state.message.author):
        return True
    return False

async def paused_send(s):
    for i in s:
        await state.message.channel.send(i)
        one_sec_pause()
        
async def short_paused_send(s):
    for i in s:
        await state.message.channel.send(i)
        half_sec_pause()

async def long_paused_send(s):
    for i in s:
        await state.message.channel.send(i)
        twoSecPause()

def half_sec_pause():
    time.sleep(.5)

def one_sec_pause():
    time.sleep(1)

def twoSecPause():
    time.sleep(2)