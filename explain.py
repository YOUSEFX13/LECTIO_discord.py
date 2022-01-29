# bot.py
import nextcord
import os
# load our local env so we dont have the token in public
from dotenv import load_dotenv
from nextcord.utils import get
from nextcord import FFmpegPCMAudio
from nextcord import TextChannel
from youtube_dl import YoutubeDL
import json
import datetime
from src.lectio import Lectio


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
LECNAME = os.getenv('Lectio_name')
LECPASS = os.getenv('Lectio_pass')
SCHOOLID = os.getenv('Lectio_ID')

intents = nextcord.Intents.default()
intents.members = True
client = nextcord.Client(intents=intents)


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

    print(f'{client.user} is connected to the following guild:\n',
          f'{guild.name}(id: {guild.id})\n')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

# join message


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    await client.change_presence(status=nextcord.Status.online, activity=nextcord.Game(name='Lectio'))


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

    if message.content == prefix+'github':  # github command
        response = 'Link to github: https://github.com/YOUSEFX13/discord.py'
        await message.channel.send(response)

    if message.content == prefix+'help':  # list of commands

        embed = nextcord.Embed(title="Here is a list of commands!",
                               description="List of commands", color=0xffffff)

        embed.set_author(name="DEVSEVBOT", url="https://www.youtube.com/watch?v=989-7xsRLR4",
                         icon_url="https://i.imgur.com/jPJFHH3.png")

        embed.set_thumbnail(url="https://i.imgur.com/55EaVfW.png")

        embed.add_field(
            name=prefix+'help', value="Shows a list of commands! ", inline=False)
        embed.add_field(
            name=prefix+'Mike', value="Does a Mike check!", inline=False)
        embed.add_field(
            name=prefix+'github', value="Our **Github page** (its private right now so you wont be able to see it D:", inline=False)
        embed.add_field(
            name=prefix+'prefix', value="Change the prefix (only one character)", inline=False)
        embed.add_field(
            name=prefix+'skema', value="Shows the **Schedule** for the day!", inline=False)
        embed.add_field(
            name=prefix+'afl', value="Shows the **afleveringer** for the week!", inline=False)

        embed.set_footer(
            text="Made by ๖ۣۜℜ𝒾bar𝒾⚔#9594 & жар#9179")

        channel = client.get_channel(936548630146449508)

        await message.channel.send(embed=embed)

    if message.content == (prefix+'skema'):  # skema

        lectiotime()
        response = 'Skemaet for idag' + ' ' + (message.author.mention)
        skema = (str(lec.getSchedule()))

        anan = skema.replace("\'", "\"")

        x = json.loads(anan)

        aa = (int(len(x)))

        for ad in range(aa):
            global yy

            yy = x[int(ad)]
            ff = str(yy['Time'].split(curYear)[0])
            kk = ff.replace("-", "-"+curYear)

            DANUMBA[str(kk)] = str(ad)

            gg = DANUMBA.get(str(curDate), 'del')
            u = [(gg, {gg: gg})]

            thenumba.update(u)

        if 'del' in thenumba:
            thenumba.pop('del')
        else:
            pass
        for l in thenumba:
            numberint = int(l)
            y = x[numberint]

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
            channel = client.get_channel(936548630146449508)
            await channel.send(embed=embed)  # channel.send(respone)

    if message.content == (prefix+'afl'):  # se dine Aflevering

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

                embed = nextcord.Embed(title="Link To Modul(WIP)", url="https://www.lectio.dk/lectio/"+SCHOOLID+"/aktivitet/aktivitetforside2.aspx?absid="+urlid,
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

    if message.content.startswith(prefix+'prefix'):
        response = message.content

        if message.content == (prefix+'prefix'):
            await message.channel.send('You need to input a character  like !prefix .')

        elif len(message.content.split(" ")[1]) == one:

            response = message.content.split(" ")[1]
            print(response)

            await message.channel.send('accepted the new prefix is'+' '+response)
            (open('Config.txt', 'w').write('prefix ='+response))
            updatevar()

        else:
            await message.channel.send('only one charecter')

    #
    # MUSIC PART
    #

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


@ client.event  # leave message
async def on_member_leave(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'{member.name},Left the Discord server!')


client.run(TOKEN)
