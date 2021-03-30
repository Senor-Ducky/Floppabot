import discord
from discord.ext import commands
import os
import json
from dotenv import load_dotenv
import random

load_dotenv()




client = commands.Bot(command_prefix = "flop!")

@client.event
async def on_ready():
	print("logged in")

@client.command()
async def balance(ctx):
	await open_account(ctx.author)

	user = ctx.author

	users = await get_bank_data()

	wallet_amt = users[str(user.id)]["wallet"]
	bank_of_floppa = users[str(user.id)]["Floppa Republic Bank"]

	em = discord.Embed(title = f"{ctx.author}'s balance", color = discord.Color.purple())
	em.add_field(name = "Wallet", value = wallet_amt)
	em.add_field(name = "Floppa National Bank Account", value = bank_of_floppa)
	await ctx.send(embed = em)

@client.command()
async def beg(ctx):
	await open_account(ctx.author)

	user = ctx.author

	users = await get_bank_data()

	earnings = random.randrange(101)

	await ctx.send(f"You have been given {earnings} floppabucks")

	users[str(user.id)]["wallet"] += earnings

	with open("bank.json", "w") as f:
		json.dump(users,f)



async def open_account(user):

	users = await get_bank_data()

	if str(user.id) in users:
		return False 
	else:
		users[str(user.id)] = {}
		users[str(user.id)]["wallet"] = 0
		users[str(user.id)]["Floppa Republic Bank"] = 1000

	with open("bank.json", "w") as f:
		json.dump(users,f)

async def get_bank_data():
	with open("bank.json", "r") as f:
		users = json.load(f)

		return users








client.run(os.getenv('TOKEN'))