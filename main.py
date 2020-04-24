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



def fetch_flags():
    flag_keyss = open("settings/flagKeys.txt","r")
    flag_valss = open("settings/flagVals.txt", "r")
    flag_keys = flag_keyss.readlines()
    flag_vals = flag_valss.readlines()
    flags = {}

    for i in range(len(flag_keys)):
        flags[flag_keys[i].strip()] = bool(int(flag_vals[i].strip()))

    flag_keyss.close()
    flag_valss.close()

    return flags



def fetch_cuses():
    f = open("general/cuses.txt", "r")
    foo = f.readlines()
    listlol = []   
    f.close()
    for i in foo:
        listlol.append(i.strip())

    return listlol


def save_file(filename):
    f = open(filename, "r")
    lines = []
    for i in range(len(f.readlines())):
        lines[i] = f.readlines()[i].strip()
    f.close()
    return lines    




def update_flags():
    #There is prob a better and quicker way to do this but il do it later
    flag_keyss = open("settings/flagKeys.txt","w")
    flag_valss = open("settings/flagVals.txt", "w")
    write_key = ""
    write_val = ""
    for i in flags:
        write_key += i+"\n"
        if flags[i]:
            write_val += "1\n"
        else:
            write_val += "0\n"
    flag_keyss.write(write_key)
    flag_valss.write(write_val)

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
bad_words = fetch_cuses()
raw_channels = {"general":702792879772401677, "bot":702794344087814247, "commands": 702794305919647766, "welcome": 702844875888132096, "announcements": 702845142087892992}
ggs = ["gg bois we did it", "yeah boiiii", "ok nice", "gg", "gg", "gg", "lol nice gg"]
songs = ["https:!!www.youtube.com!watch?v=rNZ7r8pM37k", "https:!!www.youtube.com!watch?v=sBugnmrF3G8"]
f = open("roles/mods.txt", "r")
mods = [i.strip() for i in f.readlines()]
#========== Main Vars  END ===========#

#========== Main Flags ===========#

flags = fetch_flags()


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

    if message.author == client.user and flags["ignoreBots"]:
            return


    if message.content.split()[0] == "/flag":
        if str(message.author) in mods:
            if message.content == "/flag":
                pass


            if len(message.content.split()) == 2:
            
                if message.content.split()[1] in flags:
                    
                    await message.channel.send(str(flags[message.content.split()[1]])) 

                else:
                    await message.channel.send(f"There is no such flag named [{message.content.split()[1]}]")

            elif len(message.content.split()) == 3:
                if message.content.split()[1] in flags:

                    if message.content.split()[2].lower() == "true":
                        flags[message.content.split()[1]] = True
                        
                        await message.channel.send(f"Updated {message.content.split()[1]} to {flags[message.content.split()[1]]}")

                    elif message.content.split()[2].lower() == "false":
                        flags[message.content.split()[1]] = False
                        await message.channel.send(f"Updated {message.content.split()[1]} to {flags[message.content.split()[1]]}")

                    else:
                        await message.channel.send(f"{message.content.split()[2]} is not a boolean")
                else:
                    await message.channel.send(f"There is no such flag named [{message.content.split()[1]}]")
        else:
            await message.channel.send("You are not authorized to perform this command")
        update_flags()


    if flags["botEnabled"]:
        
        global messages
        messages += 1

       

        if flags["blockCurses"]:
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