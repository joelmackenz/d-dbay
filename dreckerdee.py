#!/usr/bin/python3.9.7
import discord
import os
from zoltan.debug.debug_functions import zoltan_debug
from state import init_state
import state
from dotenv import load_dotenv
from zoltan.router.game_router import game_router

load_dotenv()
client = discord.Client()

# Bot sign in
@client.event
async def on_ready():
    print('{0.user}'.format(client) + ' logged in!')
    init_state()

# Message Responses
@client.event
async def on_message(message):

    if not state.game_running:
        if message.author == client.user:
            return

        state.message = message

        if state.game:
            await game_router(message)
        elif ("$auction") in message.content:
            state.game = "ddbay"
            await on_message(message)
        elif ("$zoltan") in state.message.content:
            state.game = "zoltan"
            await on_message(message)
        elif("$debug") in state.message.content:
            await zoltan_debug()

        state.message = {}

client.run(os.getenv('TOKEN'))