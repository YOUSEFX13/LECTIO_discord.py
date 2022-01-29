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


# load our local env so we dont have the token in public


# from lectio import Lectio


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
LECNAME = os.getenv('Lectio_name')
LECPASS = os.getenv('Lectio_pass')
SCHOOLID = os.getenv('Lectio_ID')

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
    if message.author == client.user:
        return

    if message.content == (prefix+'skema'):  # mike

        skema = (str(lec.getExercises()))

        anan = skema.replace("\'", "\"")

        xx = json.loads(anan)

        aa = (int(len(xx)-14))

        for ad in range(aa):
            global yy
            yy = xx[int(ad+14)]
            ff = str(yy['Frist'].split(curYear)[0])
            kk = ff.replace("-", "-"+curYear)
            fff = str(yy['Id'])

            liste = {}
            internal_marks = {kk: fff}
            liste.update(internal_marks)

        for l in thenumba:
            numberint = int(l)
            y = xx[numberint]

            time = y['Time']
            team = y['Team']
            teacher = y['Teacher']
            room = y['Room']
            urlid = y['Id']

            embed = nextcord.Embed(title="Link To Modul", url="https://www.lectio.dk/lectio/"+SCHOOLID+"/aktivitet/aktivitetforside2.aspx?absid="+urlid,
                                   description="Hello! Here is your schedule for the day :D ", color=0xffffff)

            embed.set_author(name="DEVSEVBOT", url="https://www.youtube.com/watch?v=989-7xsRLR4",
                             icon_url="https://i.imgur.com/jPJFHH3.png")

            embed.set_thumbnail(url="https://i.imgur.com/55EaVfW.png")
            embed.add_field(name="Time",
                            value=time, inline=False)
            embed.add_field(name="Team",
                            value=team, inline=False)
            embed.add_field(name="Teacher",
                            value=teacher, inline=True)
            embed.add_field(name="Room",
                            value=room, inline=True)

            embed.set_footer(
                text="Made by ๖ۣۜℜ𝒾bar𝒾⚔#9594 & жар#9179")

            await message.channel.send(embed=embed)


client.run(TOKEN)
