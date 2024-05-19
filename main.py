import discord                                                              #go to discord developer portal to active bot
import random

import os 
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('TOKEN')

from discord.ext import commands                                            #outline



intents = discord.Intents.default()
intents.message_content = True

client  =  commands.Bot(command_prefix = '!', intents=intents)              #bot preflix

@client.event                                                               #if the bot ready or not
async def on_ready():
    print("Bot now ready")
    print("-------------")

@client.command()                                                           #command space
async def ptj_dump(ctx):
    await ctx.send("yeah, i agree")

@client.command()                                                           #write a msg to a channel
async def msg(ctx, channel: discord.TextChannel, *, message):
    await channel.send(message)

@client.command()                                                           #for fun
async def oof(ctx):
    await ctx.send("<a:oof_pat:1082303590347046942>")

@client.command()
async def ptj(ctx):
    await ctx.send("<a:ptj_pat:1082302741352828999>")

@client.command()
async def speczy(ctx):
    await ctx.send("<a:gigachad:1241292798595170346>")

@client.command()                                                           #spin systems
async def spin(ctx):
    i = random.randint(1, 100)
    if i <= 15:
        await ctx.send("You spun some shit uncommon item")
    elif 16 <= i <= 30:
        await ctx.send("You got some trash rare item")
    elif 31 <= i <= 45:
        await ctx.send("You spun some useless epic item")
    elif 46 <= i <= 60:
        await ctx.send("You just wasted your time for stupid legendary item")
    elif 61 <= i <= 80:
        await ctx.send("Congrats on a random relic item")
    elif 81 <= i <= 90:
        await ctx.send("Congrats you spun out a contraband ")
    else:
        unobtainable_item = [" Frostbite", " Fagdfaust IV", " Coroller", " Vertigo", " RGB", " Disintegrator", " Anti-matter", " Exotic", " Scouts Honor", " Moonfeather", " Ghostie", " Eternal Frost", " Keeper Of The Deep", " Flying Dutchman", " Assault Drone", " Deep Space", " Mysterious Orb", " Bruisegg", " ZENITH", " Esper", " Forbidden Tome", " ESPER", " Attack Drone", " DOS Armour", " DOS", " DOS Walker", " DOS Belt", " Devourer Of Souls"]
        await ctx.send("Congrats you hit the bingo, you spun out:" + random.choice(unobtainable_item))




client.run(token)
#authorize: https://discord.com/oauth2/authorize?client_id=1240319216930918511&permissions=581652796549239&scope=bot