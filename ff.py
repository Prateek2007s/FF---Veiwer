import subprocess
import sys
import time
import os

# Required modules
required_modules = ["requests", "pyfiglet", "termcolor"]

# Function to clear the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to install modules with a simulated installation progress
def install_module(module_name):
    print(f"Installing {module_name}...")
    time.sleep(0.5)
    for i in range(1, 101, 10):
        print(f"Progress: {i}% {'█' * (i // 10)}", end="\r")
        time.sleep(0.2)
    print("\n")

    # Install module using pip
    subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
    print(f"{module_name} installed successfully.\n")
    time.sleep(0.5)

# Check and install missing modules
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        install_module(module)

# Display "Installation Successful" message
clear_terminal()
print("Installation Successful!\n")
time.sleep(1)

# Clear terminal and run the main program code
clear_terminal()

# Importing modules after installation
import requests
from pyfiglet import figlet_format
from termcolor import colored

# Display Banner and Developer Credits
print(colored(figlet_format("AntifiedNull", font="standard"), "cyan"))

print(colored("• This Code Is Developed By AntifiedNull [Prateek]", "green"))
print(colored("• This Code Can Fetch Account Details Of Free Fire By UID", "yellow"))
print(colored("• Must Give Feedback Back To Us At Telegram", "green"))
print(colored("                      @AntifiedNullBot ✓", "blue"))
print(colored("                      @Vkpathal200 ✓", "blue"))

# UID input lene ka code
uid = input("Enter UID: ")

# Aapke diye gaye URL mein UID embed karenge
url = f"https://nepdevs.co/immortal_hack/api/ff-info.php?id={uid}"

try:
    # API request bhejna
    response = requests.get(url)
    
    # Response check karenge
    if response.status_code == 200:
        # Raw response text ko line by line split karenge
        lines = response.text.splitlines()
        
        # Filtered lines jisme unwanted lines nahi hain
        unwanted_lines = ["Array", "ACCOUNT INFO:", "api by @crazy_hacker404"]
        filtered_lines = [
            line for line in lines 
            if line.strip() and all(unwanted not in line for unwanted in unwanted_lines)
        ]
        
        # Filtered response ko print karenge
        print("\n".join(filtered_lines))
        
        # Custom closing message
        print("\nAPI HAS BEEN DEVELOPED BY @AntifiedNullBot, @Vkpathak200 IF YOU WANTED TO BUY THEN DM ME")
    else:
        print("Error:", response.status_code, response.text)
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)