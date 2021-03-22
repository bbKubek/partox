# po dodaniu osobnego pliku listener nasłuchującego wiadomości można używać komendy help

import discord
from discord.ext import commands

krzysiu = ["fede", "krzychu", "krzyś", "krzysiu", "krzys"]


class Listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.lower() in krzysiu:
            await message.channel.send('to pedał 🌈')

def setup(bot):
    bot.add_cog(Listener(bot))
