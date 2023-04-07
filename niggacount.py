import discord
from discord.ext import commands


intenti = discord.Intents(guilds = True,members = True,presences = True,messages = True,message_content=True)
client = commands.Bot(command_prefix="!", intents = intenti)
word = ["negro", "nigga", "negrp"]
importantmessages = []
importantnames = []
userword = []
numword = []
tempindex = []
nummagici = [1,3,69,420,256,999,10,20]
limitpazzp = None
loadingnum = 0
@client.event
async def on_ready():
  global loadingnum
  global importantnames
  global importantmessages
  global userword
  global numword
  global tempindex
  global guilda
  guilda = client.get_guild(615245635700129814)
  channels = guilda.text_channels
  print(len(channels))
  print(channels)
  for i in range(len(channels)):
    print(channels[i].id)
    messages = channels[i].history(limit=limitpazzp)
    print("messages: " + str(messages))
    messages = messages.flatten()
    for msg in messages:
      loadingnum = loadingnum + 1
      print(loadingnum)
      for o in range(len(word)):
        if word[o].lower() in msg.content.lower():
          importantmessages.append(msg)
  for p in range(len(importantmessages)):
    importantnames.append(importantmessages[p].author)

  n = 0
  print("importantnames : " + str(importantnames))

  while len(importantnames) != 0:

    userword.append(importantnames[0])

    print("userword : " + str(userword))

    for j in range(len(importantnames)):

      if userword[n] == importantnames[j]:

        tempindex.append(j)

        print("tempindex : " + str(tempindex))

    numword.append(len(tempindex))

    print("numword : " + str(numword))

    for k in range(len(tempindex)):

      importantnames = importantnames[  : tempindex[k] - k] + importantnames[tempindex[k] + 1 - k:]

      print("importantnames : " + str(importantnames))


    tempindex.clear()

    n = n+1



  print("we have logged in as {0.user}".format(client))
  print("importantnames : " + str(importantnames))
  print("tempindex : " + str(tempindex))
  print("userword : " + str(userword))
  print("numword : " + str(numword))

@client.event
async def on_message(message):
  global numword
  print("è partito")
  if message.author != client.get_user(981928229776551946):
    if ((message.content).lower()).find("negro") != -1:
      print("ha trovato il negro")
      print(message.content)

      for i3 in range(len(userword)):
        if message.author == userword[i3]:
          numword[i3] = numword[i3] + 1
        else:
          if i3 == len(userword)-1:
            userword.append(message.author)
            numword.append(1)

      for i in range(len(numword)):
        print("sta ciclando le numword")
        print(str(i) + ":" + str(len(numword)))

        for i2 in range(len(nummagici)):
          print("sta ciclando i numeri magici")
          print(str(i2) + ":" + str(len(nummagici)))

          if numword[i] == nummagici[i2] and userword[i] == message.author:
            print("il punteggio coincide")
            print(str(numword[i]) + "=" + str(nummagici[i2]))
            print(str(message.author) + "=" + str(userword[i]))

            if message.author == userword[i]:
              print("autore coincide")
              print(str(message.author) + "=" + str(userword[i]))
              await message.channel.send("grande " + message.author.display_name + " sei il razzista modello")
              numword[i] = numword[i] + 1

    if message.content.startswith("!cerca parola "):
      comando = message.content
      comando = comando.replace("!cerca parola ","")
      parolaeutente = comando.split("\" \"")
      parolaeutente[0] = parolaeutente[0].replace("\"","")
      parolaeutente[1] = parolaeutente[1].replace("\"", "")
      await srchword(parolaeutente[0],parolaeutente[1],message)
    print("userword : " + str(userword))
    print("numword : " + str(numword))
    print("")
    print("")

async def srchword(word,user,message):
  print("func srchword")
  global guilda
  global loadingnum
  count = 0
  channels = guilda.text_channels
  print(len(channels))
  print(channels)
  for i in range(len(channels)):
    print(channels[i].id)
    messages = await channels[i].history(limit=limitpazzp).flatten()

    for msg in messages:
      loadingnum = loadingnum + 1
      print(loadingnum)
      if word.lower() in msg.content.lower() and msg.author.display_name.lower() == user.lower():
        count = count + 1
  await message.channel.send(str(user) + " ha scritto " + str(word) + " " + str(count) + " volte")




client.run("OTgxOTI4MjI5Nzc2NTUxOTQ2.GjJp7k.wX6iAOorFQynnTHLNIzu7XghzPpFGpdRzCB3h0")