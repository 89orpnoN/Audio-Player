import discord
from discord.ext import commands
import datetime

intenti = discord.Intents(guilds = True,members = True,presences = True,messages = True)
client = commands.Bot(command_prefix="!", intents = intenti)

utente = input("")


@client.event
async def on_ready():
    guilda = client.get_guild(615245635700129814)
    print(guilda)
    member = guilda.get_member_named(utente)
    print(member)
    role = await discord.utils.get(lambda role: role.name == "Eretico", guilda.roles)
    print(role)
    await member.add_roles(role)
    print("we have logged in as {0.user}".format(client))



client.run("OTgxOTI4MjI5Nzc2NTUxOTQ2.GjJp7k.wX6iAOorFQynnTHLNIzu7XghzPpFGpdRzCB3h0")