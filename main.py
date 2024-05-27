import discord                                                              #go to discord developer portal to active bot
import random
import json
import os

from discord.ui import Button, View
from dotenv import load_dotenv                                              #token for .env file

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

async def open_account(user):                                               #bank system
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["KR"] = 0
    
    with open("bank.json",'w') as f:                                        #json file for database
        json.dump(users, f)
    return True

async def get_bank_data():
    with open("bank.json",'r') as f:
        users = json.load(f)
    return users

async def update_bank(user, change = 0, mode = "KR"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("bank.jason", 'w') as f:
        json.dump(users,f)

    bal = users[str(user.id)]["KR"]
    return bal

@client.command()                                                           #make and check bank mine of other account
async def balance(ctx, mention: discord.Member = None):
    if mention != None:
        await open_account(mention)

        users = await get_bank_data()

        wallet_amt = users[str(mention.id)]["KR"]
    
        em = discord.Embed(title = f"{mention}'s balance", color = discord.Color.red())
        em.add_field(name= "KR", value = wallet_amt)
        await ctx.send(embed = em)
    else:
        await open_account(ctx.author)
        user = ctx.author

        users = await get_bank_data()

        wallet_amt = users[str(user.id)]["KR"]
    
        em = discord.Embed(title = f"{ctx.author.name}'s balance", color = discord.Color.red())
        em.add_field(name= "KR", value = wallet_amt)
        await ctx.send(embed = em)

@client.command()                                                           #work earn 500 - 1000
@commands.cooldown(1, 10*60, commands.BucketType.user)
async def work(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()

    user = ctx.author

    earnings = random.randint(500, 1000)

    await ctx.send(f"You work hard and earn: {earnings} KR")

    users[str(user.id)]["KR"] += earnings
    with open("bank.json",'w') as f:
        json.dump(users,f)

@client.command()                                                           #beg earn 0 - 500
@commands.cooldown(1, 15, commands.BucketType.user)
async def beg(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()

    user = ctx.author

    i = random.randint(1, 1000)

    if i == 1:
        earnings = random.randint(151, 500)

        await ctx.send(f"Rain of KR and you recive: {earnings} KR")

        users[str(user.id)]["KR"] += earnings
        with open("bank.json",'w') as f:
            json.dump(users,f)
    elif 2 <= i <= 50:
        earnings = random.randint(101, 150)

        await ctx.send(f"A generous person give you: {earnings} KR")

        users[str(user.id)]["KR"] += earnings
        with open("bank.json",'w') as f:
            json.dump(users,f)
    elif 51 <= i <= 150:
        earnings = random.randint(51, 100)

        await ctx.send(f"Since you are praying all day so somebody give you: {earnings} KR")

        users[str(user.id)]["KR"] += earnings
        with open("bank.json",'w') as f:
            json.dump(users,f)
    elif 151 <= i <= 350:
        earnings = random.randint(31, 50)

        await ctx.send(f"Someone think you homeless and give you: {earnings} KR")

        users[str(user.id)]["KR"] += earnings
        with open("bank.json",'w') as f:
            json.dump(users,f)
    elif 351 <= i <= 800:
        earnings = random.randint(20, 30)

        await ctx.send(f"You suck but still somebody give you: {earnings} KR")

        users[str(user.id)]["KR"] += earnings
        with open("bank.json",'w') as f:
            json.dump(users,f)
    else:
        await ctx.send(f"You are so suck that nobody want to give you a shit!")

@client.command()                                                           #search earn 0 - 500
@commands.cooldown(1, 15, commands.BucketType.user)
async def search(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()

    user = ctx.author

    i = random.randint(1, 1000)

    if i == 1:
        earnings = random.randint(151, 500)

        await ctx.send(f"You found a godden nugget and sold for: {earnings} KR")

        users[str(user.id)]["KR"] += earnings
        with open("bank.json",'w') as f:
            json.dump(users,f)
    elif 2 <= i <= 50:
        earnings = random.randint(101, 150)

        await ctx.send(f"You found a wallet and nobody near here, so you earn: {earnings} KR")

        users[str(user.id)]["KR"] += earnings
        with open("bank.json",'w') as f:
            json.dump(users,f)
    elif 51 <= i <= 150:
        earnings = random.randint(51, 100)

        await ctx.send(f"You found some sliver and sell for: {earnings} KR")

        users[str(user.id)]["KR"] += earnings
        with open("bank.json",'w') as f:
            json.dump(users,f)
    elif 151 <= i <= 350:
        earnings = random.randint(31, 50)

        await ctx.send(f"You found some KR that somebody threw away: {earnings} KR")

        users[str(user.id)]["KR"] += earnings
        with open("bank.json",'w') as f:
            json.dump(users,f)
    elif 351 <= i <= 800:
        earnings = random.randint(20, 30)

        await ctx.send(f"You found some trash but still can make some KR from those: {earnings} KR")

        users[str(user.id)]["KR"] += earnings
        with open("bank.json",'w') as f:
            json.dump(users,f)
    else:
        await ctx.send(f"You search hard but still found nothing, haha skill issues <:LMAO:945539956066115594> !!")

@client.command()                                                           #spin systems
async def spin(ctx):
    await open_account(ctx.author)

    bal = await update_bank(ctx.author)
    
    if 500 > bal:
        await ctx.send("You don't have enough KR !!")
    else:
        users = await get_bank_data()

        user = ctx.author
        
        users[str(user.id)]["KR"] += -500
        with open("bank.json",'w') as f:
            json.dump(users,f)

        i = random.randint(1, 10000)
        if i == 1:
            await ctx.send("<a:spin:1243478409930080342> Congratulation, you won the jackpot prize: a basic nitro ticket")
        elif 2 <= i <= 10:
            unobtainable_item = [" Frostbite", " Fagdfaust IV", " Coroller", " Vertigo", " RGB", " Disintegrator", " Anti-matter", " Exotic", " Scouts Honor", " Moonfeather", " Ghostie", " Eternal Frost", " Keeper Of The Deep", " Flying Dutchman", " Assault Drone", " Deep Space", " Mysterious Orb", " Bruisegg", " ZENITH", " Esper", " Forbidden Tome", " ESPER", " Attack Drone", " DOS Armour", " DOS", " DOS Walker", " DOS Belt", " Devourer Of Souls"]
            await ctx.send("<a:spin:1243478409930080342> Congrats you hit the bingo, you spun out:" + random.choice(unobtainable_item))
        elif 11 <= i <= 60:
            await ctx.send("<a:spin:1243478409930080342> Congrats you spun out a contraband ")
        elif 61 <= i <= 300:
            await ctx.send("<a:spin:1243478409930080342> Congrats on a random relic item")
        elif 301 <= i <= 1700:
            await ctx.send("<a:spin:1243478409930080342> You just wasted your time for a stupid legendary item")
        elif 1701 <= i <= 5200:
            await ctx.send("<a:spin:1243478409930080342> You spun some useless epic item")
        else:
            await ctx.send("<a:spin:1243478409930080342> You got some trash rare item")

@client.command()
async def chances(ctx):

    button1 = Button(label= "work", style= discord.ButtonStyle.primary)
    button2 = Button(label= "beg / search", style= discord.ButtonStyle.primary)
    button3 = Button(label= "spin", style= discord.ButtonStyle.primary)
    button4 = Button(label="↩", style= discord.ButtonStyle.primary)
    async def button_callback(interaction):
        em = discord.Embed(title = f"Work chance:", color = discord.Color.red())
        em.add_field(name= "Random", value="500 - 1500")
        view = View()
        view.add_item(button4)
        await interaction.response.edit_message(embed = em, view = view)
    button1.callback = button_callback

    async def button_callback(interaction):
        em = discord.Embed(title = f"Beg / search chance:", color = discord.Color.red())
        em.add_field(name= "0 kr", value="20%")
        em.add_field(name= "20 - 30 kr", value="45%")
        em.add_field(name= "31 - 50 kr", value="20%")
        em.add_field(name= "51 - 100 kr", value="10%")
        em.add_field(name= "101 - 150 kr", value="4,9%")
        em.add_field(name= "151 - 500 kr", value="0,1%")
        view = View()
        view.add_item(button4)
        await interaction.response.edit_message(embed = em, view = view)
    button2.callback = button_callback

    async def button_callback(interaction):
        em = discord.Embed(title = f"Spin chance:", color = discord.Color.red())
        em.add_field(name= "Rare item", value="48%")
        em.add_field(name= "Epic item", value="35%")
        em.add_field(name= "Legendary item", value="14%")
        em.add_field(name= "Relic item", value="2,4%")
        em.add_field(name= "Contraband item", value="0,5%")
        em.add_field(name= "Unobtainable item", value="0,09%")
        em.add_field(name= "Nitro Basic ticket", value="0,01%")
        view = View()
        view.add_item(button4)
        await interaction.response.edit_message(embed = em, view = view)
    button3.callback = button_callback

    async def button_callback(interaction):
        view = View()
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)
        em = discord.Embed(title = f"Check the chance of these commands:", color = discord.Color.red())
        await interaction.response.edit_message(embed = em, view = view)
    button4.callback = button_callback

    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    em = discord.Embed(title = f"Check the chance of these commands:", color = discord.Color.red())
    await ctx.send(embed = em, view = view)

@client.event
async def on_command_error(ctx, err):
    if err.__class__ is commands.CommandOnCooldown:
        cd: int = int(err.retry_after)
        # send an error message, you can customize this
        await ctx.send(f'The command is on cooldown, time left: **{cd//86400}d {(cd//3600)%24}h {(cd//60)%60}m {cd % 60}s**.')
        return


client.run(token)
#authorize: https://discord.com/oauth2/authorize?client_id=1240319216930918511&permissions=581652796549239&scope=bot
