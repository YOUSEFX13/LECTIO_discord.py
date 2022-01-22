# debugbot.py
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


@client.event
async def on_message(message):
    if message.author == client.user:
        return

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


client.run(TOKEN)
