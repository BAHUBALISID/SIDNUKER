import sys
import os

print("Installing python pip modules for SidNuker")
if sys.platform.startswith("win"):
    "WINDOWS"
    os.system("pip install pystyle")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install json")
    os.system("pip install random")
    os.system("pip install string")
    os.system("pip install base64")
    os.system("pip install threading")
    os.system("pip install discord")
    os.system("pip install discord.py")
    os.system("python SidNuker.py")
