import os
import sys
import time
import webbrowser
import re
import colorama
from colorama import Fore
import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance




# Var
file_path = "hunteriosettings.txt"
key = None

# Func
try:
    with open(file_path, "r") as file:
        # Read the content of the file
        file_content = file.read()
        match = re.search(r'"([^"]*)"', file_content)
        if match:
            key = match.group(1)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"API key can't load, Make sure that you provided your hunter.io API key properly: {e}")

def printDetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f"IP Address: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")

# Main Script

def main():
    global onstart
    print(f"""
{Fore.MAGENTA}     ▄▄▄       ██▓███   ██░ ██ ▓█████  ██▓     ██▓ ▒█████    ██████ 
{Fore.MAGENTA}    ▒████▄    ▓██░  ██▒▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒▒██▒  ██▒▒██    ▒ 
{Fore.MAGENTA}    ▒██  ▀█▄  ▓██░ ██▓▒▒██▀▀██░▒███   ▒██░    ▒██▒▒██░  ██▒░ ▓██▄   
{Fore.MAGENTA}    ░██▄▄▄▄██ ▒██▄█▓▒ ▒░▓█ ░██ ▒▓█  ▄ ▒██░    ░██░▒██   ██░  ▒   ██▒
{Fore.MAGENTA}     ▓█   ▓██▒▒██▒ ░  ░░▓█▒░██▓░▒████▒░██████▒░██░░ ████▓▒░▒██████▒▒
{Fore.MAGENTA}     ▒▒   ▓▒█░▒▓▒░ ░  ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░░▓  ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
{Fore.MAGENTA}      ▒   ▒▒ ░░▒ ░      ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░ ▒ ░  ░ ▒ ▒░ ░ ░▒  ░ ░
{Fore.MAGENTA}      ░   ▒   ░░        ░  ░░ ░   ░     ░ ░    ▒ ░░ ░ ░ ▒  ░  ░  ░  
{Fore.MAGENTA}          ░  ░          ░  ░  ░   ░  ░    ░  ░ ░      ░ ░        ░  
{Fore.LIGHTBLUE_EX}
    [0] Exit                        [1] Email Verifier >Hunter.io
    [2] Domain Search >Hunter.io    [3] Email Finder >Hunter.io
    [4] IPv4 Track                  [5] Url Track
    [6] Email Listing               [7] Credits
{Fore.LIGHTMAGENTA_EX}
""")

    cmd = input("Aphelios@User>")

    if cmd == "0":
        sys.exit(0)
    if cmd == "1":
        print(f"This is your API key : ", key)
        email = input("Put Target's email >")
        webbrowser.open('https://api.hunter.io/v2/email-verifier?email='+email+'&api_key='+key)
        time.sleep(1)
        onstart()
    if cmd == "2":
        print(f"This is your API key : ", key)
        domain = input("Put Target's domain >")
        webbrowser.open('https://api.hunter.io/v2/domain-search?domain='+domain+'&api_key='+key)
        time.sleep(1)
        onstart()
    if cmd == "3":
        print(f"This is your API key : ", key)
        edomain = input("Put Target's Email Domain >")
        firstn = input("Put Target's First Name >")
        lastn = input("Put Target's Last Name >")
        webbrowser.open('https://api.hunter.io/v2/email-finder?domain='+edomain+'&first_name='+firstn+'&last_name='+lastn+'&api_key='+key)
        time.sleep(1)
        onstart()
    if cmd == "4":
        ip_add = input("Enter Target's IP: ") 
        printDetails(ip_add)
        print("Press Enter to Continue...")
        input()
        onstart()
    if cmd == "5":
        url = input("Enter URL: ") 
        ip_add = socket.gethostbyname(url)
        printDetails(ip_add)
        print("Press Enter to Continue...")
        input()
        onstart()
    if cmd == "7":
        webbrowser.open('https://github.com/intel1337')
        print("""
dev by bash / Intel1337
With Hunter.io API
        """)
        print("Press Enter to Continue...")
        input()
        onstart()
    else:
        print("Please enter a number between 1 and 5.")
        print("Press Enter to Continue...")
        input()
        onstart()
        
        


def onstart():
	os.system("cls && title Aphelios - Osint")
	main()

onstart()