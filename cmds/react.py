from discord.ext import commands
from ctypes.wintypes import MSG
from datetime import datetime
from encodings import utf_8
from core.classes import Cog_Extension
import discord,json
with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class React(Cog_Extension):
    
    @commands.command()
    async def pic(self, ctx):
        pic=discord.File(jdata['pic'])
        await ctx.send(file=pic)

def setup(bot):
    bot.add_cog(React(bot))