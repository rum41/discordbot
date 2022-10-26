from ast import While
from audioop import add
from cgi import test
from email import message
from fileinput import filename
from imghdr import what
from operator import truediv
from pickle import FALSE
from pydoc import describe
from sqlite3 import Timestamp
from turtle import goto, title
from unicodedata import name
from discord.ext import commands
from ctypes.wintypes import MSG
from encodings import utf_8
import traceback
from core.classes import Cog_Extension
import discord,json,os,time
import datetime
from datetime import tzinfo, timedelta,timezone,datetime
with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
    
##取得當前時間
def tw_time():
  dt1=datetime.utcnow().replace(tzinfo=timezone.utc)#取得時間
  dt2 = dt1.astimezone(timezone(timedelta(hours=8)))#轉時區
  tw=dt2.strftime("%Y-%m-%d %H:%M:%S")
  return tw


##文字記錄(刪除)鉛入
def msg_delete(msg,who_delete,what_msg=None):
    space=' '
    retStr = str(f"""```css\n{tw_time()}```""")
    if msg.attachments:
        embed=discord.Embed(title="----圖片刪除紀錄----", color=0xff94c9)
        embed.set_author(name="通知", icon_url="https://i.imgur.com/NkoBPr0.gif")
        embed.add_field(name="頻道", value=f'<#{msg.channel.id}>', inline=True)
        embed.add_field(name="訊息作者", value=msg.author.mention, inline=True)
        embed.add_field(name="誰刪除訊息", value=who_delete, inline=True)
        embed.set_image(url=msg.attachments[0])
        embed.add_field(name="時間", value=retStr, inline=False)
        embed.add_field(name="圖片", value=msg.attachments[0].url, inline=False)
    else:
        what_msg=msg.content
        embed=discord.Embed(title="----文字刪除紀錄----", color=0xff94c9)
        embed.set_author(name="通知", icon_url="https://i.imgur.com/NkoBPr0.gif")
        embed.add_field(name="頻道", value=f'<#{msg.channel.id}>', inline=True)
        embed.add_field(name="訊息作者", value=msg.author.mention, inline=True)
        embed.add_field(name="誰刪除訊息", value=who_delete, inline=True)
        embed.add_field(name="原始訊息", value=what_msg, inline=False)
        embed.add_field(name="時間", value=retStr, inline=False)
    return embed
    #await bg.send(embed=embed)

class Event(Cog_Extension):
     
    #指令發生錯誤處理
    @commands.Cog.listener()
    async def on_command_error(ctx,exception):
        #if isinstance()
        await ctx.send(exception)
    
    ##成員加入伺服器    
    @commands.Cog.listener()
    async def on_member_join(self,member):
        # if member.avatar == None:
        #     print(member.display_avatar.url)

        
        #######取得伺服器人數#######
        guild=self.bot.get_guild(688748599437164579)
        role=guild.get_role(737679565538984016)
        await member.add_roles(role)
        mchannel=self.bot.get_channel(989115704664027136)
        cm=[]
        for cmember in guild.members:
            if cmember.bot == False:
                cm.append(cmember)
        
        ###########################
        n='\n'
        now_time = str(f"""```css\n{tw_time()}```""")
        embed=discord.Embed(title=" ", description=f"歡迎加入stora country{n}{member.mention}{n}{now_time}", color=0x5899ee)
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_author(name=" 通知", icon_url="https://i.imgur.com/NkoBPr0.gif")
        channel = self.bot.get_channel(721237070458126357)
        await channel.send(embed=embed)
        await mchannel.edit(name=f'目前伺服器人數 : {len(cm)}')
    
    ##成員離開伺服器 
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        
        #######取得伺服器人數#######
        guild=self.bot.get_guild(688748599437164579)
        mchannel=self.bot.get_channel(989115704664027136)
        cm=[]
        for cmember in guild.members:
            if cmember.bot == False:
                cm.append(cmember)
        
        ###########################
        n='\n'
        retStr = str(f"""```css\n{tw_time()}```""")
        embed=discord.Embed(title=" ", description=f"感謝光顧stora country {member.mention} {retStr}", color=0x5899ee)
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_author(name=" 通知", icon_url="https://i.imgur.com/NkoBPr0.gif")
        channel = self.bot.get_channel(721237070458126357)
        await channel.send(embed=embed)
        await mchannel.edit(name=f'目前伺服器人數 : {len(cm)}')
    

    #信息偵測
    @commands.Cog.listener()
    async def on_message(self,msg:discord.Message):
        wl_channel=self.bot.get_channel(int(jdata['nm_channel']))
        if '光臨' in msg.content:
            await wl_channel.send(f'目前時間:{tw_time()}')
        elif msg.content=='嗨' and msg.author != self.bot.user:
            await msg.channel.send('嗨')
        else:
            pass
        if msg.embeds:
            if "分隊系統" == msg.embeds[0].title:
                await msg.add_reaction('#️⃣')
                await msg.add_reaction('✅')
                

async def setup(bot):
    await bot.add_cog(Event(bot))