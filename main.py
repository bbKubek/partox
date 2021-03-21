import discord  # importowanie bibliotekii discord
import json  # importowanie jsona
import requests  # tworzenie requesta do strony
import random

open_json = open('config.json')  # otwieranie pliku json
data = json.load(open_json)  # ładowanie danych pliku json

bot = discord.Client()  # interpretuje bota jako użytkownika

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


@bot.event          # Wiadomość o wystartowaniu bota
async def on_ready():
    print("{0.user} has Started.".format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content

    if msg.startswith('$inspire'):
        quote = get_quotes()
        await message.channel.send(quote)           # await message.channel.send() wysyłanie wiadomości przez bota


    if msg.startswith("$new"):
        encouraging_message = msg.split("$new ", 1)[1]
        update_encouragements(encouraging_message)      # dodawanie zachęty przez użytkownika
        await message.channel.send("New encouraging message added.")

    if msg.startswith("$del"):
        encouragements = []
        if "encouragements" in db.keys():
            index = int(msg.split("$del", 1)[1])
            delete_encouragment(index)
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)


bot.run(data['TOKEN'])
