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

client  =  commands.Bot(command_prefix = '!', intents=intents, help_command= None)              #bot preflix

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

@client.command()
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
        button1.callback = button_callback

        async def button_callback(interaction):
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
        button2.callback = button_callback

        view = View()
        view.add_item(button1)
        view.add_item(button2)
        em = discord.Embed(title = f"Chose one for chance to x2 the kr you bet:", color = discord.Color.red())
        await ctx.send(embed = em, view = view)

@client.command()
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
        button1.callback = button_callback

        async def button_callback(interaction):
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
        button2.callback = button_callback

        async def button_callback(interaction):
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
        button3.callback = button_callback

        async def button_callback(interaction):
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
        button4.callback = button_callback

        async def button_callback(interaction):
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
        button5.callback = button_callback

        async def button_callback(interaction):
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
        button6.callback = button_callback

        async def button_callback(interaction):
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
        button7.callback = button_callback

        async def button_callback(interaction):
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
        button8.callback = button_callback

        async def button_callback(interaction):
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
            await ctx.send(f"<a:spin:1243478409930080342> Congratulation, {ctx.author.name} won the jackpot prize: a basic nitro ticket")
        elif 2 <= i <= 10:
            unobtainable_item = [" Frostbite", " Fagdfaust IV", " Coroller", " Vertigo", " RGB", " Disintegrator", " Anti-matter", " Exotic", " Scouts Honor", " Moonfeather", " Ghostie", " Eternal Frost", " Keeper Of The Deep", " Flying Dutchman", " Assault Drone", " Deep Space", " Mysterious Orb", " Bruisegg", " ZENITH", " Esper", " Forbidden Tome", " ESPER", " Attack Drone", " DOS Armour", " DOS", " DOS Walker", " DOS Belt", " Devourer Of Souls"]
            await ctx.send(f"<a:spin:1243478409930080342> Congrats {ctx.author.name} hit the bingo, you spun out:" + random.choice(unobtainable_item))
        elif 11 <= i <= 60:
            await ctx.send(f"<a:spin:1243478409930080342> Congrats {ctx.author.name} spun out a contraband ")
        elif 61 <= i <= 300:
            await ctx.send("<a:spin:1243478409930080342> Congrats on a random relic item")
        elif 301 <= i <= 1700:
            await ctx.send("<a:spin:1243478409930080342> You just wasted your time for a stupid legendary item")
        elif 1701 <= i <= 5200:
            await ctx.send("<a:spin:1243478409930080342> You spun some useless epic item")
        else:
            await ctx.send("<a:spin:1243478409930080342> You got some trash rare item")

@client.command()
async def get_help(ctx):
    button1 = Button(label= "Commands", style= discord.ButtonStyle.primary)
    button2 = Button(label= "Chances", style= discord.ButtonStyle.primary)
    button3 = Button(label= "Source", style= discord.ButtonStyle.primary, url= "https://github.com/unoof/nknl-bot")
    button5 = Button(label= "Work", style= discord.ButtonStyle.primary)
    button6 = Button(label= "Beg / Search", style= discord.ButtonStyle.primary)
    button7 = Button(label= "Spin", style= discord.ButtonStyle.primary)
    button_back1 = Button(label="↩", style= discord.ButtonStyle.primary)
    button_back2 = Button(label="↩", style= discord.ButtonStyle.primary)

    async def button_callback(interaction):
        em = discord.Embed(title = f"All command:", color = discord.Color.red())
        em.add_field(name= "ptj_dump", value="No CD")
        em.add_field(name= "ptj", value="No CD")
        em.add_field(name= "oof", value="No CD")
        em.add_field(name= "speczy", value="No CD")
        em.add_field(name= "balance", value="Leave blank to check your self or @user/user_id to get someone else balance")
        em.add_field(name= "work", value="10 mins cooldown")
        em.add_field(name= "beg", value="15 secs cooldown")
        em.add_field(name= "search", value="15 secs cooldown")
        em.add_field(name= "toss + (kr you want to bet)", value="chance to x2 the bet")
        em.add_field(name= "dice + (kr you want to bet)", value="Chance to x9 the bet")
        em.add_field(name= "spin", value="500 KR per spin")
        view = View()
        view.add_item(button_back1)
        await interaction.response.edit_message(embed = em, view = view)
    button1.callback = button_callback

    async def button_callback(interaction):

        async def button_callback(interaction):
            em = discord.Embed(title = f"Work chance:", color = discord.Color.red())
            em.add_field(name= "Random", value="500 - 1500")
            view = View()
            view.add_item(button_back2)
            await interaction.response.edit_message(embed = em, view = view)
        button5.callback = button_callback
        async def button_callback(interaction):
            em = discord.Embed(title = f"Beg / search chance:", color = discord.Color.red())
            em.add_field(name= "0 kr", value="20%")
            em.add_field(name= "20 - 30 kr", value="45%")
            em.add_field(name= "31 - 50 kr", value="20%")
            em.add_field(name= "51 - 100 kr", value="10%")
            em.add_field(name= "101 - 150 kr", value="4,9%")
            em.add_field(name= "151 - 500 kr", value="0,1%")
            view = View()
            view.add_item(button_back2)
            await interaction.response.edit_message(embed = em, view = view)
        button6.callback = button_callback

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
            view.add_item(button_back2)
            await interaction.response.edit_message(embed = em, view = view)
        button7.callback = button_callback

        async def button_callback(interaction):
            view = View()
            view.add_item(button5)
            view.add_item(button6)
            view.add_item(button7)
            view.add_item(button_back1)
            em = discord.Embed(title = f"Check the chance of these commands:", color = discord.Color.red())
            await interaction.response.edit_message(embed = em, view = view)
        button_back2.callback = button_callback

        view = View()
        view.add_item(button5)
        view.add_item(button6)
        view.add_item(button7)
        view.add_item(button_back1)
        em = discord.Embed(title = f"Check the chance of these commands:", color = discord.Color.red())
        await interaction.response.edit_message(embed = em, view = view)
    button2.callback= button_callback

    async def button_callback(interaction):
        view = View()
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)
        em = discord.Embed(title = f"Get your help:", color = discord.Color.red())
        await interaction.response.edit_message(embed = em, view = view)
    button_back1.callback = button_callback

    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    em = discord.Embed(title = f"Get your help:", color = discord.Color.red())
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
