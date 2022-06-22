from ast import While
from audioop import add
from cgi import test
from email import message
from fileinput import filename
from sqlite3 import Timestamp
from turtle import goto, title
from unicodedata import name
from discord.ext import commands
from ctypes.wintypes import MSG
from encodings import utf_8

from core.classes import Cog_Extension
import discord,json,os,time
import datetime
from datetime import tzinfo, timedelta,timezone,datetime
with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

def tw_time():
  dt1=datetime.utcnow().replace(tzinfo=timezone.utc)#取得時間
  dt2 = dt1.astimezone(timezone(timedelta(hours=8)))#轉時區
  tw=dt2.strftime("%Y-%m-%d %H:%M:%S")
  return tw

class Event(Cog_Extension):
    
    # async def interval(self):
    #     await self.bot.wait_for('on_raw_reaction_remove')
    #     print('test')

    @commands.Cog.listener()
    async def on_member_join(self,member):
        #######取得伺服器人數#######
        guild=self.bot.get_guild(688748599437164579)
        mchannel=self.bot.get_channel(989115704664027136)
        cm=[]
        for member in guild.members:
            if member.bot == False:
                cm.append(member)
        ###########################
        n='\n'
        retStr = str(f"""```css\n{tw_time()}```""")
        embed=discord.Embed(title=" ", description=f"歡迎加入stora country{n}{member.mention}{n}{retStr}", color=0x5899ee)
        embed.set_author(name=" 通知", icon_url="https://i.imgur.com/NkoBPr0.gif")
        #embed.set_footer(text=f"加入時間:{tw_time()}")
        channel = self.bot.get_channel(721237070458126357)
        await channel.send(embed=embed)
        await mchannel.edit(name=f'目前伺服器人數 : {len(cm)}')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        #######取得伺服器人數#######
        guild=self.bot.get_guild(688748599437164579)
        mchannel=self.bot.get_channel(989115704664027136)
        cm=[]
        for member in guild.members:
            if member.bot == False:
                cm.append(member)
        ###########################
        n='\n'
        retStr = str(f"""```css\n{tw_time()}```""")
        embed=discord.Embed(title=" ", description=f"感謝光顧stora country{n}{member.mention}{n}{retStr}", color=0x5899ee)
        embed.set_author(name=" 通知", icon_url="https://i.imgur.com/NkoBPr0.gif")
        #embed.set_footer(text=f"加入時間:{tw_time()}")
        channel = self.bot.get_channel(721237070458126357)
        await channel.send(embed=embed)
        await mchannel.edit(name=f'目前伺服器人數 : {len(cm)}')
    
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
    async def on_voice_state_update(self,member,before,after):
        space='  '
        bg=self.bot.get_channel(981767398698926160)
        if before.channel ==None :#成員先前均無進入頻道
            await bg.send(f':exclamation:**{member.name}**{space}:regional_indicator_j::regional_indicator_o::regional_indicator_i::regional_indicator_n:{space}**{after.channel}**')
        elif after.channel==None:#成員離開頻道後均無進入頻道
            await bg.send(f':exclamation:**{member.name}**{space}:regional_indicator_l::regional_indicator_e::regional_indicator_f::regional_indicator_t:{space}**{before.channel}**')
        elif before.channel !=after.channel:#成員先前進入頻道
            await bg.send(f':exclamation:**{member.name}**{space}:regional_indicator_l::regional_indicator_e::regional_indicator_f::regional_indicator_t:{space}**{before.channel}**')
            await bg.send(f':exclamation:**{member.name}**{space}:regional_indicator_j::regional_indicator_o::regional_indicator_i::regional_indicator_n:{space}**{after.channel}**')
        #elif after.self_mute==True:


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
            # embed.set_author(name=" 通知", icon_url="https://i.imgur.com/NkoBPr0.gif")
            
            # #embed.add_field(name="Name field can't be colored as it seems",value=retStr)
            # await msg.channel.send(embed=embed)
        elif msg.content=='hi':
            await msg.channel.send(f'嗨{msg.author.mention}',reference=msg)
        # elif msg.author.mention and msg.author != self.bot.user:
        #     n='/n'
        #     rein=str("""```css\n你之前說的內嵌```""")
        #     embed=discord.Embed(title=" ", description=f'{rein}', color=0x5899ee)
        #     embed.set_author(name=" 通知", icon_url="https://i.imgur.com/NkoBPr0.gif")
        #     await msg.channel.send(embed=embed)
        elif msg.raw_mentions==[848798723294232628] and msg.author != self.bot.user and 'i love you' in msg.content:
            await msg.add_reaction('💖')
            await msg.channel.send(f'{msg.author.mention}love you💖')
        elif msg.raw_mentions==[848798723294232628] and msg.author != self.bot.user and 'i hate you' in msg.content:
            await msg.add_reaction('🔪')
            await msg.channel.send(f'{msg.author.mention}hate you🤢')

        else:
            pass
        if msg.embeds:
            embed = msg.embeds[0]
            embed_d = embed.to_dict()
            if embed_d['title']=='更改Bot狀態':
                r_msg=msg
                embed_dict = embed_d
                await testbg.send(embed_dict)
                await msg.add_reaction('🎮')
        # if msg.content.startswith('https')==True and msg.author != self.bot.user and setchannel==msg.channel :
        #     url=msg.content
        #     if embed_dict['title']=='更改Bot狀態':
        #         #await testbg.send(embed_dict)
        #         if embed_dict['fields'][3]['value']=='尚未填入' and embed_dict['fields'][4]['value']=='尚未填入' or embed_dict['fields'][3]['value']!='尚未填入' and embed_dict['fields'][4]['value']=='尚未填入':
        #             url=url
        #             embed_dict['fields'][4]['value']=url
        #             await r_msg.edit(embed=discord.Embed.from_dict(embed_dict))
        #             await msg.delete()
        #             await msg.channel.send('網址設定成功')
        #             if writetp==discord.Streaming:
        #                 await 
                    
                    
        # elif msg.content and msg.author != self.bot.user and setchannel==msg.channel:
        #     ame=msg.content
        #     if embed_dict['title']=='更改Bot狀態':
        #         if embed_dict['fields'][3]['value']=='尚未填入' and embed_dict['fields'][4]['value']=='尚未填入' or embed_dict['fields'][3]['value']=='尚未填入' and embed_dict['fields'][4]['value']!='尚未填入' :
        #             ame=ame
        #             embed_dict['fields'][3]['value']=ame
        #             await r_msg.edit(embed=discord.Embed.from_dict(embed_dict))
        #             await msg.delete()
        #             await msg.channel.send('活動名稱設定成功')
        #             await self.bot.change_presence(activity=)

def setup(bot):
    bot.add_cog(Event(bot))