import colorama, json, requests, threading, time, sys, os
from colorama import Fore, Back, Style
from modules import capmonster, invites, tokens, session
from colorama import Fore
import discord


thread_lock = threading.Lock()
printNumber = 0



with open('config.json', 'r') as config_file:
    config = json.load(config_file)

class Console:
    """Console utils"""

    @staticmethod
    def _time():
        return time.strftime("%H:%M:%S", time.gmtime())

    @staticmethod
    def clear():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def sprint(content: str, status: bool = True) -> None:
        thread_lock.acquire()
        sys.stdout.write(
            f"{Fore.LIGHTBLACK_EX}{Console()._time()} |{Fore.RESET} {Fore.LIGHTGREEN_EX if status else Fore.RED}{content}"
            + "\n"
            + Fore.RESET
        )
        thread_lock.release()
        global printNumber
        printNumber += 1

import json

# Read the config file
try:
    with open("config.json") as file:
        config = json.load(file)
except FileNotFoundError:
    print("Config file not found!")
    exit()

# Check for errors in the config file
if "token" not in config:
    print("Incorrect error from the config file: 'token' key not found!")
elif "guildid" not in config:
    print("Incorrect error from the config file: 'guildid' key not found!")
else:
    print("Config file checked successfully!")



Console().clear()


webhook_url = config["webhook"]

embed = {
    "content": f"@everyone valhala",
    "title": "valhalla lvl 1",
    "description": f"The tool is ready to snipe!",
    "color": 16711680,  # Red color
    "avatar_url": "https://images-ext-1.discordapp.net/external/PMVgfiGE7ShxALuCFDFIXdP56NypNgP5MNdtpmcfJ7s/https/i.pinimg.com/564x/e7/23/e5/e723e5b052c95283022e816475e1371f.jpg?width=421&height=415",
    "image" : "https://media.tenor.com/RFOd5ssQMyIAAAAd/blood-magnus-bruun.gif",
}

payload = {
    "embeds": [embed]
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
print(f'''{Fore.CYAN}

           __     __     _      _       _   _      _      _       _          _    
           \ \   / /    / \    | |     | | | |    / \    | |     | |        / \   
            \ \ / /    / _ \   | |     | |_| |   / _ \   | |     | |       / _ \  
             \ V /    / ___ \  | |___  |  _  |  / ___ \  | |___  | |___   / ___ \ 
              \_/    /_/   \_\ |_____| |_| |_| /_/   \_\ |_____| |_____| /_/   \_\                              
                                    

                                      #1 sniper-]]
       
''')
class VanityBot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user.name} ({self.user.id})')
print
printNumber += 1
token = config["token"]
printNumber += 1
guildid = config["guildid"]
printNumber += 1
vanities = open("list.txt", "r").read().splitlines()
printNumber += 1
delay = 0
printNumber += 1
 

token = tokens.formatToken(token)

if tokens.validateToken(token) == False:
    Console().sprint(f"{Fore.WHITE}({Fore.RED}-{Fore.WHITE}) [{Fore.RED}{printNumber}{Fore.WHITE}] {Fore.CYAN}Invalid token, please restart the program and try again.", False)
    time.sleep(0)
    sys.exit()

try:
    delay = int(delay)
except:
    Console().sprint(f"{Fore.WHITE}({Fore.RED}-{Fore.WHITE}) [{Fore.RED}{printNumber}{Fore.WHITE}] {Fore.CYAN}Invalid delay, please restart the program and try again.", False)
    time.sleep(0)
    sys.exit()

webhook = config["webhook"]
headers, _ = tokens.get_headers(token)
client = session.getTlsClient()
client.headers.update(headers)
response = client.get(f'https://discord.com/api/v10/guilds/{guildid}')
if response.status_code != 200:
    Console().sprint(f"{Fore.WHITE}({Fore.RED}+{Fore.WHITE}) [{Fore.RED}{printNumber}{Fore.WHITE}] {Fore.CYAN}Invalid guild id, please restart the program and make sure you are in the guild.", False)
    time.sleep(0)
    sys.exit()

snipedInvite = False

# Assuming you have the necessary imports and variables defined
import time

start_time = time.time()

# Your sniping code here

end_time = time.time()
discord_ms = round((end_time - start_time) * 1000, 2)


while snipedInvite == False:
    for vanity in vanities:
        req = client.get(f'https://discord.com/api/v10/invites/{vanity}?inputValue={vanity}&with_counts=true&with_expiration=true').text
        if 'type' in req:
            members = json.loads(req)['approximate_member_count']
            boosts = json.loads(req)['guild']['premium_subscription_count']
            if int(boosts) < 14:
                boosts = f"{boosts} (Partnered Server)"
            Console().sprint(f"{Fore.WHITE}({Fore.RED}-{Fore.WHITE}) [{Fore.RED}{printNumber}{Fore.WHITE}] {Fore.RED}{vanity} {Fore.CYAN}is taken {Fore.LIGHTBLACK_EX}| {Fore.CYAN}Members: {Fore.LIGHTBLACK_EX}{members} {Fore.CYAN}| Boosts: {Fore.LIGHTBLACK_EX}{boosts} {Fore.CYAN}Status: {Fore.LIGHTBLACK_EX}{response.status_code}",False)
        else:
            request = client.patch(f'https://discord.com/api/v9/guilds/{guildid}/vanity-url', json={"code": vanity})
            if request.status_code == 200:
                snipedInvite = True
                Console().sprint(f"{Fore.WHITE}({Fore.GREEN}+{Fore.WHITE}) [{Fore.GREEN}{printNumber}{Fore.WHITE}] {Fore.CYAN}Successfully sniped discord.gg/{vanity}", True)
send = {
    "content": f"@everyone {vanity}",
    "username": "valhalla lvl 1",
    "avatar_url": "https://images-ext-1.discordapp.net/external/PMVgfiGE7ShxALuCFDFIXdP56NypNgP5MNdtpmcfJ7s/https/i.pinimg.com/564x/e7/23/e5/e723e5b052c95283022e816475e1371f.jpg?width=421&height=415",
    "embeds": [
        {
            "title": "Vanity Sniped",
            "fields": [
                {"name": "**vanity**", "value": vanity},
                {"name": "**guildid**", "value": guildid},
                {"name": "**speed**", "value": f"{discord_ms} ms"},
                {"name": "**source**", "value": "keep sniping :)"}
            ],
            "color": int('2c2d31', 16),
            "image": {"url": "https://media.tenor.com/MbvDrB63TcgAAAAC/viking-ship.gif"}
        }
    ]
}


requests.post(webhook, json=send)

if snipedInvite:
    # Change guild name to ".gg/" followed by the sniped vanity
    guild_name = f".gg/{vanity}"
    client.patch(f'https://discord.com/api/v9/guilds/{guildid}', json={"name": guild_name})

input("\n\nPress enter to exit...")