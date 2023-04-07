import discord
from discord.ext import commands
import msgcryptorLIB

client = discord.Client()

intents = discord.Intents().all()
client = commands.Bot(command_prefix="!",message_content=True, intents = intents)

@client.event
async def on_ready():
  print("we have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.content.startswith("!cr"):
    await message.delete()
    Messaggio = ((message.content).replace("!cr ", "")).split(" ", 1)
    Messaggio[1] = msgcryptorLIB.standardizzatore(Messaggio[1])
    intchiave = msgcryptorLIB.riconoscimentochiave(Messaggio[0])
    Messaggio_cifrato = msgcryptorLIB.encripter(Messaggio[1],intchiave)
    await message.channel.send(f"{Messaggio_cifrato} - {Messaggio[0]}")


  elif message.content.startswith("!de"):
    await message.delete()
    Messaggio = ((message.content).replace("!de ", "")).split(" ", 1)
    Messaggio[1] = msgcryptorLIB.standardizzatore(Messaggio[1])
    intchiave = msgcryptorLIB.riconoscimentochiave(Messaggio[0])
    Messaggio_cifrato = msgcryptorLIB.decripter(Messaggio[1],intchiave)
    await message.channel.send(f"{Messaggio_cifrato} - {Messaggio[0]}")


  elif message.content.startswith("!showkeys"):

    chiaviDISP = str(msgcryptorLIB.QNlinee())
    chiaviDISP = chiaviDISP.replace("[", "")
    chiaviDISP = chiaviDISP.replace("]", "")
    chiaviDISP = chiaviDISP.replace("'", "")
    msgcryptorLIB.QNlinee()
    await message.channel.send(f"le chiavi disponibili sono: {chiaviDISP}.")


client.run("OTgxOTI4MjI5Nzc2NTUxOTQ2.GjJp7k.wX6iAOorFQynnTHLNIzu7XghzPpFGpdRzCB3h0")
