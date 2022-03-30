import asyncio
from collections import deque

from . import ALIVE_NAME, catub, edit_or_reply


from uuid import uuid4

plugin_category = "Queen main"

@catub.cat_cmd(
    pattern="HEART$",
    command=("HEART", plugin_category),
    info={
    "header": "HEART animation",
    "usage": "{tr}HEART",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "HEART")
    await event.edit("❤ Love")
    await asyncio.sleep(0.5)