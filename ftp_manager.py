import os
from keyboard import press_and_release
from time import sleep
from pyautogui import write
import colorama
from colorama import Fore
colorama.init(autoreset=True)
import sys


print(Fore.CYAN+'''
╭━━━┳━━━━┳━━━╮
┃╭━━┫╭╮╭╮┃╭━╮┃
┃╰━━╋╯┃┃╰┫╰━╯┃
┃╭━━╯╱┃┃╱┃╭━━╯
┃┃╱╱╱╱┃┃╱┃┃
╰╯╱╱╱╱╰╯╱╰╯         MANAGER V-0.1
------------------------------------------''')
print(Fore.RED+'''make sure your ftp server open port is 2221
------------------------------------------''')
os.system("start cmd /k ipconfig")
add = input(Fore.BLUE+'Just copy and past defult getway address here : ')
print(Fore.LIGHTYELLOW_EX+'please wait opening FTP server')
os.system('taskkill /f /im cmd.exe')
sleep(0.10)
press_and_release('win+e')
sleep(1)
press_and_release('alt+d')
sleep(0.10)
write(f'ftp://{add}:2221/')
sleep(0.10)
press_and_release('enter')
print(Fore.BLUE+'succesfully open ftp server')
sys.exit()