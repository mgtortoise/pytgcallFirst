import pyrogram
import asyncio
import config
from config import config
from pyrogram import Client
from pyrogram import filters
from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioVideoPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio
from pytgcalls.types.input_stream.quality import HighQualityVideo
from pytgcalls.types import AudioPiped
bot = pyrogram.Client(
    'py-tgcalls',
    api_id=config.api_id,
    api_hash=config.api_hash,
    bot_token = config.bot_token,
)
client = Client(config.session,config.api_id,config.api_hash)
app = PyTgCalls(client)
app.start()
@bot.on_message(filters.command('start'))
async def start(bot,msg):
    await bot.send_message(msg.chat.id,'Hello')
    randid = bot.rnd_id()
    print(randid)

asyncio.run(bot.run())
idle()