# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


def updatevar():
    global source
    source = (open('Config.txt').read())
    global mylist
    mylist = source.split("=")[1]
    global prefix
    prefix = str(mylist)
    print(prefix)


updatevar()
one = 1


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

# join message


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    print(prefix+'Mike')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!')

# join message end


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == prefix+'Mike':
        response = 'Check'+' ' + (message.author.mention)
        await message.channel.send(response)

    if message.author == client.user:
        return

    if message.content == prefix+'github':
        response = 'Our Github page: https://github.com/YOUSEFX13/discord.py'
        await message.channel.send(response)


@client.event  # leave message
async def on_member_leave(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'{member.name},Left the Discord server!')


@client.event  # change prefix
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix+'prefix'):
        response = message.content.split(" ")[1]
        print(response)
        if len(response) == one:
            await message.channel.send('accepted the new prefix is'+' '+response)
            (open('Config.txt', 'w').write('prefix ='+response))
            updatevar()

        else:
            await message.channel.send('only one charecter')

client.run(TOKEN)
