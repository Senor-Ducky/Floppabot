import discord
from discord.ext import commands
import os
import json
from dotenv import load_dotenv

load_dotenv()


client = command.bot("flop!")

@client.event
async def on_ready():
	print("logged in")

@client.command
async def balance(ctx):
	await open_account(ctx.author)

async def open_account(user):

	users = await get_bank_data()

	if str(user.id) in users:
		return false 
	else:
		users[str(user.id)]["wallet"] = 0
		users[str(user.id)]["Floppa Republic Bank"] = 1000

	with open("floppareserve", "w") as f:
		json.dump(users,f)

async def get_bank_data():
	with open("floppareserve", "r") as f:
		users = json.load(f)

		return users








client.run(os.getenv('TOKEN'))