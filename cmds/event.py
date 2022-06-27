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
        embed=discord.Embed(title=" ", description=f"歡迎加入stora country{n}{member.mention}{n}{retStr}", color=0x5899ee)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_author(name=" 通知", icon_url="https://i.imgur.com/NkoBPr0.gif")
        
        #embed.set_footer(text=f"加入時間:{tw_time()}")
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
        embed=discord.Embed(title=" ", description=f"感謝光顧stora country{n}{member.mention}{n}{retStr}", color=0x5899ee)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_author(name=" 通知", icon_url="https://i.imgur.com/NkoBPr0.gif")
        channel = self.bot.get_channel(721237070458126357)
        await channel.send(embed=embed)
        await mchannel.edit(name=f'目前伺服器人數 : {len(cm)}')
    ##文字紀錄(刪除)
    '''
    邏輯
    1.判斷訊息是誰刪的
    1-1.如果是管理員刪則log會更新(不可行)
    1-2
    '''
    # @commands.Cog.listener()
    # async def on_message_delete(self,msg):
    #     channel=self.bot.get_channel(989792973975871518)
    #     for i in msg.guild.members:#回傳member
    #         for role in i.roles:
    #             if role.permissions.manage_messages==True:
    #                 await channel.send(i)
        
        # async for entry in msg.guild.audit_logs(action=discord.AuditLogAction.message_delete,limit=1,after=datetime.utcnow()):
        #     for i in msg.guild.members:
        #         if entry.user.id==i.id:
        #             for a in i.roles:
        #                 if a.id == 688751396358848518:
        #                     await channel.send('boss')
        
        # for i in msg.guild.members:
        #     if msg.author.id==i.id:
        #         await channel.send(msg.author.name)            # async for entry in msg.guild.audit_logs(action=discord.AuditLogAction.message_delete,limit=1):#找尋第一筆審核日誌
            #     if i.id==entry.user.id:
            #         await channel.send(entry.user.name)


        #await channel.send(allmember)
        # if msg.author.id
        
            # await channel.send(entry)
            # if msg.author.id != entry.user.id:#判斷訊息是否被管理員刪除
            #     if not msg.attachments :#判斷訊息是否為圖片--否
            #         who_delete=f'<@{entry.user.id}>'
            #         await channel.send(embed=msg_delete(msg,who_delete))
            #     elif msg.attachments:#判斷訊息是否為圖片--是
            #         who_delete=f'<@{entry.user.id}>'
            #         embed=msg_delete(msg,who_delete)
            #         await channel.send(embed=embed)

        #     who_delete=f'<@{msg.author.id}>'
        #     await channel.send(embed=msg_delete(msg,who_delete))


            # else:
            #     if not msg.attachments:#判斷訊息是否為圖片--否
            #         who_delete=f'<@{msg.author.id}>'
            #         await channel.send(embed=msg_delete(msg,who_delete))
            #     else:#判斷訊息是否為圖片--是
            #         who_delete=f'<@{msg.author.id}>'
            #         embed=msg_delete(msg,who_delete)
            #         await channel.send(embed=embed)
            # else:
            #     if msg.attachments:
            #         who_delete=msg.author.mention
            #         embed=msg_delete(msg,who_delete)
            #         embed.set_image(url=msg.attachments[0].proxy_url)
            #         await channel.send(embed=embed)
        # else:
        #     embed=msg_delete(msg)
        #     embed.set_image(url="attachment://image.png")
        #     await channel.send(msg.attachments[0])
        #if msg.attachments==False:
            #await channel.send('87')
        #if msg.attachments[0]==True:
        #await channel.send(msg.attachments)
        # 



        # count=1
        # channel=self.bot.get_channel(989792973975871518)
        # async for data in msg.guild.audit_logs(action=discord.AuditLogAction.message_delete):
        #     if count==1:
        #         await channel.send(f'<@{data.user.id}>')
        #         count+=1
       
        # await channel.send(embed=embed)

    # @commands.Cog.listener()
    # async def on_member_update(self,before, after):
    #     if before
    #     print(after.activity)
        #print(before.name)
    # @commands.Cog.listener()
    # async def on_raw_reaction_add(self,data):
    #     global writetp
    #     print(str(r_msg.reactions[0]))
    #     if str(r_msg.reactions[0])=='🎮' :
    #         await r_msg.add_reaction('💻')
    #         await r_msg.add_reaction('🎵')
    #         await r_msg.add_reaction('👁️')
    #     if str(data.emoji)=='🎮' and  data.user_id != self.bot.user.id:
    #         writetp=discord.Game
    #         await r_msg.clear_reaction('👁️')
    #         await r_msg.clear_reaction('🎵')
    #         await r_msg.clear_reaction('💻')
    #         await r_msg.clear_reaction('🎮')
    #     elif str(data.emoji)=='💻' and  data.user_id != self.bot.user.id:
    #         writetp=discord.Streaming
    #         await r_msg.clear_reaction('👁️')
    #         await r_msg.clear_reaction('🎵')
    #         await r_msg.clear_reaction('💻')
    #         await r_msg.clear_reaction('🎮')
    #     elif str(data.emoji)=='🎵' and  data.user_id != self.bot.user.id:
    #         writetp=discord.ActivityType.listening
    #         await r_msg.clear_reaction('👁️')
    #         await r_msg.clear_reaction('🎵')
    #         await r_msg.clear_reaction('💻')
    #         await r_msg.clear_reaction('🎮')
    #     elif str(data.emoji)=='👁️' and  data.user_id != self.bot.user.id:
    #         writetp=discord.ActivityType.watching
    #         await r_msg.clear_reaction('👁️')
    #         await r_msg.clear_reaction('🎵')
    #         await r_msg.clear_reaction('💻')
    #         await r_msg.clear_reaction('🎮')
    @commands.Cog.listener()
    async def on_shard_disconnect(data):
        print(data)

    

    #信息偵測
    @commands.Cog.listener()
    async def on_message(self,msg:discord.Message):
        global r_msg,embed_dict,ame,url
        wl_channel=self.bot.get_channel(int(jdata['nm_channel']))
        testbg=self.bot.get_channel(979555335813615666)
        setchannel=self.bot.get_channel(980860042926505984)
        if '光臨' in msg.content:
            await wl_channel.send(f'目前時間:{tw_time()}')
        elif msg.content=='嗨' and msg.author != self.bot.user:
            await msg.channel.send('嗨')
            # n='\n'
            # retStr = str(f"""```css\n{(tw_time())}```""")
            # embed=discord.Embed(title=" ", description=f"感謝光顧stora country{n}87878{n}{retStr}", color=0x5899ee)
            # embed.set_thumbnail(url=msg.author.avatar_url)
            # embed.add_field(name="key", value=msg.author.display_icon, inline=False)
            # embed.set_author(name=" 通知", icon_url="https://i.imgur.com/NkoBPr0.gif")
            
            #embed.add_field(name="Name field can't be colored as it seems",value=retStr)
            #await msg.channel.send(embed=embed)
        elif msg.content=='hi':
            await msg.channel.send(f'嗨{msg.author.mention}',reference=msg)
            # retStr = str(f"""```css\n{(tw_time())}\n```""")
            # embed=discord.Embed(title="--語音頻道進出紀錄--",colour=0x5899ee)
            # embed.set_author(name="通知", icon_url="https://i.imgur.com/NkoBPr0.gif")
            # embed.add_field(name="時間", value=msg.author.display_name, inline=True)
            # # #embed.set_footer(text=retStr)
            # await msg.channel.send(embed=embed)
        elif msg.raw_mentions==[848798723294232628] and msg.author != self.bot.user and 'i love you' in msg.content:
            await msg.add_reaction('💖')
            await msg.channel.send(f'{msg.author.mention}love you💖')
        elif msg.raw_mentions==[848798723294232628] and msg.author != self.bot.user and 'i hate you' in msg.content:
            await msg.add_reaction('🔪')
            await msg.channel.send(f'{msg.author.mention}hate you🤢')
        else:
            pass

def setup(bot):
    bot.add_cog(Event(bot))