import discord  # importowanie bibliotekii discord
from discord.ext import commands

import json  # importowanie jsona
import requests  # tworzenie requesta do strony
import random
import asyncio

bot = discord.Client()  # interpretuje bota jako użytkownika
bot = commands.Bot(command_prefix="$")  # prefix

open_json = open('config.json')  # otwieranie pliku json
data = json.load(open_json)  # ładowanie danych pliku json



sad_words = ["sad", "depressed", "unhappy", "angry", "depressing"]

krzysiu = ["fede", "krzychu", "krzyś", "krzysiu", "krzys"]

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


@bot.event  # Wiadomość o wystartowaniu bota
async def on_ready():
    print("{0.user} has Started.".format(bot))
    await bot.change_presence(activity=discord.Game('$help'))


@bot.event
async def serverstats(message):
    if message.content.startswith("$serverinfo"):

        server_name = str(message.guild.name)
        server_owner = str(message.guild.owner)

        await message.send(f"""***SERVER INFO: ***
        **Server Name: `{server_name}`
        Server Owner: `{server_owner}`
        Server ID: `{str(idserver)}`
        Full Count Of Users: `{str(arb)}`
        Number Of Members: `{str(arb - countas)}`
        Number Of Bots: `{str(countas)}`
        Number Of Channels: `{str(channel_count)}`
        Number Of Voice Channels: `{str(voice_count)}`
        Number Of Roles: `{str(role_count)}`
        Number Of Emojis: `{str(emoji_count)}`
        Number Of Boosts: `{str(ctx.message.guild.premium_subscription_count)}`
        Number Of Webhooks: `{str(lk)}`
        Verification Level: `{str(verification_level)}`
        Server Region: `{str(server_region)}`
        Server Created On: `{str(created_on)}`**""")


@bot.event
async def userstats(member: discord.Member = None):
    if discord.message.content.startswith("$userstats"):
        if member is None:
            member = discord.message.content.message.author
        else:
            pronoun = str(member)
        name = f"{member.name}#{member.discriminator}"
        status = discord.message.channel.author.status.name
        created_on = member.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S')
        userAvatarUrl = member.avatar_url
        join = member.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S')
        statoos = member.activity
        house = member.top_role
        permissions = member.permissions_in(discord.message.channel)
        # userhighest role
        await discord.message.channel.send("``` ```")
        await discord.message.channel.send(f"""**`Here's Some Dirt On:` {member.mention}!:
        Username is: `{str(member.name)}`
        UserTag is: `{str(member.discriminator)}`
        User ID is: `{str(member.id)}`
        User Presence is: `{str(status)}`
        User Is Playing: `{str(statoos)}`
        User Highest Role: `{str(house)}`
        User Created On: `{str(created_on)}`
        User Joined On: `{str(join)}`
        User Permissions: `{str(permissions)}`**""")
        await discord.message.channel.send(userAvatarUrl)
        await discord.message.channel.send("``` ```")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content

    # help
    if message.content.startswith('$help'):
        embed = discord.Embed(title=bot.user, description="Desc", color=0x00ff00)
        embed.add_field(name="Field1", value="hi", inline=False)
        embed.add_field(name="Field2", value="hi2", inline=False)
        embed.add_field(name="Field2", value="hi2", inline=False)
        await message.channel.send(userAvatarUrl)
        await message.channel.send(embed=embed)

    if msg.startswith('$inspire'):
        quote = get_quotes()
        await message.channel.send(quote)  # await message.channel.send() wysyłanie wiadomości przez bota

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

    if any(word in msg.lower() for word in
           krzysiu):  # jeżeli jakiekolwiek słowo w wiadomość będzie zawierało słowo z listy
        await message.channel.send("to pedał")  # wiadomość użytkownika jest konwertowana na małe litery msg.lower()
        # value = True
        # while (value):                                 # nieskończony loop
        #    await message.channel.send("to pedał")


bot.run(data['TOKEN'])
