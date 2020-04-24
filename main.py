#CHECK DISCORD SERVER FOR UPDATES
#CHECK DISCORD SERVER FOR UPDATES
#CHECK DISCORD SERVER FOR UPDATES
#CHECK DISCORD SERVER FOR UPDATES
#CHECK DISCORD SERVER FOR UPDATES
#CHECK DISCORD SERVER FOR UPDATES
import os

import discord,random
from discord.ext import commands
import time, asyncio

#========== Main Functions ===========#

def cler():
  print("\x1b[2J\x1b[H",end="")

token = os.getenv('TOKEN')
#def load_token():
#    f = open("?????", "r")
#    token = f.readlines()[0].strip()
#    f.close()
#    return token

#========== Main Functions END ===========#

#========== Main Vars  ===========#

messages = joined = 0
#token = load_token()
img_root = "/images/"
client = discord.Client()
cler()
guild = client.get_guild(702792879772401674)
channels = ["commands", "bot"]
bad_words = ["fuck", "shit", "bitch"]
raw_channels = {"general":702792879772401677, "bot":702794344087814247, "commands": 702794305919647766, "welcome": 702844875888132096, "announcements": 702845142087892992}
ggs = ["gg bois we did it", "yeah boiiii", "ok nice", "gg", "gg", "gg", "lol nice gg"]
songs = ["https:!!www.youtube.com!watch?v=rNZ7r8pM37k", "https:!!www.youtube.com!watch?v=sBugnmrF3G8"]
f = open("roles/mods.txt", "r")
mods = [i.strip() for i in f.readlines()]
#========== Main Vars  END ===========#

#========== Main Flags ===========#

flags = {"ignoreBots" : True, "cursesBlocked": True, "addComments": True, "botEnabled": True}


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.channel.send(
        f'Hi {member.name}! Welcome to the server!'
    )

#========== Main Flags END ===========#



#========== Message Beggin ===========#
@client.event
async def on_message(message):


    if message.author in mods:
        if len(message.content.split()) == 2:
            return 
        if message.content.split()[0] == "/flag":
            pass


    if flags["botEnabled"]:
        
        global messages
        messages += 1

        if message.author == client.user and flags["ignoreBots"]:
            return

        if flags["cursesBlocked"]:
            for word in bad_words:
                if message.content.count(word) > 0 and message.author not in mods:
                    print(f"A bad word was said by [  {message.author}] - [{message.content}]")
                    await message.channel.purge(limit=1)

        if flags["addComments"]:
            if message.content.find("gg") != -1:
                await message.channel.send("gg")
            
            
            elif message.content.lower() == 'f' or "fs" in  message.content:
                response = "f"
                await message.channel.send(response)
    for i in bad_words:
      if(i in message.content.lower()):
        message.delete()


    #THE BIT BELOW ME NEEDS DEEPER FILTERING... DO IT LATER
    #THE BIT BELOW ME NEEDS DEEPER FILTERING... DO IT LATER
    #THE BIT BELOW ME NEEDS DEEPER FILTERING... DO IT LATER
    #THE BIT BELOW ME NEEDS DEEPER FILTERING... DO IT LATER
    #THE BIT BELOW ME NEEDS DEEPER FILTERING... DO IT LATER
    #   if str(message.channel) not in channels:# and str(message.author) not in valid_users:
    #        if "/" in message.content:
    #            print(f"""User: {message.author} tried to do command [{message.content}] in channel [{message.channel}]""")
    #        return





    #========== Message END ===========#
client.run(token)