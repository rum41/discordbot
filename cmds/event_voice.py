import json,discord,time
from operator import truediv
from datetime import datetime
from discord.ext import commands
from core.classes import Cog_Extension
from datetime import tzinfo, timedelta,timezone,datetime

with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)



##取得當前時間
def tw_time():
  dt1=datetime.utcnow().replace(tzinfo=timezone.utc)#取得時間
  dt2 = dt1.astimezone(timezone(timedelta(hours=8)))#轉時區
  tw=dt2.strftime("%Y-%m-%d %H:%M:%S")
  return tw



##語音紀錄嵌入
def in_on(member_name,channel,status):
    retStr = str(f"""```css\n{tw_time()}```""")
    embed=discord.Embed(title="----語音頻道進出紀錄----",color=0xb1c5f8)
    embed.set_author(name="通知", icon_url="https://i.imgur.com/NkoBPr0.gif")
    embed.add_field(name="成員暱稱", value=member_name, inline=True)
    embed.add_field(name="頻道", value=channel, inline=True)
    embed.add_field(name="狀態", value=status, inline=True)
    embed.add_field(name="時間", value=retStr, inline=True)
    return embed

class Event_voice(Cog_Extension):
    ##語音頻道進出偵測
    @commands.Cog.listener()
    async def on_voice_state_update(self,member,before,after):
        bg=self.bot.get_channel(981767398698926160)
        logs=self.bot.get_channel(989792973975871518)
        if before.channel ==None :#成員先前均無進入頻道
            member_name=member.display_name
            channel=after.channel
            status=jdata['join_emoji']
            await bg.send(embed=in_on(member_name,channel,status))

        elif after.channel==None:#成員離開頻道後均無進入頻道
            member_name=member.display_name
            channel=before.channel
            status=jdata['leave_emoji']
            await bg.send(embed=in_on(member_name,channel,status))

        elif before.channel !=after.channel:#成員先前進入頻道
            member_name=member.display_name
            channel=before.channel
            status=jdata['leave_emoji']
            await bg.send(embed=in_on(member_name,channel,status))
            member_name=member.display_name
            channel=after.channel
            status=jdata['join_emoji']
            await bg.send(embed=in_on(member_name,channel,status))

        elif member.voice.mute == True:
            async for entry in member.guild.audit_logs(action=discord.AuditLogAction.member_update,limit=1):
                entry=entry
            retStr = str(f"""```css\n{tw_time()}```""")
            embed=discord.Embed(title="---------語音紀錄---------",color=0xb1c5f8)
            embed.set_author(name="通知", icon_url="https://i.imgur.com/NkoBPr0.gif")
            embed.add_field(name="成員暱稱", value=member.display_name, inline=False)
            embed.add_field(name="操作者", value=entry.user.name, inline=False)
            embed.add_field(name="頻道", value=after.channel, inline=True)
            embed.add_field(name="狀態", value=jdata['mute'], inline=True  )
            embed.add_field(name="時間", value=retStr, inline=False)
            await logs.send(embed=embed)

        elif member.voice.mute == False and before.mute== True:
            async for entry in member.guild.audit_logs(action=discord.AuditLogAction.member_update,limit=1):
                entry=entry
            retStr = str(f"""```css\n{tw_time()}```""")
            embed=discord.Embed(title="----管理員語音靜音紀錄----",color=0xb1c5f8)
            embed.set_author(name="通知", icon_url="https://i.imgur.com/NkoBPr0.gif")
            embed.add_field(name="成員暱稱", value=member.display_name, inline=False)
            embed.add_field(name="操作者", value=entry.user.name, inline=False)
            embed.add_field(name="頻道", value=after.channel, inline=True)            
            embed.add_field(name="狀態", value=jdata['unmute'], inline=True)
            embed.add_field(name="時間", value=retStr, inline=False)
            await logs.send(embed=embed)
        elif member.voice.deaf == True:
            async for entry in member.guild.audit_logs(action=discord.AuditLogAction.member_update,limit=1):
                entry=entry
            retStr = str(f"""```css\n{tw_time()}```""")
            embed=discord.Embed(title="---------管理員語音拒聽紀錄---------",color=0xb1c5f8)
            embed.set_author(name="通知", icon_url="https://i.imgur.com/NkoBPr0.gif")
            embed.add_field(name="成員暱稱", value=member.display_name, inline=False)
            embed.add_field(name="操作者", value=entry.user.name, inline=False)
            embed.add_field(name="頻道", value=after.channel, inline=True)
            embed.add_field(name="狀態", value=jdata['mute'], inline=True  )
            embed.add_field(name="時間", value=retStr, inline=False)
            await logs.send(embed=embed)
        elif member.voice.deaf == False and before.deaf==True:
            async for entry in member.guild.audit_logs(action=discord.AuditLogAction.member_update,limit=1):
                entry=entry
            retStr = str(f"""```css\n{tw_time()}```""")
            embed=discord.Embed(title="---------管理員語音拒聽紀錄---------",color=0xb1c5f8)
            embed.set_author(name="通知", icon_url="https://i.imgur.com/NkoBPr0.gif")
            embed.add_field(name="成員暱稱", value=member.display_name, inline=False)
            embed.add_field(name="操作者", value=entry.user.name, inline=False)
            embed.add_field(name="頻道", value=after.channel, inline=True)
            embed.add_field(name="狀態", value=jdata['unmute'], inline=True  )
            embed.add_field(name="時間", value=retStr, inline=False)
            await logs.send(embed=embed)


        else:
            pass


def setup(bot):
    bot.add_cog(Event_voice(bot))