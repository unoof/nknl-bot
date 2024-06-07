import discord                                                              #go to discord developer portal to active bot
import random
import json
import os

from discord.ui import Button, View
from dotenv import load_dotenv                                              #token for .env file

load_dotenv()

token = os.getenv('TOKEN')

from discord.ext import commands                                            #outline



intents = discord.Intents.all()
intents.message_content = True

client  =  commands.Bot(command_prefix = '!', intents=intents, help_command= None)              #bot preflix

@client.event                                                               #if the bot ready or not
async def on_ready():
    print("Bot now ready")
    print("-------------")

@client.command()                                                           #command space
async def ptj_dumb(ctx):
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

@client.command()
@commands.cooldown(1, 5*60, commands.BucketType.user)
async def penis(ctx):
    await ctx.send("https://tenor.com/view/penis-haha-gif-18597041")

async def open_warn(user):
    users = await get_warns()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["warns"] = 0
    
    with open("warning.json",'w') as f:                                        #json file for database
        json.dump(users, f)
    return True

async def get_warns():
    with open("warning.json",'r') as f:
        users = json.load(f)
    return users

async def update_warns(user, change = 0, mode = "warns"):
    users = await get_warns()

    users[str(user.id)][mode] += change

    with open("warning.json", 'w') as f:
        json.dump(users,f)

    warns = users[str(user.id)]["warns"]
    return warns

@client.command()                                                           #make and check bank account
async def warning(ctx, mention: discord.Member = None):
    if mention != None:
        await open_warn(mention)

        users = await get_warns()

        wallet_amt = users[str(mention.id)]["warns"]

        if wallet_amt == 0:
            await ctx.send(f"{mention} have no warn yet, you should get some for fun bro.")
        else:
            em = discord.Embed(title = f"{mention}'s total warns:", color = discord.Color.red())
            em.add_field(name= "Warns", value = wallet_amt)
            await ctx.send(embed = em)
    else:
        await open_warn(ctx.author)

        user = ctx.author

        users = await get_warns()

        wallet_amt = users[str(user.id)]["warns"]
    
        if wallet_amt == 0:
            await ctx.send(f"{user.name} have no warn yet, you should get some for fun bro.")
        else:
            em = discord.Embed(title = f"{ctx.author.name}'s total warns:", color = discord.Color.red())
            em.add_field(name= "Warns", value = wallet_amt)
            await ctx.send(embed = em)

@client.command()
@commands.has_role('King')
async def warn(ctx, mention: discord.Member,*, reason):
    await open_warn(mention)
    
    warns = await update_warns(mention)

    users = await get_warns()
    
    users[str(mention.id)]["warns"] += 1
    with open("warning.json",'w') as f:
        json.dump(users,f)
        
    await ctx.send(f"{mention} had been warn with reason: {reason}")
    await mention.send(f"You had been warn with reason: {reason}, now you have {warns +1} warns")

@client.command()
@commands.has_role('King')
async def remove(ctx, mention: discord.Member, x= 1):
    await open_warn(mention)

    users = await get_warns()

    number_of_warn = await update_warns(mention)

    if x > number_of_warn:
        await ctx.send(f"{mention} doesn't have that much warns to remove.")
    else:
        users[str(mention.id)]["warns"] -= x
        with open("warning.json",'w') as f:
            json.dump(users,f)
        
        await ctx.send(f"Successful remove {mention} {x} warn.")

@client.command()
@commands.has_role('King')
async def remove_all(ctx, mention: discord.Member):
    await open_warn(mention)

    users = await get_warns()

    users[str(mention.id)]["warns"] = 0
    with open("warning.json",'w') as f:
        json.dump(users,f)
        
    await ctx.send(f"Successful remove all {mention} warns.")



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

    with open("bank.json", 'w') as f:
        json.dump(users,f)

    bal = users[str(user.id)]["KR"]
    return bal

async def collected_unob(user):                                             #for unobtainable
    member = await get_unob_data()

    if str(user.id) in member:
        return False
    else:
        member[str(user.id)] = {}
        member[str(user.id)]["Frostbite"] = 0
        member[str(user.id)]["Fagdfaust IV"] = 0
        member[str(user.id)]["Coroller"] = 0
        member[str(user.id)]["Vertigo"] = 0
        member[str(user.id)]["RGB"] = 0
        member[str(user.id)]["Disintegrator"] = 0
        member[str(user.id)]["Anti-matter"] = 0
        member[str(user.id)]["Scouts Honor"] = 0
        member[str(user.id)]["Moonfeather"] = 0
        member[str(user.id)]["Ghostie"] = 0
        member[str(user.id)]["Eternal Frost"] = 0
        member[str(user.id)]["Keeper Of The Deep"] = 0
        member[str(user.id)]["Flying Dutchman"] = 0
        member[str(user.id)]["Assault Drone"] = 0
        member[str(user.id)]["Deep Space"] = 0
        member[str(user.id)]["Mysterious Orb"] = 0
        member[str(user.id)]["Bruisegg"] = 0
        member[str(user.id)]["ZENITH"] = 0
        member[str(user.id)]["Esper"] = 0
        member[str(user.id)]["Forbidden Tome"] = 0
        member[str(user.id)]["ESPER"] = 0
        member[str(user.id)]["Attack Drone"] = 0
        member[str(user.id)]["DOS Armour"] = 0
        member[str(user.id)]["DOS"] = 0
        member[str(user.id)]["DOS Walker"] = 0
        member[str(user.id)]["DOS Belt"] = 0
        member[str(user.id)]["Devourer Of Souls"] = 0
    with open("unob.json",'w') as f:                                        #json file for database
        json.dump(member, f)
    return True

async def get_unob_data():
    with open("unob.json",'r') as f:
        unob = json.load(f)
    return unob

async def open_inv(user):                                                   #inventory system
    member = await get_inv_data()

    if str(user.id) in member:
        return False
    else:
        member[str(user.id)] = {}
        member[str(user.id)]["Rare"] = 0
        member[str(user.id)]["Epic"] = 0
        member[str(user.id)]["Legendary"] = 0
        member[str(user.id)]["Relic"] = 0
        member[str(user.id)]["Contraband"] = 0
        member[str(user.id)]["Unobtainable"] = 0
        member[str(user.id)]["Nitro Basic ticket"] = 0

    with open("inventory.json",'w') as f:                                    #json file for database
        json.dump(member, f)
    return True

async def get_inv_data():
    with open("inventory.json",'r') as f:
        member = json.load(f)
    return member

async def use_ticket(user, change = 0, mode = "Nitro Basic ticket"):
    users = await get_inv_data()

    users[str(user.id)][mode] += change

    with open("inventory.json", 'w') as f:
        json.dump(users,f)

    ticket = users[str(user.id)]["Nitro Basic ticket"]
    return ticket

async def update_inv(user, change = 0, mode = "Unobtainable"):
    member = await get_inv_data()

    member[str(user.id)][mode] += change

    with open("inventory.json", 'w') as f:
        json.dump(member,f)

    unob = member[str(user.id)]["Unobtainable"]
    return unob

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

@client.command()                                                           #make and check inventory account
async def inv(ctx, mention: discord.Member = None):
    if mention != None:
        await open_inv(mention)
        unob = await update_inv(mention)

        if 1 > unob:
            await open_inv(mention)

            member = await get_inv_data()

            Rare = member[str(mention.id)]["Rare"]
            Epic = member[str(mention.id)]["Epic"]
            Legendary = member[str(mention.id)]["Legendary"]
            Relic = member[str(mention.id)]["Relic"]
            Contraband = member[str(mention.id)]["Contraband"]
            Unobtainable = member[str(mention.id)]["Unobtainable"]
            Nitro_Basic_ticket = member[str(mention.id)]["Nitro Basic ticket"]
    
            em = discord.Embed(title = f"{mention}'s inventory", color = discord.Color.red())
            em.add_field(name= "Rare", value = Rare, inline= False)
            em.add_field(name= "Epic", value = Epic, inline= False)
            em.add_field(name= "Legendary", value = Legendary, inline= False)
            em.add_field(name= "Relic", value = Relic, inline= False)
            em.add_field(name= "Contraband", value = Contraband, inline= False)
            em.add_field(name= "Unobtainable", value = Unobtainable, inline= False)
            em.add_field(name= "Nitro Basic ticket", value = Nitro_Basic_ticket, inline= False)
            await ctx.send(embed = em)
        else:
            button1 = Button(label= "Collection", style= discord.ButtonStyle.primary)
            button_back1 = Button(label="❌", style= discord.ButtonStyle.primary)
            next_button1 = Button(label= "➡", style= discord.ButtonStyle.primary)
            next_button2 = Button(label= "➡", style= discord.ButtonStyle.primary)
            previous_button1 = Button(label= "⬅", style= discord.ButtonStyle.primary)
            previous_button2 = Button(label= "⬅", style= discord.ButtonStyle.primary)

            await open_inv(mention)

            member = await get_inv_data()

            collection = await get_unob_data()

            Rare = member[str(mention.id)]["Rare"]
            Epic = member[str(mention.id)]["Epic"]
            Legendary = member[str(mention.id)]["Legendary"]
            Relic = member[str(mention.id)]["Relic"]
            Contraband = member[str(mention.id)]["Contraband"]
            Unobtainable = member[str(mention.id)]["Unobtainable"]
            Nitro_Basic_ticket = member[str(mention.id)]["Nitro Basic ticket"]

            async def button_callback(interaction):
                Frostbite = collection[str(mention.id)]["Frostbite"]
                Fagdfaust_IV = collection[str(mention.id)]["Fagdfaust IV"]
                Coroller = collection[str(mention.id)]["Coroller"]
                Vertigo = collection[str(mention.id)]["Vertigo"]
                rgb = collection[str(mention.id)]["RGB"]
                Disintegrator = collection[str(mention.id)]["Disintegrator"]
                Anti_matter = collection[str(mention.id)]["Anti-matter"]
                Scouts_Honor = collection[str(mention.id)]["Scouts Honor"]
                Moonfeather = collection[str(mention.id)]["Moonfeather"]
                Ghostie = collection[str(mention.id)]["Ghostie"]

                em = discord.Embed(title= f"{mention}'s unobtainable collection:", color= discord.Color.red())
                em.add_field(name= "Frostbite", value= Frostbite, inline= False)
                em.add_field(name= "Fagdfaust IV", value= Fagdfaust_IV, inline= False)
                em.add_field(name= "Coroller", value= Coroller, inline= False)
                em.add_field(name= "Vertigo", value= Vertigo, inline= False)
                em.add_field(name= "RGB", value= rgb, inline= False)
                em.add_field(name= "Disintegrator", value= Disintegrator, inline= False)
                em.add_field(name= "Anti-matter", value= Anti_matter, inline= False)
                em.add_field(name= "Scouts Honor", value= Scouts_Honor, inline= False)
                em.add_field(name= "Moonfeather", value= Moonfeather, inline= False)
                em.add_field(name= "Ghostie", value= Ghostie, inline= False)

                view = View()
                view.add_item(button_back1)
                view.add_item(next_button1)
                await interaction.response.edit_message(embed = em, view = view)
            button1.callback = button_callback

            async def button_callback(interaction):
                Eternal_Frost = collection[str(mention.id)]["Eternal Frost"]
                Keeper_Of_The_Deep = collection[str(mention.id)]["Keeper Of The Deep"]
                Flying_Dutchman = collection[str(mention.id)]["Flying Dutchman"]
                Assault_Drone = collection[str(mention.id)]["Assault Drone"]
                Deep_Space = collection[str(mention.id)]["Deep Space"]
                Mysterious_Orb = collection[str(mention.id)]["Mysterious Orb"]
                Bruisegg = collection[str(mention.id)]["Bruisegg"]
                zenith = collection[str(mention.id)]["ZENITH"]
                Esper = collection[str(mention.id)]["Esper"]
                Forbidden_Tome = collection[str(mention.id)]["Forbidden Tome"]

                em = discord.Embed(title= f"{mention}'s unobtainable collection:", color= discord.Color.red())
                em.add_field(name= "Eternal Frost", value= Eternal_Frost, inline= False)
                em.add_field(name= "Keeper Of The Deep", value= Keeper_Of_The_Deep, inline= False)
                em.add_field(name= "Flying Dutchman", value= Flying_Dutchman, inline= False)
                em.add_field(name= "Assault Drone", value= Assault_Drone, inline= False)
                em.add_field(name= "Deep Space", value= Deep_Space, inline= False)
                em.add_field(name= "Mysterious Orb", value= Mysterious_Orb, inline= False)
                em.add_field(name= "Bruisegg", value= Bruisegg, inline= False)
                em.add_field(name= "ZENITH", value= zenith, inline= False)
                em.add_field(name= "Esper", value= Esper, inline= False)
                em.add_field(name= "Forbidden Tome", value= Forbidden_Tome, inline= False)

                view = View()
                view.add_item(button_back1)
                view.add_item(previous_button1)
                view.add_item(next_button2)
                await interaction.response.edit_message(embed = em, view = view)
            next_button1.callback = button_callback

            async def button_callback(interaction):
                Frostbite = collection[str(mention.id)]["Frostbite"]
                Fagdfaust_IV = collection[str(mention.id)]["Fagdfaust IV"]
                Coroller = collection[str(mention.id)]["Coroller"]
                Vertigo = collection[str(mention.id)]["Vertigo"]
                rgb = collection[str(mention.id)]["RGB"]
                Disintegrator = collection[str(mention.id)]["Disintegrator"]
                Anti_matter = collection[str(mention.id)]["Anti-matter"]
                Scouts_Honor = collection[str(mention.id)]["Scouts Honor"]
                Moonfeather = collection[str(mention.id)]["Moonfeather"]
                Ghostie = collection[str(mention.id)]["Ghostie"]

                em = discord.Embed(title= f"{mention}'s unobtainable collection:", color= discord.Color.red())
                em.add_field(name= "Frostbite", value= Frostbite, inline= False)
                em.add_field(name= "Fagdfaust IV", value= Fagdfaust_IV, inline= False)
                em.add_field(name= "Coroller", value= Coroller, inline= False)
                em.add_field(name= "Vertigo", value= Vertigo, inline= False)
                em.add_field(name= "RGB", value= rgb, inline= False)
                em.add_field(name= "Disintegrator", value= Disintegrator, inline= False)
                em.add_field(name= "Anti-matter", value= Anti_matter, inline= False)
                em.add_field(name= "Scouts Honor", value= Scouts_Honor, inline= False)
                em.add_field(name= "Moonfeather", value= Moonfeather, inline= False)
                em.add_field(name= "Ghostie", value= Ghostie, inline= False)

                view = View()
                view.add_item(button_back1)
                view.add_item(next_button1)
                await interaction.response.edit_message(embed = em, view = view)
            previous_button1.callback = button_callback

            async def button_callback(interaction):
                Esper1 = collection[str(mention.id)]["ESPER"]
                Attack_Drone = collection[str(mention.id)]["Attack Drone"]
                DOS_Armour = collection[str(mention.id)]["DOS Armour"]
                Dos = collection[str(mention.id)]["DOS"]
                DOS_Walker = collection[str(mention.id)]["DOS Walker"]
                DOS_Belt = collection[str(mention.id)]["DOS Belt"]
                Devourer_Of_Souls = collection[str(mention.id)]["Devourer Of Souls"]

                em = discord.Embed(title= f"{mention}'s unobtainable collection:", color= discord.Color.red())
                em.add_field(name= "ESPER", value= Esper1, inline= False)
                em.add_field(name= "Attack Drone", value= Attack_Drone, inline= False)
                em.add_field(name= "DOS Armour", value= DOS_Armour, inline= False)
                em.add_field(name= "DOS", value= Dos, inline= False)
                em.add_field(name= "DOS Walker", value= DOS_Walker, inline= False)
                em.add_field(name= "DOS Belt", value= DOS_Belt, inline= False)
                em.add_field(name= "Devourer Of Souls", value= Devourer_Of_Souls, inline= False)

                view = View()
                view.add_item(button_back1)
                view.add_item(previous_button2)
                await interaction.response.edit_message(embed = em, view = view)
            next_button2.callback = button_callback

            async def button_callback(interaction):
                Eternal_Frost = collection[str(mention.id)]["Eternal Frost"]
                Keeper_Of_The_Deep = collection[str(mention.id)]["Keeper Of The Deep"]
                Flying_Dutchman = collection[str(mention.id)]["Flying Dutchman"]
                Assault_Drone = collection[str(mention.id)]["Assault Drone"]
                Deep_Space = collection[str(mention.id)]["Deep Space"]
                Mysterious_Orb = collection[str(mention.id)]["Mysterious Orb"]
                Bruisegg = collection[str(mention.id)]["Bruisegg"]
                zenith = collection[str(mention.id)]["ZENITH"]
                Esper = collection[str(mention.id)]["Esper"]
                Forbidden_Tome = collection[str(mention.id)]["Forbidden Tome"]

                em = discord.Embed(title= f"{mention}'s unobtainable collection:", color= discord.Color.red())
                em.add_field(name= "Eternal Frost", value= Eternal_Frost, inline= False)
                em.add_field(name= "Keeper Of The Deep", value= Keeper_Of_The_Deep, inline= False)
                em.add_field(name= "Flying Dutchman", value= Flying_Dutchman, inline= False)
                em.add_field(name= "Assault Drone", value= Assault_Drone, inline= False)
                em.add_field(name= "Deep Space", value= Deep_Space, inline= False)
                em.add_field(name= "Mysterious Orb", value= Mysterious_Orb, inline= False)
                em.add_field(name= "Bruisegg", value= Bruisegg, inline= False)
                em.add_field(name= "ZENITH", value= zenith, inline= False)
                em.add_field(name= "Esper", value= Esper, inline= False)
                em.add_field(name= "Forbidden Tome", value= Forbidden_Tome, inline= False)

                view = View()
                view.add_item(button_back1)
                view.add_item(previous_button1)
                view.add_item(next_button2)
                await interaction.response.edit_message(embed = em, view = view)
            previous_button2.callback = button_callback

            async def button_callback(interaction):
                em = discord.Embed(title = f"{mention}'s inventory", color = discord.Color.red())
                em.add_field(name= "Rare", value = Rare, inline= False)
                em.add_field(name= "Epic", value = Epic)
                em.add_field(name= "Legendary", value = Legendary, inline= False)
                em.add_field(name= "Relic", value = Relic, inline= False)
                em.add_field(name= "Contraband", value = Contraband, inline= False)
                em.add_field(name= "Unobtainable", value = Unobtainable, inline= False)
                em.add_field(name= "Nitro Basic ticket", value = Nitro_Basic_ticket, inline= False)

                view = View()
                view.add_item(button1)

                await interaction.response.edit_message(embed = em, view = view)
            button_back1.callback = button_callback

            em = discord.Embed(title = f"{mention}'s inventory", color = discord.Color.red())
            em.add_field(name= "Rare", value = Rare, inline= False)
            em.add_field(name= "Epic", value = Epic, inline= False)
            em.add_field(name= "Legendary", value = Legendary, inline= False)
            em.add_field(name= "Relic", value = Relic, inline= False)
            em.add_field(name= "Contraband", value = Contraband, inline= False)
            em.add_field(name= "Unobtainable", value = Unobtainable, inline= False)
            em.add_field(name= "Nitro Basic ticket", value = Nitro_Basic_ticket, inline= False)

            view = View()
            view.add_item(button1)

            await ctx.send(embed = em, view = view)
    else:
        await open_inv(ctx.author)
        unob = await update_inv(ctx.author)
        if 1 > unob:
            await open_inv(ctx.author)

            user = ctx.author

            member = await get_inv_data()

            Rare = member[str(user.id)]["Rare"]
            Epic = member[str(user.id)]["Epic"]
            Legendary = member[str(user.id)]["Legendary"]
            Relic = member[str(user.id)]["Relic"]
            Contraband = member[str(user.id)]["Contraband"]
            Unobtainable = member[str(user.id)]["Unobtainable"]
            Nitro_Basic_ticket = member[str(user.id)]["Nitro Basic ticket"]
    
            em = discord.Embed(title = f"{ctx.author.name}'s inventory", color = discord.Color.red())
            em.add_field(name= "Rare", value = Rare, inline= False)
            em.add_field(name= "Epic", value = Epic, inline= False)
            em.add_field(name= "Legendary", value = Legendary, inline= False)
            em.add_field(name= "Relic", value = Relic, inline= False)
            em.add_field(name= "Contraband", value = Contraband, inline= False)
            em.add_field(name= "Unobtainable", value = Unobtainable, inline= False)
            em.add_field(name= "Nitro Basic ticket", value = Nitro_Basic_ticket, inline= False)
            await ctx.send(embed = em)
        else:
            button1 = Button(label= "Collection", style= discord.ButtonStyle.primary)
            button_back1 = Button(label="❌", style= discord.ButtonStyle.primary)
            next_button1 = Button(label= "➡", style= discord.ButtonStyle.primary)
            next_button2 = Button(label= "➡", style= discord.ButtonStyle.primary)
            previous_button1 = Button(label= "⬅", style= discord.ButtonStyle.primary)
            previous_button2 = Button(label= "⬅", style= discord.ButtonStyle.primary)

            await open_inv(ctx.author)

            user = ctx.author

            member = await get_inv_data()

            collection = await get_unob_data()

            Rare = member[str(user.id)]["Rare"]
            Epic = member[str(user.id)]["Epic"]
            Legendary = member[str(user.id)]["Legendary"]
            Relic = member[str(user.id)]["Relic"]
            Contraband = member[str(user.id)]["Contraband"]
            Unobtainable = member[str(user.id)]["Unobtainable"]
            Nitro_Basic_ticket = member[str(user.id)]["Nitro Basic ticket"]

            async def button_callback(interaction):
                Frostbite = collection[str(user.id)]["Frostbite"]
                Fagdfaust_IV = collection[str(user.id)]["Fagdfaust IV"]
                Coroller = collection[str(user.id)]["Coroller"]
                Vertigo = collection[str(user.id)]["Vertigo"]
                rgb = collection[str(user.id)]["RGB"]
                Disintegrator = collection[str(user.id)]["Disintegrator"]
                Anti_matter = collection[str(user.id)]["Anti-matter"]
                Scouts_Honor = collection[str(user.id)]["Scouts Honor"]
                Moonfeather = collection[str(user.id)]["Moonfeather"]
                Ghostie = collection[str(user.id)]["Ghostie"]

                em = discord.Embed(title= f"{ctx.author.name}'s unobtainable collection:", color= discord.Color.red())
                em.add_field(name= "Frostbite", value= Frostbite, inline= False)
                em.add_field(name= "Fagdfaust IV", value= Fagdfaust_IV, inline= False)
                em.add_field(name= "Coroller", value= Coroller, inline= False)
                em.add_field(name= "Vertigo", value= Vertigo, inline= False)
                em.add_field(name= "RGB", value= rgb, inline= False)
                em.add_field(name= "Disintegrator", value= Disintegrator, inline= False)
                em.add_field(name= "Anti-matter", value= Anti_matter, inline= False)
                em.add_field(name= "Scouts Honor", value= Scouts_Honor, inline= False)
                em.add_field(name= "Moonfeather", value= Moonfeather, inline= False)
                em.add_field(name= "Ghostie", value= Ghostie, inline= False)

                view = View()
                view.add_item(button_back1)
                view.add_item(next_button1)
                await interaction.response.edit_message(embed = em, view = view)
            button1.callback = button_callback

            async def button_callback(interaction):
                Eternal_Frost = collection[str(user.id)]["Eternal Frost"]
                Keeper_Of_The_Deep = collection[str(user.id)]["Keeper Of The Deep"]
                Flying_Dutchman = collection[str(user.id)]["Flying Dutchman"]
                Assault_Drone = collection[str(user.id)]["Assault Drone"]
                Deep_Space = collection[str(user.id)]["Deep Space"]
                Mysterious_Orb = collection[str(user.id)]["Mysterious Orb"]
                Bruisegg = collection[str(user.id)]["Bruisegg"]
                zenith = collection[str(user.id)]["ZENITH"]
                Esper = collection[str(user.id)]["Esper"]
                Forbidden_Tome = collection[str(user.id)]["Forbidden Tome"]

                em = discord.Embed(title= f"{ctx.author.name}'s unobtainable collection:", color= discord.Color.red())
                em.add_field(name= "Eternal Frost", value= Eternal_Frost, inline= False)
                em.add_field(name= "Keeper Of The Deep", value= Keeper_Of_The_Deep, inline= False)
                em.add_field(name= "Flying Dutchman", value= Flying_Dutchman, inline= False)
                em.add_field(name= "Assault Drone", value= Assault_Drone, inline= False)
                em.add_field(name= "Deep Space", value= Deep_Space, inline= False)
                em.add_field(name= "Mysterious Orb", value= Mysterious_Orb, inline= False)
                em.add_field(name= "Bruisegg", value= Bruisegg, inline= False)
                em.add_field(name= "ZENITH", value= zenith, inline= False)
                em.add_field(name= "Esper", value= Esper, inline= False)
                em.add_field(name= "Forbidden Tome", value= Forbidden_Tome, inline= False)

                view = View()
                view.add_item(button_back1)
                view.add_item(previous_button1)
                view.add_item(next_button2)
                await interaction.response.edit_message(embed = em, view = view)
            next_button1.callback = button_callback

            async def button_callback(interaction):
                Frostbite = collection[str(user.id)]["Frostbite"]
                Fagdfaust_IV = collection[str(user.id)]["Fagdfaust IV"]
                Coroller = collection[str(user.id)]["Coroller"]
                Vertigo = collection[str(user.id)]["Vertigo"]
                rgb = collection[str(user.id)]["RGB"]
                Disintegrator = collection[str(user.id)]["Disintegrator"]
                Anti_matter = collection[str(user.id)]["Anti-matter"]
                Scouts_Honor = collection[str(user.id)]["Scouts Honor"]
                Moonfeather = collection[str(user.id)]["Moonfeather"]
                Ghostie = collection[str(user.id)]["Ghostie"]

                em = discord.Embed(title= f"{ctx.author.name}'s unobtainable collection:", color= discord.Color.red())
                em.add_field(name= "Frostbite", value= Frostbite, inline= False)
                em.add_field(name= "Fagdfaust IV", value= Fagdfaust_IV, inline= False)
                em.add_field(name= "Coroller", value= Coroller, inline= False)
                em.add_field(name= "Vertigo", value= Vertigo, inline= False)
                em.add_field(name= "RGB", value= rgb, inline= False)
                em.add_field(name= "Disintegrator", value= Disintegrator, inline= False)
                em.add_field(name= "Anti-matter", value= Anti_matter, inline= False)
                em.add_field(name= "Scouts Honor", value= Scouts_Honor, inline= False)
                em.add_field(name= "Moonfeather", value= Moonfeather, inline= False)
                em.add_field(name= "Ghostie", value= Ghostie)

                view = View()
                view.add_item(button_back1)
                view.add_item(next_button1)
                await interaction.response.edit_message(embed = em, view = view)
            previous_button1.callback = button_callback

            async def button_callback(interaction):
                Esper1 = collection[str(user.id)]["ESPER"]
                Attack_Drone = collection[str(user.id)]["Attack Drone"]
                DOS_Armour = collection[str(user.id)]["DOS Armour"]
                Dos = collection[str(user.id)]["DOS"]
                DOS_Walker = collection[str(user.id)]["DOS Walker"]
                DOS_Belt = collection[str(user.id)]["DOS Belt"]
                Devourer_Of_Souls = collection[str(user.id)]["Devourer Of Souls"]

                em = discord.Embed(title= f"{ctx.author.name}'s unobtainable collection:", color= discord.Color.red())
                em.add_field(name= "ESPER", value= Esper1, inline= False)
                em.add_field(name= "Attack Drone", value= Attack_Drone, inline= False)
                em.add_field(name= "DOS Armour", value= DOS_Armour, inline= False)
                em.add_field(name= "DOS", value= Dos, inline= False)
                em.add_field(name= "DOS Walker", value= DOS_Walker, inline= False)
                em.add_field(name= "DOS Belt", value= DOS_Belt, inline= False)
                em.add_field(name= "Devourer Of Souls", value= Devourer_Of_Souls, inline= False)

                view = View()
                view.add_item(button_back1)
                view.add_item(previous_button2)
                await interaction.response.edit_message(embed = em, view = view)
            next_button2.callback = button_callback

            async def button_callback(interaction):
                Eternal_Frost = collection[str(user.id)]["Eternal Frost"]
                Keeper_Of_The_Deep = collection[str(user.id)]["Keeper Of The Deep"]
                Flying_Dutchman = collection[str(user.id)]["Flying Dutchman"]
                Assault_Drone = collection[str(user.id)]["Assault Drone"]
                Deep_Space = collection[str(user.id)]["Deep Space"]
                Mysterious_Orb = collection[str(user.id)]["Mysterious Orb"]
                Bruisegg = collection[str(user.id)]["Bruisegg"]
                zenith = collection[str(user.id)]["ZENITH"]
                Esper = collection[str(user.id)]["Esper"]
                Forbidden_Tome = collection[str(user.id)]["Forbidden Tome"]

                em = discord.Embed(title= f"{ctx.author.name}'s unobtainable collection:", color= discord.Color.red())
                em.add_field(name= "Eternal Frost", value= Eternal_Frost, inline= False)
                em.add_field(name= "Keeper Of The Deep", value= Keeper_Of_The_Deep, inline= False)
                em.add_field(name= "Flying Dutchman", value= Flying_Dutchman, inline= False)
                em.add_field(name= "Assault Drone", value= Assault_Drone, inline= False)
                em.add_field(name= "Deep Space", value= Deep_Space, inline= False)
                em.add_field(name= "Mysterious Orb", value= Mysterious_Orb, inline= False)
                em.add_field(name= "Bruisegg", value= Bruisegg, inline= False)
                em.add_field(name= "ZENITH", value= zenith, inline= False)
                em.add_field(name= "Esper", value= Esper, inline= False)
                em.add_field(name= "Forbidden Tome", value= Forbidden_Tome, inline= False)

                view = View()
                view.add_item(button_back1)
                view.add_item(previous_button1)
                view.add_item(next_button2)
                await interaction.response.edit_message(embed = em, view = view)
            previous_button2.callback = button_callback

            async def button_callback(interaction):
                em = discord.Embed(title = f"{ctx.author.name}'s inventory", color = discord.Color.red())
                em.add_field(name= "Rare", value = Rare)
                em.add_field(name= "Epic", value = Epic)
                em.add_field(name= "Legendary", value = Legendary)
                em.add_field(name= "Relic", value = Relic)
                em.add_field(name= "Contraband", value = Contraband)
                em.add_field(name= "Unobtainable", value = Unobtainable)
                em.add_field(name= "Nitro Basic ticket", value = Nitro_Basic_ticket)

                view = View()
                view.add_item(button1)

                await interaction.response.edit_message(embed = em, view = view)
            button_back1.callback = button_callback

            em = discord.Embed(title = f"{ctx.author.name}'s inventory", color = discord.Color.red())
            em.add_field(name= "Rare", value = Rare, inline= False)
            em.add_field(name= "Epic", value = Epic, inline= False)
            em.add_field(name= "Legendary", value = Legendary, inline= False)
            em.add_field(name= "Relic", value = Relic, inline= False)
            em.add_field(name= "Contraband", value = Contraband, inline= False)
            em.add_field(name= "Unobtainable", value = Unobtainable, inline= False)
            em.add_field(name= "Nitro Basic ticket", value = Nitro_Basic_ticket, inline= False)

            view = View()
            view.add_item(button1)

            await ctx.send(embed = em, view = view)

@client.command()                                                           #work earn 500 - 1000
@commands.cooldown(1, 10*60, commands.BucketType.user)
async def work(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()

    user = ctx.author

    earnings = random.randint(500, 1500)

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

        await ctx.send(f"Rain of KR and you receive: {earnings} KR")

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

        await ctx.send(f"You found a golden nugget and sold for: {earnings} KR")

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

@client.command()                                                           #rob earn/lose 0 - 500
@commands.cooldown(1,3*60, commands.BucketType.user)
async def rob(ctx, mention: discord.Member):
    await open_account(ctx.author)
    await open_account(mention)

    users = await get_bank_data()

    thief = ctx.author
    victim = mention


    i = random.randint(1, 1000)

    if i == 1:
        amount = random.randint(151, 500)

        bal_of_thief = await update_bank(thief)
        bal_of_victim = await update_bank(victim)

        index = random.randint(1,2)
        if index == 2:
            if amount > bal_of_victim:
                await ctx.send(f"{ctx.author.name} successful rob all {mention} KR")

                users[str(victim.id)]["KR"] -= bal_of_victim
                with open("bank.json",'w') as f:
                    json.dump(users,f)

                users[str(thief.id)]["KR"] += bal_of_victim
                with open("bank.json",'w') as f:
                    json.dump(users,f)
            else:
                await ctx.send(f"{ctx.author.name} successful rob {mention}: {amount} KR")

                users[str(victim.id)]["KR"] -= amount
                with open("bank.json",'w') as f:
                    json.dump(users,f)

                users[str(thief.id)]["KR"] += amount
                with open("bank.json",'w') as f:
                    json.dump(users,f)
        else:
            if amount > bal_of_thief:
                await ctx.send(f"{thief.name} got caught and pay all KR to {victim}")

                users[str(victim.id)]["KR"] += bal_of_thief
                with open("bank.json",'w') as f:
                    json.dump(users,f)

                users[str(thief.id)]["KR"] -= bal_of_thief
                with open("bank.json",'w') as f:
                    json.dump(users,f)

            else:
                await ctx.send(f"{thief.name} got caught and pay {amount} KR to {victim}")

                users[str(thief.id)]["KR"] -= amount
                with open("bank.json",'w') as f:
                    json.dump(users,f)

                users[str(victim.id)]["KR"] += amount
                with open("bank.json",'w') as f:
                    json.dump(users,f)

    elif 2 <= i <= 50:
        amount = random.randint(101, 150)

        bal_of_thief = await update_bank(thief)
        bal_of_victim = await update_bank(victim)

        index = random.randint(1,2)
        if index == 2:
            if amount > bal_of_victim:
                await ctx.send(f"{ctx.author.name} successful rob all {mention} KR")

                users[str(victim.id)]["KR"] -= bal_of_victim
                with open("bank.json",'w') as f:
                    json.dump(users,f)

                users[str(thief.id)]["KR"] += bal_of_victim
                with open("bank.json",'w') as f:
                    json.dump(users,f)
            else:
                await ctx.send(f"{ctx.author.name} successful rob {mention}: {amount} KR")

                users[str(victim.id)]["KR"] -= amount
                with open("bank.json",'w') as f:
                    json.dump(users,f)

                users[str(thief.id)]["KR"] += amount
                with open("bank.json",'w') as f:
                    json.dump(users,f)
        else:
            if amount > bal_of_thief:
                await ctx.send(f"{thief.name} got caught and pay all KR to {victim}")

                users[str(victim.id)]["KR"] += bal_of_thief
                with open("bank.json",'w') as f:
                    json.dump(users,f)

                users[str(thief.id)]["KR"] -= bal_of_thief
                with open("bank.json",'w') as f:
                    json.dump(users,f)

            else:
                await ctx.send(f"{thief.name} got caught and pay {amount} KR to {victim}")

                users[str(thief.id)]["KR"] -= amount
                with open("bank.json",'w') as f:
                    json.dump(users,f)

                users[str(victim.id)]["KR"] += amount
                with open("bank.json",'w') as f:
                    json.dump(users,f)

    elif 51 <= i <= 150:
        amount = random.randint(51, 100)

        bal_of_thief = await update_bank(thief)
        bal_of_victim = await update_bank(victim)

        index = random.randint(1,2)
        if index == 2:
            if amount > bal_of_victim:
                await ctx.send(f"{ctx.author.name} successful rob all {mention} KR")

                users[str(victim.id)]["KR"] -= bal_of_victim
                with open("bank.json",'w') as f:
                    json.dump(users,f)

                users[str(thief.id)]["KR"] += bal_of_victim
                with open("bank.json",'w') as f:
                    json.dump(users,f)
            else:
                await ctx.send(f"{ctx.author.name} successful rob {mention}: {amount} KR")

                users[str(victim.id)]["KR"] -= amount
                with open("bank.json",'w') as f:
                    json.dump(users,f)

                users[str(thief.id)]["KR"] += amount
                with open("bank.json",'w') as f:
                    json.dump(users,f)
        else:
            if amount > bal_of_thief:
                await ctx.send(f"{thief.name} got caught and pay all KR to {victim}")

                users[str(victim.id)]["KR"] += bal_of_thief
                with open("bank.json",'w') as f:
                    json.dump(users,f)

                users[str(thief.id)]["KR"] -= bal_of_thief
                with open("bank.json",'w') as f:
                    json.dump(users,f)

            else:
                await ctx.send(f"{thief.name} got caught and pay {amount} KR to {victim}")

                users[str(thief.id)]["KR"] -= amount
                with open("bank.json",'w') as f:
                    json.dump(users,f)

                users[str(victim.id)]["KR"] += amount
                with open("bank.json",'w') as f:
                    json.dump(users,f)

    elif 151 <= i <= 350:
        amount = random.randint(31, 50)

        bal_of_thief = await update_bank(thief)
        bal_of_victim = await update_bank(victim)

        index = random.randint(1,2)
        if index == 2:
            if amount > bal_of_victim:
                await ctx.send(f"{ctx.author.name} successful rob all {mention} KR")

                users[str(victim.id)]["KR"] -= bal_of_victim
                with open("bank.json",'w') as f:
                    json.dump(users,f)

                users[str(thief.id)]["KR"] += bal_of_victim
                with open("bank.json",'w') as f:
                    json.dump(users,f)
            else:
                await ctx.send(f"{ctx.author.name} successful rob {mention}: {amount} KR")

                users[str(victim.id)]["KR"] -= amount
                with open("bank.json",'w') as f:
                    json.dump(users,f)

                users[str(thief.id)]["KR"] += amount
                with open("bank.json",'w') as f:
                    json.dump(users,f)
        else:
            if amount > bal_of_thief:
                await ctx.send(f"{thief.name} got caught and pay all KR to {victim}")

                users[str(victim.id)]["KR"] += bal_of_thief
                with open("bank.json",'w') as f:
                    json.dump(users,f)

                users[str(thief.id)]["KR"] -= bal_of_thief
                with open("bank.json",'w') as f:
                    json.dump(users,f)

            else:
                await ctx.send(f"{thief.name} got caught and pay {amount} KR to {victim}")

                users[str(thief.id)]["KR"] -= amount
                with open("bank.json",'w') as f:
                    json.dump(users,f)

                users[str(victim.id)]["KR"] += amount
                with open("bank.json",'w') as f:
                    json.dump(users,f)

    else:
        amount = random.randint(21, 30)

        bal_of_thief = await update_bank(thief)
        bal_of_victim = await update_bank(victim)

        index = random.randint(1,2)
        if index == 2:
            if amount > bal_of_victim:
                await ctx.send(f"{ctx.author.name} successful rob all {mention} KR")

                users[str(victim.id)]["KR"] -= bal_of_victim
                with open("bank.json",'w') as f:
                    json.dump(users,f)

                users[str(thief.id)]["KR"] += bal_of_victim
                with open("bank.json",'w') as f:
                    json.dump(users,f)
            else:
                await ctx.send(f"{ctx.author.name} successful rob {mention}: {amount} KR")

                users[str(victim.id)]["KR"] -= amount
                with open("bank.json",'w') as f:
                    json.dump(users,f)

                users[str(thief.id)]["KR"] += amount
                with open("bank.json",'w') as f:
                    json.dump(users,f)
        else:
            if amount > bal_of_thief:
                await ctx.send(f"{thief.name} got caught and pay all KR to {victim}")

                users[str(victim.id)]["KR"] += bal_of_thief
                with open("bank.json",'w') as f:
                    json.dump(users,f)

                users[str(thief.id)]["KR"] -= bal_of_thief
                with open("bank.json",'w') as f:
                    json.dump(users,f)

            else:
                await ctx.send(f"{thief.name} got caught and pay {amount} KR to {victim}")

                users[str(thief.id)]["KR"] -= amount
                with open("bank.json",'w') as f:
                    json.dump(users,f)

                users[str(victim.id)]["KR"] += amount
                with open("bank.json",'w') as f:
                    json.dump(users,f)

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def toss(ctx, bet: int):
    await open_account(ctx.author)

    bal = await update_bank(ctx.author)
    
    if bet > bal:
        await ctx.send("You don't have enough KR !!")
    else:
        users = await get_bank_data()

        user = ctx.author

        users[str(user.id)]["KR"] -= bet
        with open("bank.json",'w') as f:
            json.dump(users,f)

        button1 = Button(label= "front", style= discord.ButtonStyle.primary, emoji="<:kr1:1244816845781991527>")
        button2 = Button(label= "back", style= discord.ButtonStyle.primary, emoji="<:kr2:1244824676115419199>")

        async def button_callback(interaction):
            if interaction.user == ctx.author:
                i = random.randint(1, 2)
                if i == 1:
                    em = discord.Embed(title = f"Congratulation you guess right: you won {bet*2} KR", color = discord.Color.red())
                    await interaction.response.edit_message(embed = em, view = None)
                    users[str(user.id)]["KR"] += bet*2
                    with open("bank.json",'w') as f:
                        json.dump(users,f)
                else:
                    em = discord.Embed(title = f"You are so unlucky: you lose {bet} KR", color = discord.Color.red())
                    await interaction.response.edit_message(embed = em, view = None)
            else:
                await interaction.response.send_message("You can not click this button !!", ephemeral=True)
        button1.callback = button_callback

        async def button_callback(interaction):
            if interaction.user == ctx.author:
                i = random.randint(1, 2)
                if i == 2:
                    em = discord.Embed(title = f"Congratulation you guess right: you won {bet*2} KR", color = discord.Color.red())
                    await interaction.response.edit_message(embed = em, view = None)
                    users[str(user.id)]["KR"] += bet*2
                    with open("bank.json",'w') as f:
                        json.dump(users,f)
                else:
                    em = discord.Embed(title = f"You are so unlucky: you lose {bet} KR", color = discord.Color.red())
                    await interaction.response.edit_message(embed = em, view = None)
            else:
                await interaction.response.send_message("You can not click this button !!", ephemeral=True)
        button2.callback = button_callback

        view = View()
        view.add_item(button1)
        view.add_item(button2)
        em = discord.Embed(title = f"Chose one for chance to x2 the kr you bet:", color = discord.Color.red())
        await ctx.send(embed = em, view = view)

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def dice(ctx, bet: int):
    await open_account(ctx.author)

    bal = await update_bank(ctx.author)
    
    if bet > bal:
        await ctx.send("You don't have enough KR !!")
    else:
        users = await get_bank_data()

        user = ctx.author

        users[str(user.id)]["KR"] -= bet
        with open("bank.json",'w') as f:
            json.dump(users,f)

        button1 = Button(emoji= "<:dice_1:1244828989969661953>", style= discord.ButtonStyle.primary)
        button2 = Button(emoji= "<:dice_2:1244828991915954337>", style= discord.ButtonStyle.primary)
        button3 = Button(emoji= "<:dice_3:1244828994227146863>", style= discord.ButtonStyle.primary)
        button4 = Button(emoji= "<:dice_4:1244828996236218418>", style= discord.ButtonStyle.primary)
        button5 = Button(emoji= "<:dice_5:1244828998597611572>", style= discord.ButtonStyle.primary)
        button6 = Button(emoji= "<:dice_6:1244829000682176633>", style= discord.ButtonStyle.primary)
        button7 = Button(emoji= "<:dice_7:1244829002691248189>", style= discord.ButtonStyle.primary)
        button8 = Button(emoji= "<:dice_8:1244829005488717916>", style= discord.ButtonStyle.primary)
        button9 = Button(emoji= "<:dice_9:1244829007363444767>", style= discord.ButtonStyle.primary)

        async def button_callback(interaction):
            if interaction.user == ctx.author:
                i = random.randint(1, 9)
                if i == 1:
                    em = discord.Embed(title = f"Congratulation you guess right: you won {bet*9} KR", color = discord.Color.red())
                    await interaction.response.edit_message(embed = em, view = None)
                    users[str(user.id)]["KR"] += bet*9
                    with open("bank.json",'w') as f:
                        json.dump(users,f)
                else:
                    em = discord.Embed(title = f"You are so unlucky: you lose {bet} KR", color = discord.Color.red())
                    await interaction.response.edit_message(embed = em, view = None)
            else:
                await interaction.response.send_message("You can not click this button !!", ephemeral=True)
        button1.callback = button_callback

        async def button_callback(interaction):
            if interaction.user == ctx.author:
                i = random.randint(1, 9)
                if i == 2:
                    em = discord.Embed(title = f"Congratulation you guess right: you won {bet*9} KR", color = discord.Color.red())
                    await interaction.response.edit_message(embed = em, view = None)
                    users[str(user.id)]["KR"] += bet*9
                    with open("bank.json",'w') as f:
                        json.dump(users,f)
                else:
                    em = discord.Embed(title = f"You are so unlucky: you lose {bet} KR", color = discord.Color.red())
                    await interaction.response.edit_message(embed = em, view = None)
            else:
                await interaction.response.send_message("You can not click this button !!", ephemeral=True)
        button2.callback = button_callback

        async def button_callback(interaction):
            if interaction.user == ctx.author:
                i = random.randint(1, 9)
                if i == 3:
                    em = discord.Embed(title = f"Congratulation you guess right: you won {bet*9} KR", color = discord.Color.red())
                    await interaction.response.edit_message(embed = em, view = None)
                    users[str(user.id)]["KR"] += bet*9
                    with open("bank.json",'w') as f:
                        json.dump(users,f)
                else:
                    em = discord.Embed(title = f"You are so unlucky: you lose {bet} KR", color = discord.Color.red())
                    await interaction.response.edit_message(embed = em, view = None)
            else:
                await interaction.response.send_message("You can not click this button !!", ephemeral=True)
        button3.callback = button_callback

        async def button_callback(interaction):
            if interaction.user == ctx.author:
                i = random.randint(1, 9)
                if i == 4:
                    em = discord.Embed(title = f"Congratulation you guess right: you won {bet*9} KR", color = discord.Color.red())
                    await interaction.response.edit_message(embed = em, view = None)
                    users[str(user.id)]["KR"] += bet*9
                    with open("bank.json",'w') as f:
                        json.dump(users,f)
                else:
                    em = discord.Embed(title = f"You are so unlucky: you lose {bet} KR", color = discord.Color.red())
                    await interaction.response.edit_message(embed = em, view = None)
            else:
                await interaction.response.send_message("You can not click this button !!", ephemeral=True)
        button4.callback = button_callback

        async def button_callback(interaction):
            if interaction.user == ctx.author:
                i = random.randint(1, 9)
                if i == 5:
                    em = discord.Embed(title = f"Congratulation you guess right: you won {bet*9} KR", color = discord.Color.red())
                    await interaction.response.edit_message(embed = em, view = None)
                    users[str(user.id)]["KR"] += bet*9
                    with open("bank.json",'w') as f:
                        json.dump(users,f)
                else:
                    em = discord.Embed(title = f"You are so unlucky: you lose {bet} KR", color = discord.Color.red())
                    await interaction.response.edit_message(embed = em, view = None)
            else:
                await interaction.response.send_message("You can not click this button !!", ephemeral=True)
        button5.callback = button_callback

        async def button_callback(interaction):
            if interaction.user == ctx.author:
                i = random.randint(1, 9)
                if i == 6:
                    em = discord.Embed(title = f"Congratulation you guess right: you won {bet*9} KR", color = discord.Color.red())
                    await interaction.response.edit_message(embed = em, view = None)
                    users[str(user.id)]["KR"] += bet*9
                    with open("bank.json",'w') as f:
                        json.dump(users,f)
                else:
                    em = discord.Embed(title = f"You are so unlucky: you lose {bet} KR", color = discord.Color.red())
                    await interaction.response.edit_message(embed = em, view = None)
            else:
                await interaction.response.send_message("You can not click this button !!", ephemeral=True)
        button6.callback = button_callback

        async def button_callback(interaction):
            if interaction.user == ctx.author:
                i = random.randint(1, 9)
                if i == 7:
                    em = discord.Embed(title = f"Congratulation you guess right: you won {bet*9} KR", color = discord.Color.red())
                    await interaction.response.edit_message(embed = em, view = None)
                    users[str(user.id)]["KR"] += bet*9
                    with open("bank.json",'w') as f:
                        json.dump(users,f)
                else:
                    em = discord.Embed(title = f"You are so unlucky: you lose {bet} KR", color = discord.Color.red())
                    await interaction.response.edit_message(embed = em, view = None)
            else:
                await interaction.response.send_message("You can not click this button !!", ephemeral=True)
        button7.callback = button_callback

        async def button_callback(interaction):
            if interaction.user == ctx.author:
                i = random.randint(1, 9)
                if i == 8:
                    em = discord.Embed(title = f"Congratulation you guess right: you won {bet*9} KR", color = discord.Color.red())
                    await interaction.response.edit_message(embed = em, view = None)
                    users[str(user.id)]["KR"] += bet*9
                    with open("bank.json",'w') as f:
                        json.dump(users,f)
                else:
                    em = discord.Embed(title = f"You are so unlucky: you lose {bet} KR", color = discord.Color.red())
                    await interaction.response.edit_message(embed = em, view = None)
            else:
                await interaction.response.send_message("You can not click this button !!", ephemeral=True)
        button8.callback = button_callback

        async def button_callback(interaction):
            if interaction.user == ctx.author:
                i = random.randint(1, 9)
                if i == 9:
                    em = discord.Embed(title = f"Congratulation you guess right: you won {bet*9} KR", color = discord.Color.red())
                    await interaction.response.edit_message(embed = em, view = None)
                    users[str(user.id)]["KR"] += bet*9
                    with open("bank.json",'w') as f:
                        json.dump(users,f)
                else:
                    em = discord.Embed(title = f"You are so unlucky: you lose {bet} KR", color = discord.Color.red())
                    await interaction.response.edit_message(embed = em, view = None)
            else:
                await interaction.response.send_message("You can not click this button !!", ephemeral=True)
        button9.callback = button_callback

        view = View()
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)
        view.add_item(button4)
        view.add_item(button5)
        view.add_item(button6)
        view.add_item(button7)
        view.add_item(button8)
        view.add_item(button9)
        em = discord.Embed(title = f"Chose one for chance to x9 the kr you bet:", color = discord.Color.red())
        await ctx.send(embed = em, view = view)

@client.command()                                                           #spin systems
@commands.cooldown(1, 3, commands.BucketType.user)
async def spin(ctx, x= 1):
    await open_account(ctx.author)
    
    await open_inv(ctx.author)

    bal = await update_bank(ctx.author)

    if x == 1:
        if 500 > bal:
            await ctx.send("You don't have enough KR !!")
        else:
            member = await get_inv_data()

            users = await get_bank_data()

            user = ctx.author
        
            users[str(user.id)]["KR"] += -500
            with open("bank.json",'w') as f:
                json.dump(users,f)

            i = random.randint(1, 10000)
            if i == 1:
                await ctx.send("<a:spin:1243478409930080342> Congratulation, you won the jackpot prize: a basic nitro ticket")

                member[str(user.id)]["Nitro Basic ticket"] += 1
                with open("inventory.json",'w') as f:
                    json.dump(member,f)
                    
            elif 2 <= i <= 10:
                await open_inv(ctx.author)
                member = await get_inv_data()

                await collected_unob(ctx.author)
                add_item = await get_unob_data()

                user = ctx.author
    
                unobtainable_item = ["Frostbite", "Fagdfaust IV", "Coroller", "Vertigo", "RGB", "Disintegrator", "Anti-matter", "Exotic", "Scouts Honor", "Moonfeather", "Ghostie", "Eternal Frost", "Keeper Of The Deep", "Flying Dutchman", "Assault Drone", "Deep Space", "Mysterious Orb", "Bruisegg", "ZENITH", "Esper", "Forbidden Tome", "ESPER", "Attack Drone", "DOS Armour", "DOS", "DOS Walker", "DOS Belt", "Devourer Of Souls"]
                choice_item = random.choice(unobtainable_item)
                await ctx.send(f"<a:spin:1243478409930080342> Congrats you hit the bingo, you spun out: {choice_item}")

                member[str(user.id)]["Unobtainable"] += 1
                with open("inventory.json",'w') as f:
                    json.dump(member,f)

                if choice_item == "Frostbite":
                    add_item[str(user.id)]["Frostbite"] += 1
                    with open("unob.json",'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "Fagdfaust IV":
                    add_item[str(user.id)]["Fagdfaust IV"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "Coroller":
                    add_item[str(user.id)]["Coroller"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "Vertigo":
                    add_item[str(user.id)]["Vertigo"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "RGB":
                    add_item[str(user.id)]["RGB"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "Disintegrator":
                    add_item[str(user.id)]["Disintegrator"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "Anti-matter":
                    add_item[str(user.id)]["Anti-matter"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "Exotic":
                    add_item[str(user.id)]["Exotic"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "Scouts Honor":
                    add_item[str(user.id)]["Scouts Honor"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "Moonfeather":
                    add_item[str(user.id)]["Moonfeather"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "Ghostie":
                    add_item[str(user.id)]["Ghostie"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "Eternal Frost":
                    add_item[str(user.id)]["Eternal Frost"] += 1
                    with open("unob.json", 'w') as f:
                       json.dump(add_item,f)
                elif choice_item == "Keeper Of The Deep":
                    add_item[str(user.id)]["Keeper Of The Deep"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "Flying Dutchman":
                    add_item[str(user.id)]["Flying Dutchman"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "Assault Drone":
                    add_item[str(user.id)]["Assault Drone"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "Deep Space":
                    add_item[str(user.id)]["Deep Space"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "Mysterious Orb":
                    add_item[str(user.id)]["Mysterious Orb"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "Bruisegg":
                    add_item[str(user.id)]["Bruisegg"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "ZENITH":
                    add_item[str(user.id)]["ZENITH"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "Esper":
                    add_item[str(user.id)]["Esper"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "Forbidden Tome":
                    add_item[str(user.id)]["Forbidden Tome"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "ESPER":
                    add_item[str(user.id)]["ESPER"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "Attack Drone":
                    add_item[str(user.id)]["Attack Drone"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "DOS Armour":
                    add_item[str(user.id)]["DOS Armour"] += 1
                    with open("unob.json", 'w') as f:
                       json.dump(add_item,f)
                elif choice_item == "DOS":
                    add_item[str(user.id)]["DOS"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "DOS Walker":
                    add_item[str(user.id)]["DOS Walker"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "DOS Belt":
                    add_item[str(user.id)]["Fagdfaust IV"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)
                elif choice_item == "Devourer Of Souls":
                    add_item[str(user.id)]["Devourer Of Souls"] += 1
                    with open("unob.json", 'w') as f:
                        json.dump(add_item,f)

            elif 11 <= i <= 60:
                await ctx.send("<a:spin:1243478409930080342> Congrats you spun out a contraband ")

                member[str(user.id)]["Contraband"] += 1
                with open("inventory.json",'w') as f:
                    json.dump(member,f)
            elif 61 <= i <= 300:
                await ctx.send("<a:spin:1243478409930080342> Congrats on a random relic item")

                member[str(user.id)]["Relic"] += 1
                with open("inventory.json",'w') as f:
                    json.dump(member,f)
            elif 301 <= i <= 1700:
                await ctx.send("<a:spin:1243478409930080342> You just wasted your time for a stupid legendary item")
    
                member[str(user.id)]["Legendary"] += 1
                with open("inventory.json",'w') as f:
                    json.dump(member,f)
            elif 1701 <= i <= 5200:
                await ctx.send("<a:spin:1243478409930080342> You spun some useless epic item")
    
                member[str(user.id)]["Epic"] += 1
                with open("inventory.json",'w') as f:
                    json.dump(member,f)
            else:
                await ctx.send("<a:spin:1243478409930080342> You got some trash rare item")
    
                member[str(user.id)]["Rare"] += 1
                with open("inventory.json",'w') as f:
                    json.dump(member,f)

    elif x <= 0:
        await ctx.send("Invalid number of spin.")

    elif x > 1000:
        await ctx.send("1000 is the spin cap.")

    else:
        if 500 > bal:
            await ctx.send("You are so poor that you dont have enough KR for 1 time spin <:LMAO:945539956066115594> ")

        elif 500*x > bal:
            await ctx.send(f"You only have enough KR for {bal//500} times spin !!")

        else:
            rewards = []

            member = await get_inv_data()

            users = await get_bank_data()

            user = ctx.author

            users[str(user.id)]["KR"] -= 500*x
            with open("bank.json",'w') as f:
                json.dump(users,f)

            index = 0

            while index < x:
                i = random.randint(1, 10000)
                if i == 1:
                    member[str(user.id)]["Nitro Basic ticket"] += 1
                    with open("inventory.json",'w') as f:
                        json.dump(member,f)

                    rewards.append("**Nitro Basic ticket**")

                elif 2 <= i <= 10:
                    await open_inv(ctx.author)
                    member = await get_inv_data()

                    await collected_unob(ctx.author)
                    add_item = await get_unob_data()

                    user = ctx.author
    
                    unobtainable_item = ["Frostbite", "Fagdfaust IV", "Coroller", "Vertigo", "RGB", "Disintegrator", "Anti-matter", "Exotic", "Scouts Honor", "Moonfeather", "Ghostie", "Eternal Frost", "Keeper Of The Deep", "Flying Dutchman", "Assault Drone", "Deep Space", "Mysterious Orb", "Bruisegg", "ZENITH", "Esper", "Forbidden Tome", "ESPER", "Attack Drone", "DOS Armour", "DOS", "DOS Walker", "DOS Belt", "Devourer Of Souls"]
                    choice_item = random.choice(unobtainable_item)

                    member[str(user.id)]["Unobtainable"] += 1
                    with open("inventory.json",'w') as f:
                        json.dump(member,f)

                    rewards.append(f"**{choice_item}**")

                    if choice_item == "Frostbite":
                        add_item[str(user.id)]["Frostbite"] += 1
                        with open("unob.json",'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "Fagdfaust IV":
                        add_item[str(user.id)]["Fagdfaust IV"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "Coroller":
                        add_item[str(user.id)]["Coroller"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "Vertigo":
                        add_item[str(user.id)]["Vertigo"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "RGB":
                        add_item[str(user.id)]["RGB"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "Disintegrator":
                        add_item[str(user.id)]["Disintegrator"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "Anti-matter":
                        add_item[str(user.id)]["Anti-matter"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "Exotic":
                        add_item[str(user.id)]["Exotic"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "Scouts Honor":
                        add_item[str(user.id)]["Scouts Honor"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "Moonfeather":
                        add_item[str(user.id)]["Moonfeather"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "Ghostie":
                        add_item[str(user.id)]["Ghostie"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "Eternal Frost":
                        add_item[str(user.id)]["Eternal Frost"] += 1
                        with open("unob.json", 'w') as f:
                           json.dump(add_item,f)

                    elif choice_item == "Keeper Of The Deep":
                        add_item[str(user.id)]["Keeper Of The Deep"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "Flying Dutchman":
                        add_item[str(user.id)]["Flying Dutchman"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "Assault Drone":
                        add_item[str(user.id)]["Assault Drone"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "Deep Space":
                        add_item[str(user.id)]["Deep Space"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "Mysterious Orb":
                        add_item[str(user.id)]["Mysterious Orb"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "Bruisegg":
                        add_item[str(user.id)]["Bruisegg"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "ZENITH":
                        add_item[str(user.id)]["ZENITH"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "Esper":
                        add_item[str(user.id)]["Esper"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "Forbidden Tome":
                        add_item[str(user.id)]["Forbidden Tome"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "ESPER":
                        add_item[str(user.id)]["ESPER"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "Attack Drone":
                        add_item[str(user.id)]["Attack Drone"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "DOS Armour":
                        add_item[str(user.id)]["DOS Armour"] += 1
                        with open("unob.json", 'w') as f:
                           json.dump(add_item,f)

                    elif choice_item == "DOS":
                        add_item[str(user.id)]["DOS"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "DOS Walker":
                        add_item[str(user.id)]["DOS Walker"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "DOS Belt":
                        add_item[str(user.id)]["DOS Belt"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                    elif choice_item == "Devourer Of Souls":
                        add_item[str(user.id)]["Devourer Of Souls"] += 1
                        with open("unob.json", 'w') as f:
                            json.dump(add_item,f)

                elif 11 <= i <= 60:
                    member[str(user.id)]["Contraband"] += 1
                    with open("inventory.json",'w') as f:
                        json.dump(member,f)

                    rewards.append("Contraband")

                elif 61 <= i <= 300:
                    member[str(user.id)]["Relic"] += 1
                    with open("inventory.json",'w') as f:
                        json.dump(member,f)

                    rewards.append("Relic")

                elif 301 <= i <= 1700:
                    member[str(user.id)]["Legendary"] += 1
                    with open("inventory.json",'w') as f:
                        json.dump(member,f)

                    rewards.append("Legendary")

                elif 1701 <= i <= 5200:
                    member[str(user.id)]["Epic"] += 1
                    with open("inventory.json",'w') as f:
                        json.dump(member,f)

                    rewards.append("Epic")

                else:
                    member[str(user.id)]["Rare"] += 1
                    with open("inventory.json",'w') as f:
                        json.dump(member,f)

                    rewards.append("Rare")

                if index ==x:
                    break
                index += 1

            rare = 0
            epic = 0
            legend = 0
            relic = 0
            contra = 0

            rare_items = 0
            epic_items = 0
            legend_items = 0
            relic_items = 0
            contra_items = 0

            for items in rewards:
                if items == "Rare":
                    rare += 1
                elif items == "Epic":
                    epic += 1
                elif items == "Legendary":
                    legend += 1
                elif items =="Relic":
                    relic += 1
                elif items == "Contraband":
                    contra += 1
            while rare_items < rare:
                rewards.remove("Rare")
                if rare_items == rare:
                    break
                rare_items += 1
            while epic_items < epic:
                rewards.remove("Epic")
                if epic_items == epic:
                    break
                epic_items += 1
            while legend_items < legend:
                rewards.remove("Legendary")
                if legend_items == legend:
                    break
                legend_items += 1
            while relic_items < relic:
                rewards.remove("Relic")
                if relic_items == relic:
                    break
                relic_items += 1
            while contra_items < contra:
                rewards.remove("Contraband")
                if contra_items == contra:
                    break
                contra_items += 1
            await ctx.send(f"<a:spin:1243478409930080342> {ctx.author.name} spun out: Rare = {rare}, Epic = {epic}, Legendary = {legend}, Relic = {relic}, Contraband = {contra}, other: {rewards}")

@client.command()
async def use(ctx):
    await open_inv(ctx.author)

    ticket = await use_ticket(ctx.author)
    if 1 > ticket:
        await ctx.send("You dont have any ticket to use !!")
    else:
        member = await get_inv_data()

        user = ctx.author
        
        member[str(user.id)]["Nitro Basic ticket"] += -1
        with open("inventory.json",'w') as f:
            json.dump(member,f)
        await ctx.send(f"{ctx.author.name} use the Nitro Basic ticket, capture this message as a proof and DM PTJ for prize")

@client.command(aliases=['gift', 'donate'])
async def give(ctx,mention: discord.Member, amount :int):
    await open_account(mention)
    await open_account(ctx.author)

    bal = await update_bank(ctx.author)
    if amount > bal:
        await ctx.send("You dont have enough KR to gift !!")
    elif amount <= 0:
        await ctx.send("Illegal amount of KR  !!")
    else:
        gift = await get_bank_data()

        user = ctx.author

        await ctx.send(f"{ctx.author.name} give {mention}: {amount} KR")

        gift[str(user.id)]["KR"] -= amount
        with open("bank.json",'w') as f:
            json.dump(gift,f)

        gift[str(mention.id)]["KR"] += amount
        with open("bank.json",'w') as f:
            json.dump(gift,f)

@client.command()
@commands.has_role('*')
async def add(ctx, mention: discord.Member, amount: int):
    if amount < 0:
        await ctx.send("Invalid amount of KR")
    else:
        await open_account(mention)

        users = await get_bank_data()
    
        users[str(mention.id)]["KR"] += amount
        with open("bank.json",'w') as f:
            json.dump(users,f)
        
        await ctx.send(f"Add {amount} KR to {mention}'s balance")

@client.command()
@commands.has_role('*')
async def remove_KR(ctx, mention: discord.Member, amount: int):
    if amount < 0:
        await ctx.send("Invalid amount of KR")
    else:
        await open_account(mention)

        bal = await update_bank(mention)
        if amount >= bal:
            users = await get_bank_data()
    
            users[str(mention.id)]["KR"] -= bal
            with open("bank.json",'w') as f:
                json.dump(users,f)

            await ctx.send(f"Successful remove all {mention}'s KR")
        else:
            users = await get_bank_data()
    
            users[str(mention.id)]["KR"] -= amount
            with open("bank.json",'w') as f:
                json.dump(users,f)
        
            await ctx.send(f"Successful {amount} all {mention}'s KR")

@client.command()
async def lb(ctx):
    users = await get_bank_data()
    leader_board = {}
    total = []

    for user in users:
        name = int(user)
        amount = users[user]["KR"]
        leader_board[amount] = name
        total.append(amount)

    total = sorted(total, reverse= True)

    em = discord.Embed(title= f"Top 10 people with most KR:", color= discord.Color.red())
    i = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        name = member.name 
        em.add_field(name= f"{i}. {name}", value= f"{amt}", inline= False)    
        if i == 10:
            break
        else:
            i = i+1       
    await ctx.send(embed = em)

@client.command()
async def get_help(ctx):
    button1 = Button(label= "Commands", style= discord.ButtonStyle.primary)
    button2 = Button(label= "Chances", style= discord.ButtonStyle.primary)
    button3 = Button(label= "Source", style= discord.ButtonStyle.primary, url= "https://github.com/unoof/nknl-bot")
    button5 = Button(label= "Work", style= discord.ButtonStyle.primary)
    button6 = Button(label= "Beg / Search/ Rob", style= discord.ButtonStyle.primary)
    button7 = Button(label= "Spin", style= discord.ButtonStyle.primary)
    button_back1 = Button(label="❌", style= discord.ButtonStyle.primary)
    button_back2 = Button(label="go back", style= discord.ButtonStyle.primary)

    async def button_callback(interaction):
        if interaction.user == ctx.author:

            button1 = Button(label= "For fun", style= discord.ButtonStyle.primary)
            button_back2 = Button(label="go back", style= discord.ButtonStyle.primary)
            button2 = Button(label= "Main commands", style= discord.ButtonStyle.primary)
            button3 = Button(label= "Mod only", style= discord.ButtonStyle.primary)

            async def button_callback(interaction):
                if interaction.user == ctx.author:
                    em = discord.Embed(title = f"All fun command:", color = discord.Color.red())
                    em.add_field(name= "ptj_dumb", value="No CD", inline= False)
                    em.add_field(name= "ptj", value="No CD", inline= False)
                    em.add_field(name= "oof", value="No CD", inline= False)
                    em.add_field(name= "speczy", value="No CD", inline= False)
                    em.add_field(name= "penis",  value="5 minutes CD", inline= False)

                    view = View()
                    view.add_item(button_back2)
                    await interaction.response.edit_message(embed = em, view = view)
                else:
                    await interaction.response.send_message("You can not click this button !!", ephemeral=True)
            button1.callback = button_callback

            async def button_callback(interaction):
                if interaction.user == ctx.author:
                    em = discord.Embed(title = f"All main command:", color = discord.Color.red())
                    em.add_field(name= "balance", value="Leave blank to check your self or @user/user_id to get someone else balance", inline= False)
                    em.add_field(name= "inv", value="Leave blank to check your self or @user/user_id to get someone else inv", inline= False)
                    em.add_field(name= "work", value="10 mins cooldown", inline= False)
                    em.add_field(name= "beg", value="15 secs cooldown", inline= False)
                    em.add_field(name= "search", value="15 secs cooldown", inline= False)
                    em.add_field(name= "rob", value="3 mins cooldown", inline= False)
                    em.add_field(name= "toss + (kr you want to bet)", value="chance to x2 the bet", inline= False)
                    em.add_field(name= "dice + (kr you want to bet)", value="Chance to x9 the bet", inline= False)
                    em.add_field(name= "give/gift/donate + @user/userid + (amount)", value= "to give somebody any amount of KR", inline= False)
                    em.add_field(name= "spin + (number of spin)", value="500 KR per spin", inline= False)
                    em.add_field(name= "use", value= "use a Nitro Basic ticket", inline= False)

                    view = View()
                    view.add_item(button_back2)
                    await interaction.response.edit_message(embed = em, view = view)
                else:
                    await interaction.response.send_message("You can not click this button !!", ephemeral=True)
            button2.callback = button_callback

            async def button_callback(interaction):
                if interaction.user == ctx.author:
                    em = discord.Embed(title = f"All mod only command:", color = discord.Color.red())
                    em.add_field(name= "add + @user/userid + (amount of kr)", value= "To add some kr to other balance  (only high mod can use this)", inline= False)
                    em.add_field(name= "remove_KR + @user/userid + (number)", value= "To remove an amount of kr  (only high mod can use this)")
                    em.add_field(name= "warning", value= "Leave blank to check your self or @user/user_id to get someone else warning", inline= False)
                    em.add_field(name= "warn + @user/userid + (reason)", value= "Use to warn people", inline= False)
                    em.add_field(name= "remove + @user/userid + (number)", value= "Remove somebody warn, leave space to remove 1", inline= False)
                    em.add_field(name= "remove_all + @user/userid", value= "Remove all somebody warns", inline= False)

                    view = View()
                    view.add_item(button_back2)
                    await interaction.response.edit_message(embed = em, view = view)
                else:
                    await interaction.response.send_message("You can not click this button !!", ephemeral=True)
            button3.callback = button_callback

            async def button_callback(interaction):
                if interaction.user == ctx.author:
                    em = discord.Embed(title = f"All command type:", color = discord.Color.red())

                    view = View()
                    view.add_item(button1)
                    view.add_item(button2)
                    view.add_item(button3)
                    view.add_item(button_back1)
                    await interaction.response.edit_message(embed = em, view = view)
                else:
                    await interaction.response.send_message("You can not click this button !!", ephemeral=True)
            button_back2.callback = button_callback

            em = discord.Embed(title = f"All command type:", color = discord.Color.red())

            view = View()
            view.add_item(button_back1)
            view.add_item(button1)
            view.add_item(button2)
            view.add_item(button3)
            await interaction.response.edit_message(embed = em, view = view)
        else:
            await interaction.response.send_message("You can not click this button !!", ephemeral=True)
    button1.callback = button_callback

    async def button_callback(interaction):
        if interaction.user == ctx.author:

            async def button_callback(interaction):
                if interaction.user == ctx.author:
                    em = discord.Embed(title = f"Work chance:", color = discord.Color.red())
                    em.add_field(name= "Random", value="500 - 1500")
                    view = View()
                    view.add_item(button_back2)
                    await interaction.response.edit_message(embed = em, view = view)
                else:
                    await interaction.response.send_message("You can not click this button !!", ephemeral=True)
            button5.callback = button_callback
            
            async def button_callback(interaction):
                if interaction.user == ctx.author:
                    em = discord.Embed(title = f"Beg / search/ rob chance:", color = discord.Color.red())
                    em.add_field(name= "0 kr", value="20%", inline= False)
                    em.add_field(name= "20 - 30 kr", value="45%", inline= False)
                    em.add_field(name= "31 - 50 kr", value="20%", inline= False)
                    em.add_field(name= "51 - 100 kr", value="10%", inline= False)
                    em.add_field(name= "101 - 150 kr", value="4,9%", inline= False)
                    em.add_field(name= "151 - 500 kr", value="0,1%", inline= False)
                    view = View()
                    view.add_item(button_back2)
                    await interaction.response.edit_message(embed = em, view = view)
                else:
                    await interaction.response.send_message("You can not click this button !!", ephemeral=True)
            button6.callback = button_callback

            async def button_callback(interaction):
                if interaction.user == ctx.author:
                    em = discord.Embed(title = f"Spin chance:", color = discord.Color.red())
                    em.add_field(name= "Rare item", value="48%", inline= False)
                    em.add_field(name= "Epic item", value="35%", inline= False)
                    em.add_field(name= "Legendary item", value="14%", inline= False)
                    em.add_field(name= "Relic item", value="2,4%", inline= False)
                    em.add_field(name= "Contraband item", value="0,5%", inline= False)
                    em.add_field(name= "Unobtainable item", value="0,09%", inline= False)
                    em.add_field(name= "Nitro Basic ticket", value="0,01%", inline= False)
                    view = View()
                    view.add_item(button_back2)
                    await interaction.response.edit_message(embed = em, view = view)
                else:
                    await interaction.response.send_message("You can not click this button !!", ephemeral=True)
            button7.callback = button_callback

            async def button_callback(interaction):
                if interaction.user == ctx.author:
                    view = View()
                    view.add_item(button_back1)
                    view.add_item(button5)
                    view.add_item(button6)
                    view.add_item(button7)
                    em = discord.Embed(title = f"Check the chance of these commands:", color = discord.Color.red())
                    await interaction.response.edit_message(embed = em, view = view)
                else:
                    await interaction.response.send_message("You can not click this button !!", ephemeral=True)
            button_back2.callback = button_callback

            view = View()
            view.add_item(button_back1)
            view.add_item(button5)
            view.add_item(button6)
            view.add_item(button7)
            em = discord.Embed(title = f"Check the chance of these commands:", color = discord.Color.red())
            await interaction.response.edit_message(embed = em, view = view)
        else:
            await interaction.response.send_message("You can not click this button !!", ephemeral=True)
    button2.callback= button_callback

    async def button_callback(interaction):
        if interaction.user == ctx.author:
            view = View()
            view.add_item(button1)
            view.add_item(button2)
            view.add_item(button3)
            em = discord.Embed(title = f"Get your help:", color = discord.Color.red())
            em.add_field(name= "Preflix", value="!")
            await interaction.response.edit_message(embed = em, view = view)
        else:
            await interaction.response.send_message("You can not click this button !!", ephemeral=True)
    button_back1.callback = button_callback

    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    em = discord.Embed(title = f"Get your help:", color = discord.Color.red())
    em.add_field(name= "Preflix", value="!")
    await ctx.send(embed = em, view = view)

@client.event
async def on_command_error(ctx, err):
    if err.__class__ is commands.MissingRole:
        await ctx.send(f'You dont have permission for this command !!!')
        return
    elif err.__class__ is commands.CommandOnCooldown:
        cd: int = int(err.retry_after)
        await ctx.send(f'The command is on cooldown, time left: **{cd//86400}d {(cd//3600)%24}h {(cd//60)%60}m {cd % 60}s**.')
        return

client.run(token)
#authorize: https://discord.com/oauth2/authorize?client_id=1240319216930918511&permissions=581652796549239&scope=bot
