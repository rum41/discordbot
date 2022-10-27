import asyncio
from asyncio import tasks
from contextlib import asynccontextmanager
from fileinput import filename
from lib2to3.pgen2.token import ASYNC
from discord.ext import commands
from ctypes.wintypes import MSG
from datetime import datetime
from encodings import utf_8
import discord,json,os,asyncio
import traceback,os
import logging,string,tkinter
import tkinter as tk



with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents=discord.Intents.all()
bot = commands.Bot(command_prefix= '[',intents=intents)


@bot.event
async def on_ready():
    channel=bot.get_channel(989182594409197618)
    await channel.send('bot is online')
    fawrite=discord.ActivityType.watching
    name='87'
    await bot.change_presence(activity=discord.Activity(type=fawrite,name=name))
    for filename in os.listdir('./cmds'):
        if filename.endswith(".py"):
            await bot.load_extension(f'cmds.{filename[:-3]}')
    print("Bot is ready")



root = tk.Tk()
root.title('my window')
root.geometry('200x150')





root.mainloop()
@bot.command(brief='載入檔案')
async def load(ctx, extension):
    def button_event():
        bot.load_extension(f'cmds.{extension}')
    
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'載入{extension} 完成!')
    mybutton = tk.Button(root, text='button', command=button_event)
    mybutton.pack()
@bot.command(brief='卸下檔案')
async def unload(ctx,extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'卸下{extension} 完成!')

@bot.command(brief='重新載入檔案')
async def reload(ctx,extension):
    bot.reload_extension(F'cmds.{extension}')
    await ctx.send(f'重新載入{extension} 完成!')

# for filename in os.listdir('./cmds'):
#     if filename.endswith('.py'):
#         bot.load_extension(F'cmds.{filename[:-3]}')
if __name__ == '__main__':
    bot.run(jdata['TOKEN'])