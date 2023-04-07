import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from pytube import YouTube
import glob
import os
import functools


intenti = discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents = intenti)

Playlist = []

@bot.event
async def on_ready():
    print("we have logged in as {0.user}".format(bot))
    files = glob.glob("*.mp4")
    for i in files:
        Playlist.append(i.split("\\")[-1])

@bot.command()
async def play(ctx):
    if not ctx.author.voice:
        return await ctx.send('You are not connected to a voice channel')
    try:
        voice_client = await connectToChannel(ctx)
    except:
        voice_client = discord.VoiceProtocol(bot,ctx.author.voice.channel)
    msgs = ctx.message.content.split(" ",1)[1]
    SongsArr = msgs.split(";")
    for i in SongsArr:
        downloadSong(i,str(len(Playlist)) + ".mp4",voice_client)
    if not voice_client.is_playing():
        playSong(voice_client)

@bot.command()
async def stop(ctx):
    # Check if the bot is in a voice channel
    if not ctx.guild.voice_client:
        return await ctx.send('I am not connected to a voice channel')

    # Stop playing audio and disconnect from the voice channel
    voice_client = ctx.guild.voice_client
    voice_client.stop()
    await voice_client.disconnect()

async def connectToChannel(ctx):
    voice_channel = ctx.author.voice.channel
    await voice_channel.connect(timeout=60.0, reconnect=True, self_deaf=False, self_mute=False)
    voice_client = ctx.guild.voice_client
    return voice_client

def playNextSong(channel,error):
    global Playlist
    os.remove(Playlist[0])
    Playlist = Playlist[1:]
    playSong(channel)

def playSong(channel):
    print("partito")
    if not channel.is_playing():
        global Playlist
        print(Playlist[0])
        audio_source = FFmpegPCMAudio(Playlist[0])
        channel.play(audio_source,after=functools.partial(playNextSong,channel))
def downloadSong(string,filename, channel):
    yt = YouTube(string)
    stream = yt.streams.get_audio_only("mp4")
    stream.download(filename=filename)
    Playlist.append(str(len(Playlist)) + ".mp4")
    print(Playlist)

bot.run('OTgxOTI4MjI5Nzc2NTUxOTQ2.GjJp7k.wX6iAOorFQynnTHLNIzu7XghzPpFGpdRzCB3h0')