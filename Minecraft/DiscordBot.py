import discord
import time
from discord.ext import commands, tasks
from itertools import cycle
from PIL import Image
import json
import os

status = cycle(['MinecraftChat', 'to Discord'])
# client = commands.Bot(command_prefix = '.')
client = discord.Client(intents=discord.Intents.default())

Data = open("C:\Minecraft\Data.json", "r")
Data = json.load(Data)
Channel = Data["Channel"]


@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready.')
    Clear = open("C:\Minecraft\MinecraftDiscord.json", "w")
    Clear.write("")
    Clear.close()
   


@tasks.loop(seconds = 1)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
    test = open("C:\Minecraft\MinecraftDiscord.json", "r")
    ChatMSGLine = test.readlines()
    test.close()
    L = 0
    while L < len(ChatMSGLine):
        ChatMSG = ChatMSGLine[L]
        print(ChatMSG)
        if ChatMSG == "":
            pass
        else:
            with open("C:\Minecraft\DiscordUser.json", "ab+") as ab:
                ab.close()
                f = open('C:\Minecraft\DiscordUser.json', 'r+')
                f.readline()
                if os.stat("C:\Minecraft\DiscordUser.json").st_size == 0:
                    f.write("{}")
                    f.close()
                else:
                    pass
                with open('C:\Minecraft\DiscordUser.json', 'r') as f:
                    users = json.load(f)
                
            try:
                             
                channel = client.get_channel(int(Channel))
                if ChatMSG[0] == "<":
                    ChatText = ChatMSG[1:].split(">"); 
                    if not f'{ChatText[0]}' in users:
                        users[f'{ChatText[0]}'] = {}
                        users[f'{ChatText[0]}']['DiscordID'] = 0
                        users[f'{ChatText[0]}']['DiscordToken'] = 0
                        users[f'{ChatText[0]}']['MSG'] = 0
                    users[f'{ChatText[0]}']['MSG'] += 1
                    embed = discord.Embed(colour=discord.Colour(0x00ffff))
                    embed.set_author(name=ChatText[0], url="", icon_url="https://th.bing.com/th/id/R.85e8705eea0e57f2af8dca28960daec8?rik=ZUbKvewxi915Mg&pid=ImgRaw&r=0")
                    embed.add_field(name="", value=ChatText[1], inline=False)

                    await channel.send(embed=embed)
                    
                if ChatMSG[1] == "+":
                    ChatText = ChatMSG[3:]
                    if not f'{ChatText}' in users:
                        users[f'{ChatText}'] = {}
                        users[f'{ChatText}']['DiscordID'] = 0
                        users[f'{ChatText}']['DiscordToken'] = 0
                        users[f'{ChatText}']['MSG'] = 0
                    embed = discord.Embed(colour=discord.Colour(0x00ff00))
                    embed.set_author(name=ChatText, url="", icon_url="https://th.bing.com/th/id/R.85e8705eea0e57f2af8dca28960daec8?rik=ZUbKvewxi915Mg&pid=ImgRaw&r=0")
                    embed.add_field(name="", value="Joined The Server", inline=False)
                    await channel.send(embed=embed)
                   
                if ChatMSG[1] == "-":
                    ChatText = ChatMSG[3:]
                    if not f'{ChatText}' in users:
                        users[f'{ChatText}'] = {}
                        users[f'{ChatText}']['DiscordID'] = 0
                        users[f'{ChatText}']['DiscordToken'] = 0
                        users[f'{ChatText}']['MSG'] = 0
                    embed = discord.Embed(colour=discord.Colour(0xff0000))
                    embed.set_author(name=ChatText, url="", icon_url="https://th.bing.com/th/id/R.85e8705eea0e57f2af8dca28960daec8?rik=ZUbKvewxi915Mg&pid=ImgRaw&r=0")
                    embed.add_field(name="", value="Left The Server", inline=False)

                    await channel.send(embed=embed)
                    
                with open('C:\Minecraft\DiscordUser.json', 'w+') as f:
                    json.dump(users, f)
            except:
                pass
        Chat = open("C:\Minecraft\MinecraftDiscord.json", "w+")
        Chat.write("")
        Chat.close()
        L += 1

Token = Data["Token"]
client.run(Token)
