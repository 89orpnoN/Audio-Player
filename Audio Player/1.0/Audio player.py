import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from pytube import YouTube
from pytube import Playlist
import glob
import os
import functools
import goto
import datetime
import asyncio

intenti = discord.Intents.all() #il bot è onnipotente
bot = commands.Bot(command_prefix='!', intents=intenti, heartbeat_timeout=500.0) #prefisso vuil dire che quando viene mandato un messaggio che inizia con "!" python prova ad avviare la funzione che ha il nome uguale all'inizio del messaggio

voice_client = "" #oggetto di connessione al canale
Queue = [] #lista di directory di brani da riprodurre
message = "" #ultimo messaggio valido mandato. da cui si possono prendere informazioni se sono mancanti
Status = "" #indica l'intenzione attuale del bot (cosa vorrei fargli fare) modifica i comportamenti di alcune funzioni


@bot.event
async def on_ready():
    #cerca le canzoni nella cartella
    files = glob.glob("*.mp4")
    for i in files:
        Queue.append(i.split("\\")[-1])

    #bot pronto
    print("we have logged in as {0.user}".format(bot)) #bot pronto


@bot.command()
async def play(ctx):
    global message
    global Status

    Status = "Play" #voglio che il bot riproduca una canzone

    if not ctx.author.voice: #controlla che l'utente sia in un canale vocale
        return await ctx.send('You are not connected to a voice channel')
    try: #prova a connettersi a un canale, se dà un errore probabilmente è già connesso
        global voice_client
        voice_client = await connect_to_channel(ctx)
    except:
        print("bot già nel canale")

    msg_text = ctx.message.content

    if msg_text.replace(" ","") != "!play": #controlla se c'è del testo dopo il "!play" se no allora non scaricare roba
        links_str = msg_text.split(" ", 1)[1]
        links_arr = links_str.split(";") #separa i vari link nel messaggio

        for i in links_arr:
            videos_links_arr = handlelink(i) #controlla che tipo di link è e ritorna una lista di link di brani

            for j in videos_links_arr: #scarica ogni singolo link
                download_song(j, str(len(Queue)) + ".mp4")
                await asyncio.sleep(0.1) #serve a dare il tempo a discord.py di mandare segnali di vita a discord

                if not voice_client.is_playing(): #se il bot non sta musicando allora fai parire la prima canzone
                    play_song(voice_client)

    else:

        if not voice_client.is_playing(): #se non c'è roba da scaricare e il bot non sta musicando allora musica
            if len(Queue) > 0:
                play_song(voice_client)
            else:
                print("non ci sono canzoni nella fila")
                await ctx.send("non ci sono canzoni nella fila")

    message = ctx #segna questo messaggio come valido


@bot.command()
async def stop(ctx):
    global Queue
    global Status
    global voice_client

    if not ctx.guild.voice_client.is_connected(): #se il bot non è connesso: fermati.
        return await ctx.send('I am not connected to a voice channel')

    Status = "Stop" #voglio che il bot smetta di riprodurre ed esca
    voice_client = ctx.guild.voice_client
    voice_client.stop() #fermarsi trigghera le funzione after di play.
    await voice_client.disconnect() #disconnettiti


@bot.command()
async def remove_queue(ctx):
    global Status

    print(Queue)
    Status = "RemoveQueue"

    if ctx.guild.voice_client.is_connected(): #se il bot è connesso: ferma la riproduzione e togli il controllo al file.
        source = voice_client.source
        voice_client.stop()
        source.cleanup()
    else:
        print("bot non in riproduzione")

    for i in range(len(Queue)): #rimuovi tutte le canzoni dalla queue e dalla cartella
        print(Queue)
        remove_first_song()



def remove_first_song():
    global Queue

    try:
        os.remove(Queue[0]) #rimuovi la prima canzone della queue dalla cartella
        Queue = Queue[1:] #rimuovi la prima canzone dalla queue
    except:
        print("file in uso da un processo")


def handlelink(link):
    try: #se trasformare il link in un oggetto "youtube" (che rappresenta un video singolo) non da errore allora ritorna un array del link
        YouTube(link)
        Songs = [link]
    except: #se trasformare il link in "youtube" da errore allora probabilmente il link è una playlist, allora ritorna un array dei link dei video contenuti nella playlist
        playlist = Playlist(link)
        Songs = playlist.video_urls
    return Songs


async def connect_to_channel(ctx):
    voice_channel = ctx.author.voice.channel #dato il messaggio di origine ottieni il canale vocale in cui sta l'utente
    await voice_channel.connect(timeout=500.0, reconnect=True, self_deaf=True, self_mute=False) #connettiti al canale vocale ottenuto
    voice_client = ctx.guild.voice_client
    return voice_client #ritorna l'oggetto della connessione al canale


def on_song_stop(channel, audio_source, error):  #questa funzione viene chiamata quando la musica viene interrota naturalmente o da uno stop
    global Queue

    print("entrato in on_song_stop")

    channel.cleanup() #"pulisci" la "connessione al canale"
    audio_source.cleanup() #togli il file che era in riproduzione dalla ram
    remove_first_song() #togli la canzone dalla cartella e dalla queue

    if Status in ["RemoveQueue","Stop"]: #siccome qeusta funzione viene chiamata quando la canzone si interrompe è comodo specificare cosa si vuole fare.
        return
    if Status in ["Play"]: #se ci sono canzoni nella queue allora riproducile, altrimenti ferma il bot
        if len(Queue) > 0:
            play_song(channel)
        else:
            stop(message)


def play_song(channel):
    print("partito")
    global Queue
    print(Queue[0])
    if len(Queue) > 0:
        audio_source = FFmpegPCMAudio(Queue[0]) #dalla queue carica il file
        channel.play(audio_source, after=functools.partial(on_song_stop, channel, audio_source)) #riproduci il file e quando si ferma la riproduzione chiama la funzione: on_song_stop(channel,audio_source)
    else:
        print("fine della queue")
        print(Queue)

def download_song(string, filename): #dato un link di canzone scarica la canzone nella directory dello script e aggiungila alla queue

    yt = YouTube(string)
    stream = yt.streams.get_audio_only("mp4")
    stream.download(filename=filename)
    Queue.append(str(len(Queue)) + ".mp4")
    print(Queue)




bot.run('OTgxOTI4MjI5Nzc2NTUxOTQ2.GjJp7k.wX6iAOorFQynnTHLNIzu7XghzPpFGpdRzCB3h0')
