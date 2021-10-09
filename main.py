import discord
from discord.channel import VoiceChannel
from discord.embeds import Embed
from discord.ext import commands
import random
import tracemalloc

client = commands.Bot(command_prefix=">")
tracemalloc.start()

@client.command()
async def team(ctx):
    old = []
    old1 = []
    x = ctx.author.voice.channel.voice_states
    if (ctx.author.voice):
        lm = x.keys()
        em = discord.Embed(title="Underrated Snipers",description="1️⃣ - Firing range \n 2️⃣ - Summit \n 3️⃣ - Standoff \n      4️⃣ - Crash \n 5️⃣ - Crossfire \n 6️⃣ - Raid \n 7️⃣ - Meltdown \n 8️⃣ - Nuketown")
        em.add_field(name="Team 1",value="")
        em.add_field(name="Team 2",value="")
        for i,j in enumerate(lm):
            if i%2==0:
                old.append("<@{}>".format(j))
            elif i%2!=0:
                old1.append("<@{}>".format(j))
        l1=str(old)
        l1 = l1.replace("['"," ")
        l1 = l1.replace("']"," ")
        l1 = l1.replace("'"," ")
        l2=str(old1)
        l2= l2.replace("['"," ")
        l2= l2.replace("']"," ")
        l2= l2.replace("'"," ")
        fx = l1.split(",")
        fx1 = l2.split(",")
        fx.extend(fx1)
        random.shuffle(fx)
        random.shuffle(fx)
        mid = len(fx)//2
        fx12 = fx[:mid]
        fx1 = fx[mid:]
        l1 = str(fx12)
        l2 = str(fx1)
        l1 = l1.replace("['"," ")
        l1 = l1.replace("']"," ")
        l1 = l1.replace("'"," ")
        l2= l2.replace("['"," ")
        l2= l2.replace("']"," ")
        l2= l2.replace("'"," ")
        l2= l2.replace(",","\n")
        l1 = l1.replace(",","\n")
        em.set_field_at(index=0,name="Team 1",value=l1)
        em.set_field_at(index=1,name="Team 2",value=l2) 
    
    msg = await ctx.send(embed=em)
    await msg.add_reaction("1️⃣")
    await msg.add_reaction("2️⃣")
    await msg.add_reaction("3️⃣")
    await msg.add_reaction("4️⃣")
    await msg.add_reaction("5️⃣")
    await msg.add_reaction("6️⃣")
    await msg.add_reaction("7️⃣")
    await msg.add_reaction("8️⃣")


client.run("ODk1ODYxNTgwMzI2MTA5MTg1.YV-uHQ.Pa6ZsNCQMY9V6_J7E0rpwYr9D1Y")