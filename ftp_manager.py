import os
import time
import colorama
from colorama import Fore
from keyboard import press_and_release
from pyautogui import write
import re
colorama.init(autoreset=True)

def ftp_clint():
    print(Fore.CYAN + '''
    ╭━━━┳━━━━┳━━━╮
    ┃╭━━┫╭╮╭╮┃╭━╮┃
    ┃╰━━╋╯┃┃╰┫╰━╯┃
    ┃╭━━╯╱┃┃╱┃╭━━╯
    ┃┃╱╱╱╱┃┃╱┃┃
    ╰╯╱╱╱╱╰╯╱╰╯         
                    MANAGER V-1.5
    ------------------------------------------             
    github - https://github.com/imraj569/ftpmanager
    instagram - @im.raj.569
    ------------------------------------------''')
    print(Fore.RED + '''Make sure your FTP server port is 2221
    ------------------------------------------''')

    output = os.popen("ipconfig").read()
    default_gateway_match = re.search(r"Default Gateway .*?:\s+(\S+)", output)
    if default_gateway_match:
        default_gateway_address = default_gateway_match.group(1)
    else:
        print(Fore.RED + "Failed to retrieve default gateway address.")
        exit()

    print(Fore.LIGHTYELLOW_EX + 'Please wait, opening FTP server...')
    time.sleep(0.10)
    press_and_release('win+e')
    time.sleep(1)
    press_and_release('alt+d')
    time.sleep(0.20)
    write(f'ftp://{default_gateway_address}:2221/')
    time.sleep(0.20)
    press_and_release('enter')
    print(Fore.BLUE + 'Successfully opened FTP server')
if __name__ == "__main__":
    ftp_clint()