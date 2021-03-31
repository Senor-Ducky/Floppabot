import discord
from discord.ext import commands
import os
import json
import random

async def open_account(user):

		users = await get_bank_data()

		if str(user.id) in users:
			return False 
		else:
			users[str(user.id)] = {}
			users[str(user.id)]["wallet"] = 0
			users[str(user.id)]["Floppa Republic Bank"] = 1000

		with open("cogs/bank.json", "w") as f:
			json.dump(users,f)

async def get_bank_data():
		with open("cogs/bank.json", "r") as f:
			users = json.load(f)

			return users

async def update_bank(user, change=0, mode = "wallet"):
		users = await get_bank_data()
		users[str(user.id)][mode] += change

		with open("cogs/bank.json", "w") as f:
			json.dump(users,f)

			bal = [users[str(user.id)]["wallet"], users[str(user.id)]["Floppa Republic Bank"]]

		return bal

class Economy(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.command()
	async def balance(self, ctx):
		await open_account(ctx.author)

		user = ctx.author

		users = await get_bank_data()

		wallet_amt = users[str(user.id)]["wallet"]
		bank_of_floppa = users[str(user.id)]["Floppa Republic Bank"]

		em = discord.Embed(title = f"{ctx.author}'s balance", color = discord.Color.purple())
		em.add_field(name = "Wallet", value = wallet_amt)
		em.add_field(name = "Floppa National Bank Account", value = bank_of_floppa)
		await ctx.send(embed = em)

	@commands.command()
	async def beg(self, ctx):
		await open_account(ctx.author)

		user = ctx.author

		users = await get_bank_data()

		earnings = random.randrange(101)

		await ctx.send(f"You have been given {earnings} floppabucks")

		users[str(user.id)]["wallet"] += earnings

		with open("bank.json", "w") as f:
			json.dump(users,f)

	@commands.command()
	async def withdraw(self, ctx, amount = None):
		await open_account(ctx.author)

		if amount == None:
			await ctx.send("Please enter the amount to withdraw")
			return

		bal = await update_bank(ctx.author)

		amount = int(amount)

		if amount>bal[1]:
			await ctx.send("Insuffecient Funds!")
			return
		if amount<0:
			await ctx.send("Enter Positive amount retard")
			return

		await update_bank(ctx.author, amount)
		await update_bank(ctx.author, -1*amount, "Floppa Republic Bank")
		await ctx.send(f"you withdrew {amount} floppabucks.")

	@commands.command()
	async def deposit(self, ctx, amount = None):
		await open_account(ctx.author)

		if amount == None:
			await ctx.send("Please enter the amount to deposit")
			return

		bal = await update_bank(ctx.author)

		amount = int(amount)

		if amount>bal[0]:
			await ctx.send("Insuffecient Funds!")
			return
		if amount<0:
			await ctx.send("Enter Positive amount retard")
			return

		await update_bank(ctx.author, -1*amount)
		await update_bank(ctx.author, amount, "Floppa Republic Bank")
		await ctx.send(f"you deposit {amount} floppabucks.")

	@commands.command()
	async def send(self, ctx, member:discord.Member,amount = None):
		await open_account(ctx.author)
		await open_account(member)

		if amount == None:
			await ctx.send("Please enter the amount to send")
			return

		bal = await update_bank(ctx.author)

		amount = int(amount)

		if amount>bal[1]:
			await ctx.send("Insuffecient Funds!")
			return
		if amount<0:
			await ctx.send("Enter Positive amount retard")
			return

		await update_bank(ctx.author, -1*amount, "Floppa Republic Bank")
		await update_bank(member, amount, "Floppa Republic Bank")
		await ctx.send(f"you sent {amount} floppabucks.")

	@commands.command()
	async def rob(self, ctx, member:discord.Member):
		await open_account(ctx.author)
		await open_account(member)

		bal = await update_bank(member)


		if bal[0]<100:
			await ctx.send(f"You can't rob {member}, they're too poor.")
			return

		earnings = random.randrange(0, bal[0])

		await update_bank(ctx.author, earnings)
		await update_bank(member, -1*earnings)
		await ctx.send(f"you robbed {member} for {earnings} floppabucks.")
		

	@commands.command()
	async def slot(self, ctx, amount = None):
		await open_account(ctx.author)

		if amount == None:
			await ctx.send("Please enter the amount to deposit")
			return

		bal = await update_bank(ctx.author)

		amount = int(amount)

		if amount>bal[0]:
			await ctx.send("Insuffecient Funds!")
			return
		if amount<0:
			await ctx.send("Enter Positive amount retard")
			return

		final = []
		for i in range(3):
			a = random.choice(["🎀", "🔮", "🏺", "💎", "💰"])
			final.append(a)

		await ctx.send(str(final))

		if final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
			await update_bank(ctx.author, 2*amount)
			await ctx.send("Floppa has blessed you with fortune!")
		else:
			await update_bank(ctx.author, -1*amount)
			await ctx.send("your flopping days are over")




def setup(client):
	client.add_cog(Economy(client))

	






