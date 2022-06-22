from discord.ext import commands
from ctypes.wintypes import MSG
from datetime import datetime
from encodings import utf_8
import discord,json

class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot=bot