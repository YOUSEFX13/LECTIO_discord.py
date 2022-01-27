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


# lec = Lectio(LECNAME, LECPASS, SCHOOLID)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix+'skema'):  # mike

        numberint = int(message.content.split(" ")[1])

        lec = Lectio(LECNAME, LECPASS, SCHOOLID)
        skema = (lec.getSchedule())
        svar = str(skema)
        anan = svar.replace("\'", "\"")
        x = json.loads(anan)
        y = x[numberint]

        time = y['Time']
        team = y['Team']
        teacher = y['Teacher']
        room = y['Room']

        embed = nextcord.Embed(title="Link To Lectio", url="https://www.lectio.dk",
                               description="Hello! Here is your schedule for the day :D ", color=0x109319)

        embed.set_author(name="DEVSEVBOT", url="https://www.youtube.com/watch?v=989-7xsRLR4",
                         icon_url="https://pbs.twimg.com/profile_images/1327036716226646017/ZuaMDdtm_400x400.jpg")

        embed.set_thumbnail(url="https://i.imgur.com/55EaVfW.png")

        embed.add_field(name="Field 1 Title",
                        value="This is the value for field 1. This is NOT an inline field.", inline=False)
        embed.add_field(name="Field 2 Title",
                        value="It is inline with Field 3", inline=True)
        embed.add_field(name="Field 3 Title",
                        value="It is inline with Field 2", inline=True)

        embed.set_footer(
            text="Made by ๖ۣۜℜ𝒾bar𝒾⚔#9594 & жар#9179")

        await message.channel.send(embed=embed)


client.run(TOKEN)
