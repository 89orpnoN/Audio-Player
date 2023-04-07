import discord
from discord.ext import commands

intenti = discord.Intents(guilds = True,members = True,presences = True,messages = True)
client = commands.Bot(command_prefix="", intents = intenti)

youtubearray = ["y","o","u","t","u","b","e",".","c","o","m"]
mee6id= "159985870458322944"
mee6channel = "768517862276071454"
yourid = "981928229776551946"
@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    youtubearrayindex = 0
    #if str((message.channel.id) == mee6channel) and (message.author.id != yourid):
     #   if str(message.author.id) != mee6id:
      #      messaggio = message.content
       #     print(messaggio)
        #    for i in range(len(messaggio)):
         #       if messaggio[i] == youtubearray[youtubearrayindex]:
          #          if youtubearrayindex != 10:
           #             youtubearrayindex = youtubearrayindex + 1
            #        if youtubearrayindex == 10:
             #           startyoutubelink = i - 10
              #  else:
 #                   youtubearrayindex = 0
  #          await message.channel.send("!play " + messaggio[startyoutubelink:] )
   #     elif str(message.author.id) == mee6id:
    #        messages = await message.channel.history(limit=2).flatten()
     #       for i in range(len(messages)):
      #          if str(messages[i].author.id) == yourid:
       #             await messages[i].delete()
    if message.content.startswith("!play https://www.youtube.com/watch?v=GaXuMC_GHEE") == False:
        await message.channel.send("!play https://www.youtube.com/watch?v=GaXuMC_GHEE")



client.run("OTgxOTI4MjI5Nzc2NTUxOTQ2.GjJp7k.wX6iAOorFQynnTHLNIzu7XghzPpFGpdRzCB3h0")