import discord  # importowanie bibliotekii discord
from discord.ext import commands
import json  # importowanie jsona
import requests  # tworzenie requesta do strony
import random


prefix = commands.Bot(command_prefix="$")

open_json = open('config.json')  # otwieranie pliku json
data = json.load(open_json)  # ładowanie danych pliku json

bot = discord.Client()  # interpretuje bota jako użytkownika

sad_words = ["sad", "depressed", "unhappy", "angry", "depressing"]

krzysiu = ["fede", "krzychu", "krzyś", "krzysiu", "krzys", ]

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


@bot.event          # Wiadomość o wystartowaniu bota
async def on_ready():
    print("{0.user} has Started.".format(bot))
    await bot.change_presence(activity=discord.Game('help'))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content

    if msg.startswith('inspire'):
        quote = get_quotes()
        await message.channel.send(quote)           # await message.channel.send() wysyłanie wiadomości przez bota

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

    if any(word in msg for word in krzysiu):
        await message.channel.send("to pedał")


bot.run(data['TOKEN'])