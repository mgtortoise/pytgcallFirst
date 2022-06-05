import pyrogram
from pyrogram import Client
from pyrogram import filters
import asyncio
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
#session = 'BQBpt34F0skZhBu89RPIrA2zW343oN59cXoGYQID3k9piOnkZpbgMwVMH6Lb9RXgmeZjVXQws39HPeV0Sn6w-_YcgLYhSA6JgcYfGTIYL3vDl_BEB49cWDzrZ4TwopFUSQEn9yeJFqTI5qjesG-A0enbls5m3EYEQlQylLfciq3vb3_IPY3GIaz8heM7Pn-ADkeL9q8-AqwkBO3h9l1KNnY1oz8S6wicd_p5OT9QEnjTAv1ID8oIUk_jxo4REYrdSfix4dV7s66Ud2oyGbQH3ESZgK5Cw8EJeMoLmtqybcRCRIgBfFEkx7CL9VmloH7GjVS35AQRuLEpN6N7qDR-rCskAAAAATPwVagA'

client = Client('BQBpt34F0skZhBu89RPIrA2zW343oN59cXoGYQID3k9piOnkZpbgMwVMH6Lb9RXgmeZjVXQws39HPeV0Sn6w-_YcgLYhSA6JgcYfGTIYL3vDl_BEB49cWDzrZ4TwopFUSQEn9yeJFqTI5qjesG-A0enbls5m3EYEQlQylLfciq3vb3_IPY3GIaz8heM7Pn-ADkeL9q8-AqwkBO3h9l1KNnY1oz8S6wicd_p5OT9QEnjTAv1ID8oIUk_jxo4REYrdSfix4dV7s66Ud2oyGbQH3ESZgK5Cw8EJeMoLmtqybcRCRIgBfFEkx7CL9VmloH7GjVS35AQRuLEpN6N7qDR-rCskAAAAATPwVagA',api_id = api_id, api_hash = api_hash)





app = PyTgCalls(client)
app.start()
song_name = ''
@bot.on_message(filters.command('start'))
async def start(bot,msg):
    await bot.send_message(msg.chat.id,'Hello')
    randid = bot.rnd_id()
    print(randid)


asyncio.run(bot.run())
idle()