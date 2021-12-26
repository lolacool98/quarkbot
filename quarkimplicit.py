import re
import random

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
# Sammich is always listening
async def on_message(bot, message):

    #defining functions for this module
	content = message.content.lower()
	cry = '😢'

	#bot should not reply to itself, just users
	if message.author == bot.user:
		return
	if message.author.bot: return

	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	if content == "hello":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send("Hi!")

	if "quark" in content:
		await message.channel.send("That's me!")

	if "good bot" in content:
		#Quark IS a good bot, thankyouverymuch
		if "do" in content:
			await message.channel.send("I AM a good bot!")
		#Quark knows it is a good bot
		else:
			await message.channel.send("Thank you :)")

    #scream command
	if content.startswith("aaa"):
		await message.channel.send("AAAAAAAAAAAAAAAAAAAAAAAAH!")
	
    #SAD!
	if re.search("sa{2,}d", content):
		await message.add_reaction(cry)
	if re.search("sa{2,}d!", content):
		await message.add_reaction(cry)
	if content == "sad" or content == "sadness":
		await message.add_reaction(cry)
	if content == "sad!":
		await message.add_reaction(cry)
    
	#kawaii
	if "owo" in content:
		if "coworker" in content:
			return
		else:
			await message.channel.send("uwu")
	if "uwu" in content:
		await message.channel.send("OwO")

    # wuh-oh
	if "uh oh" in content or "oh no" in content:
		await message.channel.send(":grimacing:")

	#yeah toast!
	if "toast" in content:
		await message.channel.send("YEAH TOAST!!!")