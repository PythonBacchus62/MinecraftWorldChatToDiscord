import discord
import time
from discord.ext import commands, tasks
from itertools import cycle
import json

status = cycle(['MinecraftBot', 'MinecraftServer'])
# client = commands.Bot(command_prefix = '.')
client = discord.Client(intents=discord.Intents.default())

Data = open("C:\Minecraft\Data.json", "r")
Data = json.load(Data)
Channel = Data["Channel"]


@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready.')
   



@tasks.loop(seconds = 1)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
    test = open("C:\Minecraft\MinecraftDiscord.json", "r")
    ChatMSG = test.read()
    test.close()
    if ChatMSG == "":
        pass
    else:
        print(ChatMSG)
        channel = client.get_channel(int(Channel))
        if ChatMSG[0] == "<":
            ChatText = ChatMSG[1:].split(">");  
            #print "Name: " + spalten[2];
            embed = discord.Embed(title="User: "+ChatText[0], colour=discord.Colour(0x3e038c))

            embed.add_field(name=f" ", value=ChatText[1], inline=False)

            await channel.send(embed=embed)
            pass
        if ChatMSG[1] == "+":
            ChatText = ChatMSG[3:] 
            embed = discord.Embed(title="User: "+ChatText, colour=discord.Colour(0x2ecc71))

            embed.add_field(name=f" ", value="Joined The Server", inline=False)

            await channel.send(embed=embed)
            pass
        if ChatMSG[1] == "-":
            ChatText = ChatMSG[3:]
            embed = discord.Embed(title="User: "+ChatText, colour=discord.Colour(0xe74c3c))

            embed.add_field(name=f" ", value="Left The Server", inline=False)

            await channel.send(embed=embed)
            pass
            pass
        # channel = client.get_channel(int(Channel))
        # await channel.send(ChatMSG)
        Chat = open("C:\Minecraft\MinecraftDiscord.json", "w+")
        Chat.write("")
        Chat.close()
    

    # test_read = open("C:\Minecraft\MinecraftDiscord.json", "w+")
    # list_of_lines1 = test_read.readlines()

    # L = 0

    
    # while L < len(list_of_lines1):
    #     if L > 0:
    #         time.sleep(1)
    #     else:
    #         print(str(list_of_lines1[L].replace("\n","")))
    #         test_read.write()


    #     L += 1

    # test_read.close()


Token = Data["Token"]
client.run(Token)
