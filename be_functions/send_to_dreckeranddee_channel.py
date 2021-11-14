import discord
import os
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()

async def send_to_dreckeranddee_channel():
    channel_id_string = os.getenv("DISCORD_CHANNEL_ID")
    message = "The Mighty Zoltan has appeared!\nWant you know your future?\nNot spent you yet your most recent downtime ativity?\nHead into the dreckeranddee Discord channel,\nand type '$zoltan' to play. . .\nIf you dare!"
    channel = client.get_channel(int(channel_id_string))
    await channel.send(message)


@client.event
async def on_ready(): 
    await send_to_dreckeranddee_channel()

client.run(os.getenv('TOKEN'))