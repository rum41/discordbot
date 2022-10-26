from unittest import async_case
from discord.ext import commands
from ctypes.wintypes import MSG
from datetime import datetime
from encodings import utf_8
from core.classes import Cog_Extension
import discord,json,asyncio

class Task(Cog_Extension):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)


async def setup(bot):
    await bot.add_cog(Task(bot))