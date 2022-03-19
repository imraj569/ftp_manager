import PySimpleGUI as sg
import os
from keyboard import press_and_release
from time import sleep
from pyautogui import write
import sys

sg.theme('Dark Blue')

layout =[
    [sg.Text('Just copy and past the default getway IP')],
    [sg.Text('Default Getway Ip:',size=(15,1)),sg.InputText(key='Ip')],
    [sg.Text('                                                              ')],
    [sg.Submit(),  sg.Button('Clear'),  sg.Exit(), sg.Button('Get IP'),  sg.Button('past')]
]

win = sg.Window('FTP manager', layout)

def clear_input():
    for key in values:
        win[key]('')
    return None

def Gatway():
    x = (values)
    address =(x['Ip'])
    os.system('taskkill /f /im cmd.exe')
    sleep(0.10)
    press_and_release('win+e')
    sleep(1)
    press_and_release('alt+d')
    sleep(0.10)
    write(f'ftp://{address}:2221/')
    sleep(0.10)
    press_and_release('enter')
    sys.exit

while True:
    event, values = win.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        os.system('taskkill /f /im cmd.exe')
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        Gatway()
    if event == 'Get IP':
        os.system("start cmd /k ipconfig")
    if event == 'past':
        press_and_release('ctrl+v')
                                                                      
win.close()
