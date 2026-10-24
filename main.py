import discord

from discord.ext import commands
from discord     import FFmpegPCMAudio
import asyncio
import signal

import secret
import src

from secret import apy_keys
from src import traductor, preguntas, buttons
from src.buttons import VistaButton

import datetime
import random
import requests
#import bbc

play_queues = {}  # guild_id: {"queue": asyncio.Queue, "voice_client": VoiceClient, "playing": False}


# Crea una instancia de Intents
intents = discord.Intents.default()  # Usa default para los intentos comunes
intents.message_content = True  # Habilita el acceso a los mensajes (si es necesario)
intents.members = True

# Crea el bot con los intents
client = commands.Bot(command_prefix='!', intents=intents)

correcta = ""
correcta_body = ""
voice_connected=False

# ----------------------------------------------------------------------------------------------------------------      Events

"""
@client.event
async def on_voice_state_update(member, before, after):
    print(member.id)
    for guild in client.guilds:
        if guild.voice_client:  # El bot está en un canal de voz
            voice = guild.voice_client  # Asignamos el VoiceClient (no el nombre del canal)
            break
        
    # Comprobar si el miembro se conecta a un canal de voz
    if before.channel is None and after.channel is not None:
        print(f'{member.name} se ha conectado al canal {after.channel.name}')
    # Comprobar si el miembro se desconecta de un canal de voz
    elif before.channel is not None and after.channel is None:
        print(f'{member.name} se ha desconectado del canal {before.channel.name}')
    else:
        print(f'{member.name} joined {before.channel.name}')
        if member.id == XUSTES:
            print("Hola XUSTES")
            source = FFmpegPCMAudio('media/sounds/xustes.mp3')
            player = voice.play(source)  # Puedes personalizar el 'after'
        if member.id == YURII:
            print("Hola XUSTES")
            source = FFmpegPCMAudio('media/sounds/xustes.mp3')
            player = voice.play(source)  # Puedes personalizar el 'after'
"""



@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        #print(f'{member.name} se ha conectado al canal {after.channel.name}')
        if member.id == apy_keys.XUSTES:
            source = FFmpegPCMAudio('media/sounds/mc_xustes.mp3')
            player = after.channel.guild.voice_client.play(source)  # Usamos after.channel.guild para obtener el VoiceClient
        elif member.id == apy_keys.YURII:
            source = FFmpegPCMAudio('media/sounds/yuri.mp3')
            player = after.channel.guild.voice_client.play(source)  # Usamos after.channel.guild para obtener el VoiceClient
        elif member.id == apy_keys.WENJIA:
            source = FFmpegPCMAudio('media/sounds/wenjia.mp3')
            player = after.channel.guild.voice_client.play(source)  # Usamos after.channel.guild para obtener el VoiceClient
        elif member.id == apy_keys.HAERING:
            source = FFmpegPCMAudio('media/sounds/haering.mp3')
            player = after.channel.guild.voice_client.play(source)  # Usamos after.channel.guild para obtener el VoiceClient
        elif member.id == apy_keys.DAVID:
            source = FFmpegPCMAudio('media/sounds/david.mp3')
            player = after.channel.guild.voice_client.play(source)  # Usamos after.channel.guild para obtener el VoiceClient
    elif before.channel is not None and after.channel is None:
        #print(f'{member.name} se ha desconectado del canal {before.channel.name}')
        if member.id == apy_keys.XUSTES:
            source = FFmpegPCMAudio('media/sounds/b_xustes.mp3')
            player = after.channel.guild.voice_client.play(source)  # Usamos after.channel.guild para obtener el VoiceClient
        elif member.id == apy_keys.YURII:
            source = FFmpegPCMAudio('media/sounds/b_yuri.mp3')
            player = after.channel.guild.voice_client.play(source)  # Usamos after.channel.guild para obtener el VoiceClient
        elif member.id == apy_keys.WENJIA:
            source = FFmpegPCMAudio('media/sounds/b_wenjia.mp3')
            player = after.channel.guild.voice_client.play(source)  # Usamos after.channel.guild para obtener el VoiceClient
        elif member.id == apy_keys.HAERING:
            source = FFmpegPCMAudio('media/sounds/b_haering.mp3')
            player = after.channel.guild.voice_client.play(source)  # Usamos after.channel.guild para obtener el VoiceClient
        elif member.id == apy_keys.DAVID:
            source = FFmpegPCMAudio('media/sounds/b_david.mp3')
            player = after.channel.guild.voice_client.play(source)  # Usamos after.channel.guild para obtener el VoiceClient
    # Comprobar si el miembro cambia de canal de voz
    elif before.channel != after.channel:
        print(f'{member.name} ha cambiado de canal de voz de {before.channel.name} a {after.channel.name} con :{member.id}')



@client.event
async def on_ready():
    channel = client.get_channel(apy_keys.PYTBOT_channel)
    await channel.send("I'm Alive")
    print("Arrancamos")


@client.event
async def on_member_join(member):
    channel = client.get_channel(apy_keys.PYTBOT_channel)
    await channel.send(f"¿Quien ha invitado a {member.display_name} al server?")
    print(f"Se unió {member.display_name}")


@client.event
async def on_member_remove(member):
    channel = client.get_channel(apy_keys.PYTBOT_channel)
    await channel.send(f"Tanta paz lleves {member.display_name}, como dejas")
    print(f"Se fue {member.display_name}")


@client.event
async def on_raw_member_remove(payload):
    channel = client.get_channel(apy_keys.PYTBOT_channel)
    member_id = payload.user_id
    member = await client.fetch_user(member_id)
    await channel.send(f"Tanta paz lleves {member.display_name}, como dejas")
    print(f"Se fue {member.display_name}")

# ----------------------------------------------------------------------------------------------------------------      Commands
#---------#
@client.command()
async def join(ctx):
    await join_channel(ctx)

@client.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        play_queues.pop(ctx.guild.id, None)

@client.command()
async def play(ctx, nombre_sonido: str):
    if ctx.author.voice:
        path = f'media/sounds/{nombre_sonido}.mp3'
        try:
            with open(path, 'rb'):
                pass
            await enqueue_audio(ctx.author.voice.channel, path)
        except FileNotFoundError:
            await ctx.send(f"❌ El sonido '{nombre_sonido}' no existe.")
    else:
        await ctx.send("🔇 Debes estar en un canal de voz para reproducir sonidos.")

@client.command()
async def cola(ctx):
    guild_id = ctx.guild.id
    if guild_id in play_queues:
        items = list(play_queues[guild_id]["queue"]._queue)
        if items:
            await ctx.send("🎵 En cola:\n" + "\n".join(items))
        else:
            await ctx.send("✅ La cola está vacía.")
    else:
        await ctx.send("🧺 No hay cola activa para este servidor.")
                       
"""
@client.command()
async def marro(ctx):
    await play(ctx, 'marro')
"""

@client.command()
async def imbd(ctx, *, option=None):
    if option is None:
        await ctx.send("Dame mas info")
    elif option == 'fav':
        try:
            url = "https://"+apy_keys.IMBD+"/api/v1/getFanFavorites"
            querystring = {"country": "ES"}
            headers = {
                "x-rapidapi-key": apy_keys.RAPIDAPI_KEY,
                "x-rapidapi-host": apy_keys.IMBD
            }
            response = requests.get(url, headers=headers, params=querystring)
            data = response.json()
            movies = data.get('data', {}).get('list', [])
            titles = [movie['originalTitleText']['text'] for movie in movies]
            respuesta = "Lista de películas favoritas de la audiencia:\n"
            for i, title in enumerate(titles, 0):
                respuesta += f"**{i}** - {title}\n"
            await ctx.send(respuesta)
        except KeyError as e:
            await ctx.send(f"Error en la respuesta de la API: {str(e)}")
        except Exception as e:
            await ctx.send(f"Ocurrió un error inesperado: {str(e)}")

    elif option == 'top10':
        url = "https://"+apy_keys.IMBD+"/api/v1/getWeekTop10"

        headers = {
            "x-rapidapi-key": apy_keys.RAPIDAPI_KEY,
            "x-rapidapi-host": apy_keys.IMBD
        }

        response = requests.get(url, headers=headers)

        print(response.json())
    elif option == 'onStream':
        url = "https://"+apy_keys.IMBD+"/api/v1/getWhatsStreaming"

        querystring = {"country": "US"}

        headers = {
            "x-rapidapi-key": apy_keys.RAPIDAPI_KEY,
            "x-rapidapi-host": apy_keys.IMBD
        }

        response = requests.get(url, headers=headers, params=querystring)

        print(response.json())
    elif option.lower().startswith('movie '):
        movie = option[6:]
        movie = movie.replace(" ", "_")
        url = "https://"+apy_keys.IMBD+"/api/v1/searchIMDB"

        querystring = {"query": movie}

        headers = {
            "x-rapidapi-key": apy_keys.RAPIDAPI_KEY,
            "x-rapidapi-host": apy_keys.IMBD
        }

        response = requests.get(url, headers=headers, params=querystring)
        try:
            data = response.json()
            # print(data)
            resultados = [{'title': item.get('title', 'Desconocido'),
                           'actors': item.get('stars', 'Desconocido'),
                           'year': item.get('year', 'Desconocido'),
                           'image': item.get('image', 'No disponible')} for item in
                          data['data']]
            respuesta = f"Lista de películas de nombre '__{movie}__':\n"
            await ctx.send(respuesta)
            for resultado in resultados:  # [:3]
                respuesta = ""
                titulo = f"**Titulo**:  {resultado['title']}\n"
                actores = f"**Actores**: {resultado['actors']}\n"
                anno = f"**Año**:     {resultado['year']}\n"
                imagen = f"**Imagen**:  {resultado['image']}\n"

                respuesta += titulo + anno + actores + imagen
                await ctx.send(respuesta)
        except KeyError as e:
            await ctx.send(f"Error en la respuesta de la API: {str(e)}")
        except Exception as e:
            await ctx.send(f"Ocurrió un error inesperado: {str(e)}")

    await ctx.send("End")


#---------------------------------------------------------------------------------------------------------SECONDARY
async def join_channel(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            return await channel.connect()
        else:
            return ctx.voice_client
    else:
        await ctx.send("¡Debes estar en un canal de voz!")
        return None

# Función que se encarga de reproducir audios en cola
async def play_next(guild_id):
    queue_info = play_queues[guild_id]
    queue = queue_info["queue"]
    voice_client = queue_info["voice_client"]

    if queue_info.get("playing"):
        return  # Ya está reproduciendo

    queue_info["playing"] = True

    while not queue.empty():
        source_path = await queue.get()
        audio_source = FFmpegPCMAudio(source_path)

        done = asyncio.Event()

        def after_playing(error):
            if error:
                print(f"Error reproduciendo: {error}")
            done.set()

        voice_client.play(audio_source, after=after_playing)
        await done.wait()

    queue_info["playing"] = False

async def enqueue_audio(channel, path):
    guild_id = channel.guild.id

    # Conectar si el bot no está ya en ese canal
    if channel.guild.voice_client is None:
        vc = await channel.connect()
    else:
        vc = channel.guild.voice_client

    # Crear cola si no existe
    if guild_id not in play_queues:
        play_queues[guild_id] = {
            "queue": asyncio.Queue(),
            "voice_client": vc,
            "playing": False
        }

    # Encolar audio
    await play_queues[guild_id]["queue"].put(path)

    # Lanzar play_next si no está activo
    if not play_queues[guild_id]["playing"]:
        asyncio.create_task(play_next(guild_id))

async def play_sound(interaction, sonido):
    user = interaction.user
    if user.voice and user.voice.channel:
        if sonido == 1:
                path = f'media/sounds/rol/fireball.mp3'
        elif sonido == 2:
                path = f'media/sounds/rol/thudershoot.mp3'
        elif sonido == 3:
                path = f'media/sounds/rol/healpot.mp3'
        elif sonido == 4:
                path = f'media/sounds/rol/cast.mp3'
        elif sonido == 5:
                path = f'media/sounds/rol/crow.mp3'
        elif sonido == 6:
                path = f'media/sounds/rol/espada.mp3'
        elif sonido == 7:
                path = f'media/sounds/rol/llamarada.mp3'
        elif sonido == 8:
                path = f'media/sounds/rol/explosion-fireball.mp3'
        elif sonido == 9:
                path = f'media/sounds/rol/medievalParty.mp3'
        elif sonido == 10:
                path = f'media/sounds/rol/espada_2.mp3'
        elif sonido == 11:
                path = f'media/sounds/rol/hammer.mp3'
        elif sonido == 12:
                path = f'media/sounds/rol/monster-cry.mp3'
        elif sonido == 13:
                path = f'media/sounds/rol/spell.mp3'
        elif sonido == 14:
                path = f'media/sounds/rol/wolf.mp3'
        elif sonido == 15:
                path = f'media/sounds/rol/arrow.mp3'
        elif sonido == 16:
                path = f'media/sounds/rol/bear.mp3'
        try:
            with open(path, 'rb'):
                pass
                await enqueue_audio(user.voice.channel, path)
        except FileNotFoundError:
            await interaction.channel.send(f" El sonido '{sonido}' no existe.")
    else:
        await interaction.channel.send(" Debes estar en un canal de voz.")

@client.command()
async def verBotones(ctx):
    view = VistaButton(play_sound)
    await ctx.send("mandado", view=view) 


# Cierre limpio del bot
async def close_bot():
    print("Cerrando bot...")
    await client.close()

def register_signals(loop):
    try:
        for sig in (signal.SIGINT, signal.SIGTERM):
            loop.add_signal_handler(sig, lambda: asyncio.ensure_future(close_bot()))
    except NotImplementedError:
        import threading
        def win_kb_listener():
            try:
                while True:
                    input()
            except EOFError:
                pass
            asyncio.run_coroutine_threadsafe(close_bot(), loop)

        thread = threading.Thread(target=win_kb_listener)
        thread.daemon = True
        thread.start()
        #threading.Thread(target=win_kb_listener, daemon=True).start()

# Main
if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    register_signals(loop)

    try:
        loop.run_until_complete(client.start(apy_keys.TOKEN))
    except (KeyboardInterrupt, SystemExit):
        print("KeyboardInterrupt detectado.")
    finally:
        print("Limpiando recursos...")
        loop.run_until_complete(close_bot())
        loop.close()