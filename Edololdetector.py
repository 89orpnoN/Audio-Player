import discord
from discord.ext import commands
import datetime



intenti = discord.Intents(guilds = True,members = True,presences = True,messages = True,message_content=True)
client = commands.Bot(command_prefix="!", intents = intenti)



@client.event
async def on_ready():
  print("we have logged in as {0.user}".format(client))
  global CSTATUS  #status del gioco a cui sta giocando edo
  global guilda #server operativo
  global canale #canale operativo
  global memberEDO #membro soggetto
  global gioco #gioco interessato
  global EDOstate #edostate ha 0 = none, 1 =  Giocando a lol , 2 = giocando non a lol , 3 = non ho ancora deciso
  EDOstate = [0,0]
  guilda = client.get_guild(615245635700129814)
  canale = client.get_channel(985243606652682240)
  memberEDO = guilda.get_member_named("Nonpro98#4597")
  gioco = "League of Legends"
  print(memberEDO)
  CSTATUS = memberEDO.activity
  if memberEDO.activity != None:
    CSTATUS = memberEDO.activity.name
    print(memberEDO.activity.name)

    if CSTATUS == gioco:
      print(CSTATUS)
      EDOstate[0] = 1
      global data_inizio
      data_inizio = datetime.datetime.now()
      print("starting raccoglimemento tempo")
      #await canale.send("edo sta giocando a LOL")

    elif memberEDO.activity == None:
      CSTATUS = memberEDO.activity

@client.event
async def on_member_update(memberB,memberA):
    global EDOstate
    if memberB == memberEDO:
        if memberA.activity != None:
            await edo_inizia_a_giocare(memberB, memberA)
        else:
            await edo_non_gioca_piu(memberB, memberA)

    if EDOstate[0] == 1 and EDOstate[1] == 0:
        print("starting raccoglimemento tempo")
        global data_inizio
        data_inizio = datetime.datetime.now()

        EDOstate[1] = 1
    elif EDOstate[0] == 0 or EDOstate[0] == 2:
        if EDOstate[1] == 1:
            global data_fine
            data_fine = datetime.datetime.now()
            EDOstate[1] = 0
            global tempo_sessione
            tempo_sessione = data_fine - data_inizio






async def edo_inizia_a_giocare(memberB,memberA):
    global CSTATUS
    global EDOstate
    if memberA.activity.name == gioco:
        if memberB.activity != None:
            if memberB.activity.name != gioco:
                CSTATUS = memberA.activity.name
                EDOstate[0] = 1
                await canale.send("edo sta giocando a LOL")
        else:
            CSTATUS = memberA.activity.name
            EDOstate[0] = 1
            await canale.send("edo sta giocando a LOL")
    else:
        await edo_non_gioca_piu(memberB, memberA)


async def edo_non_gioca_piu(memberB,memberA):
    global CSTATUS
    global EDOstate
    if memberB.activity != None:
        if memberB.activity.name == gioco:
            if memberA.activity != None:
                if memberA.activity.name != gioco:
                    CSTATUS = memberA.activity.name
                    EDOstate[0] = 2
                    await canale.send("edo non sta più giocando a LOL")
            else:
                CSTATUS = memberA.activity
                EDOstate[0] = 0
                await canale.send("edo non sta più giocando a LOL")
        else:

            CSTATUS = memberA.activity
    else:

        CSTATUS = None






@client.event
async def on_message(message):
    if message.content.startswith("!status padre di edoardo"):
        await statusPedo(message)

    if message.content.startswith("!tempo sessione di edoardo"):
        global data_inizio
        tempo_richiesta = datetime.datetime.now()
        global EDOstate
        if EDOstate[0] == 1:
            await message.channel.send(f"edo è in game su lol da {str(await deltatime_in_hours(data_inizio,tempo_richiesta))} ore e {await deltatime_in_seconds()} minuti")
        elif EDOstate[0] == 0 or EDOstate[0] == 2:
            await message.channel.send("edoardo fortunatamente non sta giocando a LOL")

    if message.content.startswith("!inizio sessione di edoardo"):
        if EDOstate[0] == 1:
            await message.channel.send(f"edo è in game su lol dalle {str(data_inizio)} ")
        elif EDOstate[0] == 0 or EDOstate[0] == 2:
            await message.channel.send("edoardo fortunatamente non sta giocando a LOL")

    if message.content.startswith("!vardev"):
        for name in dir():
            myvalue = eval(name)
            await message.channel.send(f"{name} is {type(name)} and is equal to {myvalue} \n")
            print(f"{name} is {type(name)} and is equal to {myvalue} ")


async def deltatime_in_hours(data_inizio,tempo_richiesta):
    global resto
    deltatempo = tempo_richiesta - data_inizio
    print(deltatempo)
    tempo_ore = int(deltatempo.days or 0)*24
    print(deltatempo.seconds)
    resto =int(deltatempo.seconds or 0) % 3600
    tempo_ore = (resto - deltatempo.seconds) / 3600
    print(tempo_ore)
    return int(tempo_ore)

async def deltatime_in_seconds():
    global resto
    tempo_minuti = (resto - (resto % 60))/60
    return int(tempo_minuti)

async def statusPedo(message):
    global CSTATUS
    if CSTATUS != gioco:
        await message.channel.send("il padre di edo è tornato col latte")
    elif CSTATUS == gioco:
        await message.channel.send("il padre di edo è andato a comprare il latte...")



client.run("OTgxOTI4MjI5Nzc2NTUxOTQ2.GjJp7k.wX6iAOorFQynnTHLNIzu7XghzPpFGpdRzCB3h0")