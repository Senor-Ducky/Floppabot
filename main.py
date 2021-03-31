import discord
from discord.ext import commands
import os
import dotenv
from dotenv import load_dotenv

load_dotenv()


client = commands.Bot(command_prefix = "flop!")


@client.event
async def on_ready():
	print("logged in")

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')











client.run(os.getenv('TOKEN'))