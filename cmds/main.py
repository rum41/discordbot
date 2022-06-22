
from pstats import Stats
from tkinter import N, dnd
import types
from unittest import async_case
from discord.ext import commands
from ctypes.wintypes import MSG
from datetime import date, datetime
from encodings import utf_8
from core.classes import Cog_Extension
from datetime import timedelta,timezone,datetime
import discord,json,asyncio
from urllib.parse import urlparse
with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
tw=((datetime.utcnow().replace(tzinfo=timezone.utc)).astimezone(timezone(timedelta(hours=8)))).strftime("%Y-%m-%d %H:%M:%S")
dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
dt2 = dt1.astimezone(timezone(timedelta(hours=8)))
class Main(Cog_Extension):


    @commands.command(brief='取得當前延遲', description='使用此指令即可得知當前延遲')
    async def ping(self,ctx):
        print(f'{round(self.bot.latency*1000)} (ms)')
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')
    @commands.command(brief='訊息複誦',description='複誦使用者信息')
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)
    @commands.command(brief='清除訊息',description='清除訊息')
    async def clean(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)
    @commands.command(brief='更改bot狀態',description='更改bot活動')
    async def set(self,ctx):
        nel='\n'
        global edit_msg
        embed=discord.Embed(title="更改Bot狀態")
        embed.add_field(name="說明", value=f"活動狀態與狀態皆使用點擊表情符號來設定{nel} {nel}活動名稱與網址請依個人喜好依序在訊息欄填入{nel} ", inline=False)
        embed.add_field(name="活動狀態", value=f'🎮 遊戲{nel}💻 直播{nel}🎵  聆聽{nel}👁️  觀看', inline=True)
        embed.add_field(name="狀態", value=f"🟢線上{nel}🔴離線{nel}🌙閒置{nel}⛔請勿打擾{nel}:ghost:隱身", inline=True)
        embed.add_field(name="活動名稱", value="尚未填入", inline=False)
        embed.add_field(name="網址", value="尚未填入", inline=True)
        edit_msg=await ctx.send(embed=embed)
    @commands.command()
    async def test(self,ctx):
        message = await ctx.send("hello")
        await asyncio.sleep(1)
        await message.edit(content="newcontent")




def setup(bot):
    bot.add_cog(Main(bot))