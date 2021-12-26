#credits
async def credits(ctx):
	await ctx.channel.send("Special thanks go to: \n- turnip, my mom \n- RLee, for his *insanely* helpful troubleshooting and explanations \n- and Sammich, my sister.")

#info
async def info(ctx, info_name):
	if info_name == None:
		await ctx.channel.send("I can do lots of things!")
		await ctx.channel.send("Type `$credits` to see some credits.")
		await ctx.channel.send("Type `$bubblewrap` to pop some bubble wrap.")
		await ctx.channel.send("Type `$selfcare` for a mental health check-in.")
		await ctx.channel.send("Type `$info [command name]` about any of these for some additional info.")
		await ctx.channel.send("There's more in the works! And...I've got some surprises up my sleeve c:")
		return
	lower_info_name = info_name.lower()

    #info
	if lower_info_name == "info":
		await ctx.channel.send("Haha, nice try! You know what this command does.")

    #credits
	elif lower_info_name == "credits":
		await ctx.channel.send("Roll credits!")
    
	#bubblewrap
	elif info_name == "bubblewrap":
		await ctx.channel.send("Popping bubble wrap is therapeutic. Try it! :)")
	
	#self care
	elif info_name == "selfcare":
		await ctx.channel.send("Feeling down? Need a little mental health break? Type `$selfcare` to take a moment and recalibrate.")

	else:
		await ctx.channel.send("Oops! Sorry, I didn't catch that. Try again?")

help = info

#ping pong
async def ping(ctx, ping_name):
	if ping_name == None:
		await ctx.channel.send("Pong")
		return

#bubble wrap
async def bubblewrap(ctx):
	await ctx.channel.send("Here's some bubble wrap: ")
	await ctx.channel.send("||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!|| ||pop!||")

#self care 
async def selfcare(ctx):
	await ctx.channel.send("Let's take a moment and check in.")
	await ctx.channel.send("1. Take a deep breath. Exhale slowly. Take another breath. Exhale slowly. \n2. Have you had a glass of water recently? If not, go get one. \n3. Have you had a meal today? If not, grab a snack. \n4. Have you gone for a walk recently? Stretching your legs is a good way to reset your brain. \n5. Have you gotten some exercise today? Get your blood moving a bit! \n6. Did you take your meds? Do that if you need to. \n7. Do you have a pet? Go interact with them for 5 minutes.")
	await ctx.channel.send("Take another deep breath, then exhale slowly. Things will be okay.")