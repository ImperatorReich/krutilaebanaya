import requests
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait
from time import sleep


with open(r"config.txt",'r') as file:
    global api_id
    global api_hash
    global bindchat
    global outchat
    global bindlink
    global key_wiqru
    global id_servicce_wiqru
    global summ_of_service_wiqru
    line = file.readlines()
    line = [line.rstrip() for line in line]
    print("api_id - "+line[0]+"\n"+"api_hash - "+line[1]+"\n"+"bindchat - "+line[2]+"\n"+"key-wiq.ru - "+line[3]+"\n"+"id-service-wiq.ru - "+line[4]+"\n"+"summ-service-wiq.ru - "+line[5])
    api_id = int(line[0])
    api_hash = str(line[1])
    bindchat = int(line[2])
    key_wiqru = str(line[3])
    id_servicce_wiqru = str(line[4])
    summ_of_service_wiqru = str(line[5])

app = Client("my_account", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.chat(bindchat))
def nakrut(_,msg):
    print(msg.id)
    chat = app.get_chat(msg.sender_chat.id)
    link = "https://t.me/" + chat.username + '/' + str(msg.id)
    a = requests.get('https://wiq.ru/api/?key=' + key_wiqru + '&action=create&service=' + id_servicce_wiqru + '&quantity=' + summ_of_service_wiqru + '&link=' + link)
    print(a.text)

app.run()