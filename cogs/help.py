import discord
from discord.ext import commands
from discord.ext.commands import Bot


class Example(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        owner_id = '@bbKubek#0531'
        embed = discord.Embed(title="Help Menu")
        embed.add_field(name="Bot owner", value=owner_id, inline=True)
        embed.add_field(name="Field2", value="hi2", inline=False)
        embed.add_field(name="Komendy: ", value="serverinfo, inspire", inline=False)
        embed.add_field(name="Field2", value="hi2", inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Example(bot))
