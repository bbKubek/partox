from main import bot


@bot.command(name="help")
async def help(ctx):
	await ctx.channel.send("help")