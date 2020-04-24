#HEY how will we add the token without revealing it

import os

import discord,random
from discord.ext import commands
import time, asyncio

#Things to add:
#Author/Channel Filters
#commands -  /diguise
#
#

#============= Init =============#
messages = joined = 0

def cler():
  print("\x1b[2J\x1b[H",end="")

def load_token():
    f = open("/home/HIDDEN/Codes/Py/Discord_Bot/token.txt", "r")
    token = f.readlines()[0].strip()
    f.close()
    return token

    
    
    
#id = 543728441359597578
token = load_token()
img_root = "/home/HIDDEN/Codes/Py/Discord_Bot/images/"
client = discord.Client()
cler()

#============= Finished =============#


#============= Main =============#


#============= Stats =============#
async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("/home/HIDDEN/Codes/Py/Discord_Bot/stats.txt", "a") as f:
                f.write(f"Time: [{int(time.time())}], Messages: [{messages}], Members Joined: [{joined}]\n")
                
            messages = 0
            joined = 0
            
            await asyncio.sleep(300)
        except Exception as e:
            print(e)
            await asyncio.sleep(300)
            

#============= Stats finished =============#


#============= Anti stuff =============#

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.channel.send(
        f'Hi {member.name}, Idk how u giut here but stay here if u want!'
    )


@client.event
async def on_member_update(before, after):
    n = after.nick
    if n:
        if n.lower().count("HIDDEN") > 0:
            last = before.nick
            if last:
                await after.edit(nick=last)
            else:
                await after.edit(nick="")

#============= anti finished =============#


#============= Greetings =============#

@client.event
async def on_member_join(memeber):
    global joined
    joined += 1
    for channel in memeber.guild.channels:
        if str(channel) == "general":
            await channel.send(f"""Welcome to the server {memeber.mention}!""")

#============= Greeting finished =============#


#============= On message =============#

@client.event
async def on_message(message):
    
    global messages
    messages += 1
    
    #============= Gen =============#
    
    guild = client.get_guild(700277626857586758)
    channels = ["commands", "bot"]
    bad_words = ["fuck", "shit", "bitch"]
    raw_channels = {"general":700277626857586761, "bot":701170697745203290}
    ggs = ["gg bois we did it", "yeah boiiii", "ok nice", "gg", "gg", "gg", "lol nice gg"]
    songs = ["https:!!www.youtube.com!watch?v=rNZ7r8pM37k", "https:!!www.youtube.com!watch?v=sBugnmrF3G8"]
    
    #============= Gen finished =============#
    
    
    #============= Checks =============#
    
    if message.author == client.user:
        return
    
    
    
    
    for word in bad_words:
        if message.content.count(word) > 0 and message.author not in mods:
            print(f"A bad word was said by [{message.author}] - [{message.content}]")
            await message.channel.purge(limit=1)
            
            
    
    if message.content.find("gg") != -1:
        await message.channel.send("gg")
         
        
    elif message.content.lower() == 'f' or "fs" in message.content:
        response = "f"
        await message.channel.send(response)           
            
            
    
    if str(message.channel) not in channels:# and str(message.author) not in valid_users:
        if "/" in message.content:
            print(f"""User: {message.author} tried to do command [{message.content}] in channel [{message.channel}]""")
        return
    
    #============= Checks finished =============#
    
    
    #============= Public =============#
    if str(message.author) in mods:
        if "/echo" in message.content:
            split_message = message.content.split()
            if split_message[1] in raw_channels:
                
                message.channel = client.get_channel(raw_channels[split_message[1]])
                try:
                    for i in range(int(split_message[2])):
                        response = message.content[7+len(split_message[1])+len(split_message[2]):]
                        await message.channel.send(response) 
                except:
                    response = message.content[6+len(split_message[1]):]
                    await message.channel.send(response)
            else:
                response = message.content[6:]
                await message.channel.send(response)    

    if message.content == "/users":
        await message.channel.send(f"""Nº of Members:  {guild.member_count}""")
    
        
    elif "/rnum" in message.content:
        messag = message.content.split()
        try:
            minNum = int(messag[1])
            maxNum = int(messag[3])
            response = random.randint(minNum,maxNum)
        except:
            response = "/rnum [min-Munber] - [max-Number] || e.g. /rnum 1 -10"
        await message.channel.send(response)
        
    
    elif "/songs" == message.content:
        split_command = message.content.split()
        response = str(songs)
        await message.channel.send(response)
        
        
    elif message.content == "/meme":
        await message.channel.send(file=discord.File(img_root + random.choice(os.listdir(img_root))))
    #============= Public Finished =============#
    
    #============= Finale Check =============#    
        
    elif message.content == "/help":
        embed = discord.Embed(title="Help", description="Some useful commands")
        embed.add_field(name="/users", value="Shows you a the amount of users on this server")
        embed.add_field(name="/rnum", value="Returns a random number - /rnum [min-Munber] - [max-Number] || e.g. /rnum 1 -10")
        embed.add_field(name="/songs", value="Shows you a list of songs")
        embed.add_field(name="/meme", value="Shows you a random meme")
        if str(message.author) in mods:
            embed.add_field(name="/echo", value="The bot says what you want it to say ||  /echo Hi")
            
        await message.channel.send(content=None, embed=embed)

    #============= Finale Check Finished =============#
    
    
    
    #============= Private =============#
        
    
        
    #============= Private Finished =============#
        
        
    


#============= On message finished =============#


#============= Main finished =============#

client.loop.create_task(update_stats())
client.run(token)