import telegram
from telegram import Update
from telegram.ext import Updater

import PySimpleGUI as sg

sg.theme('Reddit')

layout = [  [sg.Text('Scrivi un messaggio:', size=(25), font=('sans-serif'))],
            [sg.Multiline(key = 'text', no_scrollbar = True, size=(45, 20), font='sans-serif', background_color='whitesmoke', text_color='black')],
            [sg.Button('Invia', size=(15), font=('sans-serif')), sg.Input(key='Image', visible = False, enable_events = True), sg.FileBrowse('Immagine', target = 'Image', size=(15, 1), font=('sans-serif')), sg.Button('Annulla', size=(15), font=('sans-serif'))] ]

            
error = [   [sg.Text('Error')]  ]

window = sg.Window('TelePonti', layout, icon = 'icona.ico')

TELEGRAM_BOT_TOKEN = ' '
TELEGRAM_CHAT_ID = ' '

bot = telegram.Bot(token = TELEGRAM_BOT_TOKEN)

while True:
    event, values = window.read()
    Testo = " "
    Immagine = " "
    if event == sg.WIN_CLOSED or event == 'Annulla':
        break
        
    elif event == 'Invia' :
        for char in values['text']:
            Testo = Testo + char;
        Testo = Testo.strip()
        try:
            bot.send_message(chat_id = TELEGRAM_CHAT_ID, text = Testo)
            sg.Popup("Messaggio inviato.", icon = 'Yes.ico')
        except Exception as ex:
            sg.Popup("Messaggio privo di testo.", icon = 'No.ico')
           
            
    if event == 'Image' :
        try:
            bot.send_photo(chat_id = TELEGRAM_CHAT_ID, photo = open(values['Image'], 'rb'))
            sg.Popup("Immagine inviata!", icon = 'Yes.ico')
        except Exception as ex:
            sg.Popup("Immagine non trovata", icon = 'No.ico')
            
window.close()
