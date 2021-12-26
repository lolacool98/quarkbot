#this will be quark's file

# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
from logging import logThreads
import discord
import re
import random

# IMPORT THE OS MODULE.
import os

# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv

# IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.
from discord.ext import commands

# IMPORT BOT MODULES
# import menu
import quarkimplicit
import quarkcommands

# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()

# GRAB THE API TOKEN FROM THE .ENV FILE.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
#print("----- My DISCORD TOKEN: ", DISCORD_TOKEN)

# CREATES A NEW BOT OBJECT WITH A SPECIFIED PREFIX. IT CAN BE WHATEVER YOU WANT IT TO BE.
bot = commands.Bot(command_prefix=os.getenv("COMMAND_PREFIX"), help_command=None)

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("Quark is in " + str(guild_count) + " guilds.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):

	#bot should not reply to itself, just users
	if message.author == bot.user:
		return
	if message.author.bot: return

	await quarkimplicit.on_message(bot, message)
	await bot.process_commands(message)

#commands file
@bot.command(name="ping")
async def ping(ctx, ping_name: str=None):
	await quarkcommands.ping(ctx, ping_name)

@bot.command(name="bubblewrap")
async def bubblewrap(ctx):
	await quarkcommands.bubblewrap(ctx)

@bot.command(name="credits")
async def credits(ctx):
	await quarkcommands.credits(ctx)

@bot.command(name="info")
async def info(ctx, info_name: str=None):
	await quarkcommands.info(ctx, info_name)
@bot.command(name="help")
async def help(ctx, info_name: str=None):
	await quarkcommands.info(ctx, info_name)

@bot.command(name="selfcare")
async def selfcare(ctx):
	await quarkcommands.selfcare(ctx)
	
# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(DISCORD_TOKEN)