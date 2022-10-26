
from pstats import Stats
from tkinter import N, dnd
import types
from twitchAPI.twitch import Twitch
from unittest import async_case
from discord.ext import commands
from ctypes.wintypes import MSG
from datetime import date, datetime
from encodings import utf_8
from core.classes import Cog_Extension
from datetime import timedelta,timezone,datetime
import discord,json,asyncio
from urllib.parse import urlparse
from discord import app_commands
with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
tw=((datetime.utcnow().replace(tzinfo=timezone.utc)).astimezone(timezone(timedelta(hours=8)))).strftime("%Y-%m-%d %H:%M:%S")
dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
dt2 = dt1.astimezone(timezone(timedelta(hours=8)))


##取得當前時間
def tw_time():
  dt1=datetime.utcnow().replace(tzinfo=timezone.utc)#取得時間
  dt2 = dt1.astimezone(timezone(timedelta(hours=8)))#轉時區
  tw=dt2.strftime("%Y-%m-%d %H:%M:%S")
  return tw


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


    @commands.command()
    @commands.has_permissions(administrator=True) 
    async def update(self,ctx):
        retStr = str(f"""```css\n{tw_time()}```""")
        retStrupdtae = str(f"""```css\n新增:進伺服器自動給予身分組[成員]```""")
        embed=discord.Embed(title=" ")
        embed.set_author(name="系統", icon_url="https://i.imgur.com/NkoBPr0.gif")
        embed.add_field(name="更新內容", value=retStrupdtae, inline=False)
        embed.add_field(name="時間", value=retStr, inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def party(self,ctx,human):
        #async def self(interation:discord.Integration, ask:str):
        #1.人數
        retStr = str(f"""```css\n{tw_time()}```""")
        embed=discord.Embed(title="分隊系統")
        embed.add_field(name="點擊表情符號建立", value="#️⃣:人數 ✅:確認鍵", inline=False)
        embed.add_field(name="時間", value=retStr, inline=True)
        print(human)
        await ctx.send(embed=embed)
       

async def setup(bot):
    await bot.add_cog(Main(bot))