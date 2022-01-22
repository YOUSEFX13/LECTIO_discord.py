# bot.py
import nextcord
import os
# load our local env so we dont have the token in public
from dotenv import load_dotenv
from nextcord.utils import get
from nextcord import FFmpegPCMAudio
from nextcord import TextChannel
from youtube_dl import YoutubeDL

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = nextcord.Intents.default()
intents.members = True
client = nextcord.Client(intents=intents)


def updatevar():
    global source
    source = (open('Config.txt').read())
    global mylist
    mylist = source.split("=")[1]
    global prefix
    prefix = str(mylist)
    print('Current prefix is = '+prefix)


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

    if message.content == prefix+'Mike':  # mike
        response = 'Check'+' ' + (message.author.mention)
        await message.channel.send(response)

    if message.author == client.user:
        return

    if message.content == prefix+'github':  # github command
        response = 'Our Github page: https://github.com/YOUSEFX13/discord.py'
        await message.channel.send(response)

    if message.content == prefix+'help':  # github command
        response = 'WIP'
        await message.channel.send(response)

    if message.content.startswith(prefix+'play'):  # PLAY COMMAND

        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        voice = get(client.voice_clients, guild=message.guild)
        global url
        url = message.content.split(" ")[1]

        if not voice.is_playing():
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
            URL = info['url']
            voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
            voice.is_playing()
            await message.channel.send(':notes: Bot is playing '+url+' enjoy.')

        else:
            await message.channel.send("Bot is already playing some other music")
            return

    if message.content == (prefix+'join'):  # JOIN COMMAND
        channel = message.author.voice.channel
        voice = get(client.voice_clients, guild=message.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

    if message.content == (prefix+'leave'):  # leave command
        voice = get(client.voice_clients, guild=message.guild)
        await voice.disconnect() and message.channel.send('left the channel')


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
