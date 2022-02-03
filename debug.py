# debugbot.py
import os
import nextcord
from dotenv import load_dotenv
from nextcord.utils import get
from nextcord import Embed, FFmpegPCMAudio
from nextcord import TextChannel
from uritemplate import variables
from youtube_dl import YoutubeDL
from src.lectio import Lectio
import json
import datetime
from requests import get
import getpass


# load our local env so we dont have the token in public


# from lectio import Lectio


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
LECNAME = os.getenv('Lectio_name')
LECPASS = os.getenv('Lectio_pass')
SCHOOLID = os.getenv('Lectio_ID')
userid = os.getenv('linux_user')

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


def lectiotime():
    a = datetime.datetime.now()

    global curDay
    curDay = a.strftime("%d")
    if curDay.startswith('0'):
        curDay = curDay.split('0')[1]
        pass

    else:
        pass

    global curMonth
    curMonth = a.strftime("%m")
    if curMonth.startswith('0'):

        curMonth = curMonth.split('0')[1]
        pass

    else:
        pass

    global curYear
    curYear = a.strftime("%Y")

    global curDate
    curDate = (curDay+'/'+curMonth+'-'+curYear)

    global DANUMBA
    DANUMBA = {}
    global thenumba
    thenumba = {}


lectiotime()

lec = Lectio(LECNAME, LECPASS, SCHOOLID)


@client.event
async def on_message(message):

    if message.content == (prefix+'ip'):  # mike
        if message.author.id == 400570716401041408 or message.author.id == 383201612098830338:

            ip = get('https://api.ipify.org').content.decode('utf8')

            embed = nextcord.Embed(title="Link To Modul", url="",
                                   description="Hello! Here is your login for the server ", color=0xffffff)

            embed.set_author(name="DEVSEVBOT", url="https://www.youtube.com/watch?v=989-7xsRLR4",
                             icon_url="https://i.imgur.com/jPJFHH3.png")

            embed.set_thumbnail(url="https://i.imgur.com/55EaVfW.png")
            embed.add_field(name="IP",
                            value=ip, inline=False)
            embed.add_field(name="login",
                            value=(getpass.getuser()+'@'+ip), inline=False)

            embed.set_footer(
                text="Made by ๖ۣۜℜ𝒾bar𝒾⚔#9594 & жар#9179")

            user = client.get_user(message.author.id)
            await user.send(embed=embed)

            await message.channel.send('look at your dm')
        else:
            await message.channel.send((message.author.mention)+'you are not allowed to do that')


client.run(TOKEN)
