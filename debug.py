# debugbot.py
import os
import discord
from dotenv import load_dotenv
from src.lectio import Lectio
import json
import datetime
from requests import get
import getpass
import sys

# load our local env so we dont have the token in public


# from lectio import Lectio


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
LECNAME = os.getenv('Lectio_name')
LECPASS = os.getenv('Lectio_pass')
SCHOOLID = os.getenv('Lectio_ID')

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
    print('Current prefix is = '+prefix)


updatevar()


def lectiotime():
    global a
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
    global Weekbefore
    Weekbefore = a - datetime.timedelta(days=7)

    global WeekBFFIX
    WeekBFFIX = (str(Weekbefore.day)+'/' +
                 str(Weekbefore.month)+'-'+str(Weekbefore.year))

    global maxweek
    maxweek = a + datetime.timedelta(days=7)

    global DANUMBA
    DANUMBA = {}
    global thenumba
    thenumba = {}
    global liste
    liste = {}
    global opgavekeys
    opgavekeys = {}


lectiotime()

lec = Lectio(LECNAME, LECPASS, SCHOOLID)


@client.event
async def on_message(message):

    if message.content == (prefix+'afl'):  # se dine Aflevering
        lec = Lectio(LECNAME, LECPASS, SCHOOLID)
        lectiotime()
        response = 'Here is your request' + ' ' + (message.author.mention)
        skema = (str(lec.getExercises()))
        channel = client.get_channel(936837622574219305)
        await channel.send(response)

        anan = skema.replace("\'", "\"")

        xx = json.loads(anan)

        aa = (int(len(xx)-14))

        for ad in range(aa):
            global yya
            yya = xx[int(ad+14)]
            ff = str(yya['Frist'].split(curYear)[0])
            kk = ff.replace("-", "-"+curYear)
            fff = str(yya['Id'])
            # das = str(ad+14)
            # intdas = int(ad+14)

            liste.update({kk: fff})
        opgavekeys = list(liste.keys())

        for keynum in range(len(opgavekeys)):

            na = str(opgavekeys[keynum])
            keyyear = int(na.split("-")[1])
            keymonth = int((na.split("/")[1]).split("-")[0])
            keyday = int((na.split("-")[0]).split("/")[0])
            keydate = datetime.datetime(keyyear, keymonth, keyday)

            if keydate >= Weekbefore and keydate >= a and keydate < maxweek:

                yyy = xx[keynum+14]

                Frist = yyy['Frist']
                team = yyy['Hold']
                Opgavetitel = yyy['Opgavetitel']
                Elevtid = yyy['Elevtid']
                urlid = yyy['Id']
                Opgavenote = yyy['Opgavenote']

                embed = discord.Embed(title="Link To Modul(WIP)", url="https://www.lectio.dk/lectio/"+SCHOOLID+"/aktivitet/aktivitetforside2.aspx?absid="+urlid,
                                      description="Hello! Here is your afleveringer for the week :D ", color=0xffffff)

                embed.set_author(name="DEVSEVBOT", url="https://www.youtube.com/watch?v=989-7xsRLR4",
                                 icon_url="https://i.imgur.com/jPJFHH3.png")

                embed.set_thumbnail(url="https://i.imgur.com/55EaVfW.png")
                embed.add_field(name="Frist",
                                value=Frist, inline=False)
                embed.add_field(name="Team",
                                value=team, inline=False)
                embed.add_field(name="Opgavetitel",
                                value=Opgavetitel, inline=True)
                embed.add_field(name="Elevtid",
                                value=Elevtid, inline=True)
                if Opgavenote == '':
                    pass
                else:
                    embed.add_field(name='Opgavenote',
                                    value=Opgavenote, inline=False)

                embed.set_footer(
                    text="Made by ๖ۣۜℜ𝒾bar𝒾⚔#9594 & жар#9179")
                await channel.send(embed=embed)
            else:
                pass

    if message.content == prefix+'restart':
        print('orcun')
        sys.stdout.flush()
        os.execv(sys.executable, ['python'] + sys.argv)
client.run(TOKEN)
