import pyrogram
import my_que
from pyrogram import Client
from pyrogram import filters
import asyncio
import pytube_me
from pytube_me import vid_download
from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioVideoPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio
from pytgcalls.types.input_stream.quality import HighQualityVideo

from pytgcalls.types import AudioPiped
bot = pyrogram.Client(
    'py-tgcalls',
    api_id=10637638,
    api_hash='2acc3bec3be2681a2113ef754e3a8c29',
    bot_token = '5088830310:AAEFL6XnXHO8n9dw2kU-sf6I4U8OHxHjQVM',
)
api_id = '10637638'
api_hash = '2acc3bec3be2681a2113ef754e3a8c29'
bot_token = '5088830310:AAEFL6XnXHO8n9dw2kU-sf6I4U8OHxHjQVM'
session = 'BQBpt34F0skZhBu89RPIrA2zW343oN59cXoGYQID3k9piOnkZpbgMwVMH6Lb9RXgmeZjVXQws39HPeV0Sn6w-_YcgLYhSA6JgcYfGTIYL3vDl_BEB49cWDzrZ4TwopFUSQEn9yeJFqTI5qjesG-A0enbls5m3EYEQlQylLfciq3vb3_IPY3GIaz8heM7Pn-ADkeL9q8-AqwkBO3h9l1KNnY1oz8S6wicd_p5OT9QEnjTAv1ID8oIUk_jxo4REYrdSfix4dV7s66Ud2oyGbQH3ESZgK5Cw8EJeMoLmtqybcRCRIgBfFEkx7CL9VmloH7GjVS35AQRuLEpN6N7qDR-rCskAAAAATPwVagA'

client = Client(session, api_id, api_hash)





app = PyTgCalls(client)
app.start()
song_name = ''
@bot.on_message(filters.command('start'))
async def start(bot,msg):
    await bot.send_message(msg.chat.id,'Hello')
    randid = bot.rnd_id()
    print(randid)


@bot.on_message(filters.command('check'))
async def check(bot,msg):
    await bot.send_message(msg.chat.id,'Checked')
    #for admin in (await msg.chat.get_members(filter="administrators")):
    #    print(admin.user.id)
    #    if admin.user.id == msg.chat.id:
    #        await bot.send_message(msg.chat.id,'Your are admin')
    #    else:
    #        await bot.send_message(msg.chat.id,"Not Admin")
    if msg.from_user:
        admin = ''
        for admin in (await msg.chat.get_members(filter="administrators")):
            if msg.from_user.id == admin.user.id:
                print("this is admin")
            else:
                await bot.send_message(msg.chat.id,"Not Admin")

# @bot.on_message(filters.command('stream'))
# async def stream(bot,msg):
#     try:
#         await pytgcalls.join_group_call(
#             chat.id,
#             get_quality(song),
#             stream_type=StreamType().pulse_stream,
#         )
#     except (NoActiveGroupCall, GroupCallNotFound):
#         peer = await app.resolve_peer(chat.id)
#         await app.send(
#             CreateGroupCall(
#                 peer=InputPeerChannel(
#                     channel_id=peer.channel_id,
#                     access_hash=peer.access_hash,
#                 ),
#                 random_id=app.rnd_id() // 9000000000,
#             )
#         )

# async def get_youtube_stream():
#     proc = await asyncio.create_subprocess_exec(
#             'youtube-dl',
#             '-g',
#             '-f',
#             # CHANGE THIS BASED ON WHAT YOU WANT
#             'best[height<=?720][width<=?1280]',
#             'https://www.youtube.com/watch?v=asRapG6F32Q',
#             stdout=asyncio.subprocess.PIPE,
#             stderr=asyncio.subprocess.PIPE,
#         )

#     stdout, stderr = proc.communicate()
#     return stdout.decode().split('\n')[0]



@bot.on_message(filters.command('stream'))
async def stream(bot,msg):
    await bot.send_message(msg.chat.id,'Stream Start')
    # audio_file = ''
    # await app.join_group_call(msg.chat.id,AudioPiped(audio_file,))
    


@bot.on_message(filters.command('leave'))
async def leave(bot,msg):
    await bot.send_message(msg.chat.id,'leave')
    await app.leave_group_call(msg.chat.id)

@bot.on_message(filters.command('add'))
async def song_add(bot,msg):
    text = msg.text.split()[1]
    pytube_me.vid_download(url)
    await bot.send_message(msg.chat.id,'You added')

    #pytube_me.download(text)
    
@bot.on_message(filters.command('play'))
async def play(bot,msg):
    result = my_que.get_data()
    app.join_group_call(msg.chat.id,AudioPiped(result,))
@bot.on_message(filters.command('show'))
async def song_add(bot,msg):
    result = my_que.get_data()
    print(result)
    #pytube_me.download(text)    

asyncio.run(bot.run())
idle()

