# debugbot.py
import os
import nextcord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = nextcord.Intents.default()
intents.members = True
client = nextcord.Client(intents=intents)


client.run(TOKEN)
