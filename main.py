import discord  # importowanie bibliotekii discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import CommandNotFound

import os
import json  # importowanie jsona
import requests  # tworzenie requesta do strony
import random
import asyncio


intents = discord.Intents.all()
bot = discord.Client(intents=intents)  # interpretuje bota jako użytkownika

bot = Bot(command_prefix='$')  # prefix

open_json = open('config.json')  # otwieranie pliku json
data = json.load(open_json)  # ładowanie danych pliku json

# ładowanie komend z zewnętrznych plików
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):   # loopowanie przez folder w poszukiwaniu plików .py
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')     # usuwanie .py


sad_words = ["sad", "depressed", "unhappy", "angry", "depressing"]

starter_encouragements = [
    "Cheer up!",
    "Hang in there",
    "Giiiiiiiit jest"
]



def get_quotes():  # funkcja losująca cytaty z api
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " ~ " + "\"" + json_data[0]['a'] + "\""  # q - quote, a - author
    return (quote)


@bot.command(name='serverinfo')
async def fetchServerInfo(ctx, args):
    if(args[1] == "help"):
        await ctx.send("info")

    name = str(ctx.guild.name)
    region = str(ctx.guild.region)
    await ctx.send(f'Server Name: {name}')
    await ctx.send(f'Server region: {region}')


@bot.event                              # brak komendy
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        embed = discord.Embed(title="Nie znaleziono komendy ", description='Lista komend: $help', color=0xff0000)
        await ctx.send(embed=embed)
    raise error


@bot.event  # Wiadomość o wystartowaniu bota
async def on_ready():
    print("{0.user} has Started.".format(bot))
    await bot.change_presence(activity=discord.Game('$help'))

bot.run(data['TOKEN'])
