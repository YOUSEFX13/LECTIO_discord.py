import discord
import os
# load our local env so we dont have the token in public
from dotenv import load_dotenv
# from discord.utils import get
# from discord import FFmpegPCMAudio
# from discord import TextChannel
import json
import datetime
from src.lectio import Lectio
from requests import get
import getpass
import sys

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
LECNAME = os.getenv('Lectio_name')
LECPASS = os.getenv('Lectio_pass')
SCHOOLID = os.getenv('Lectio_ID')
author1 = os.getenv('Author_1')
author2 = os.getenv('Author_2')

lec = Lectio(str(LECNAME), str(LECPASS), str(SCHOOLID))

skema = (str(lec.getSchedule()))

# print(str(LECNAME), str(LECPASS), str(GUILD))

print(skema)
