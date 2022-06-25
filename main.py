import colorsys
import webbrowser
import requests #dependency
from pystyle import Colorate, Colors, Center
from os import system
from time import sleep
import json

settings = {}

try: 
    f = open('settings.json')
    saved_url = json.load(f)
    webhook_url = (saved_url['webhook_url']['url'])
except:
    print("No json")




boucle1 = True
data = {
    "content" : "message content",
    "username" : "custom username"
}
data["embeds"] = [
    {
        "description" : "text in embed",
        "title" : "embed title"
    }
]

header_final = """
8888888 8888888888 8 8888      88 `8.`8888.      ,8'
      8 8888       8 8888      88  `8.`8888.    ,8'
      8 8888       8 8888      88   `8.`8888.  ,8'
      8 8888       8 8888      88    `8.`8888.,8'
      8 8888       8 8888      88     `8.`88888'
      8 8888       8 8888      88     .88.`8888.
      8 8888       8 8888      88    .8'`8.`8888.
      8 8888       ` 8888     ,8P   .8'  `8.`8888.
      8 8888         8888   ,d8P   .8'    `8.`8888.
      8 8888          `Y88888P'   .8'      `8.`8888.
  V 2.0 - Arthurdufinister#3286 - discord.gg/BtNrFc45B7\n\n\n\n"""

while boucle1:
    system('cls')
    print(Colorate.Diagonal(Colors.green_to_cyan, Center.XCenter(header_final)))    
    try:
        if webhook_url.startswith("https://discord.com/api/webhooks/"):
            print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Do you want to load your webhook url ? y = yes, n = no"))
            answerload = input("")
            if answerload == "y":
                print(Colorate.Diagonal(Colors.green_to_cyan, Center.XCenter("Webhook url save is valid")))
                sleep(3)
                
            else:
                print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Webhook URL ↓"))
                webhook_url = input("")
                print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Do you want to save your webhook url ? y = yes, n = no"))
                answersave = input("")
                if answersave == "y":
                    open('settings.json', 'w').close()

                    
                    settings['webhook_url'] = {'url': webhook_url}
                    with open('settings.json', 'w') as f:
                        json.dump(settings, f)
                else:
                    pass
        else:
            pass
    except:
        system('cls')
        print(Colorate.Diagonal(Colors.green_to_cyan, Center.XCenter(header_final)))
        print(Colorate.Diagonal(Colors.green_to_cyan, Center.XCenter("No json founded, please continue.")))
        
        print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Webhook URL ↓"))
        webhook_url = input("")
        print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Do you want to save your webhook url ? y = yes, n = no"))
        answersave = input("")
        if answersave == "y":
            open('settings.json', 'w').close()

            
            settings['webhook_url'] = {'url': webhook_url}
            with open('settings.json', 'w') as f:
                json.dump(settings, f)
        else:
            pass
    if webhook_url.startswith("https://discord.com/api/webhooks/"):
        try:
            system('cls')
            print(Colorate.Diagonal(Colors.green_to_cyan, Center.XCenter(header_final)))
            print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Webhook Content"))
            content = input("")
            print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Webhook Username"))
            username = input("")
            print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Do you want to choose an avatar for the webhook ? y = yes ; n = no"))
            answer3 = input("")
            if answer3 == ("n"):
                data = {
    "content" : content,
    "username" : username,
    }          
                print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Webhook Base successfuly set"))
                sleep(1)


            elif answer3 == ("y"):
                print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Webhook Avatar URL"))
                avatar = input("")
                print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Webhook Base successfuly set"))
                sleep(1)

                data = {
        "content" : content,
        "username" : username,
        "avatar_url" : avatar
        }
            system('cls')
            print(Colorate.Diagonal(Colors.green_to_cyan, Center.XCenter(header_final)))
            print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Do you want an embed ? y = yes ; n = no"))
            answer = input("")
            if answer == ("n"):
                print(Colorate.Horizontal(Colors.green_to_cyan, "[!] Webhook posted !"))
                requests.post(webhook_url, json = data)
                sleep(1)

            elif answer == ("y"):
                system('cls')
                print(Colorate.Diagonal(Colors.green_to_cyan, Center.XCenter(header_final)))
                print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Do you want text inside it ? y = yes ; n = no"))
                answertext = input('')
                if answertext == 'y':
                    print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Embed Title"))
                    title = input("")
                    print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Embed Description"))
                    description = input("")
                    print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Do you want fields inside it ? y = yes ; n = no"))
                    answerfield = input('')
                    if answerfield == 'y':

                        print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Field Name"))
                        fieldname = input("")
                        print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Field Value"))
                        fieldvalue = input("")

                        data["embeds"] = [
                            {
                            
                                "type": "rich",
                                "title": title,
                                "description": description,
                                "color": 0x0000,                            
                                "fields": [
                                {
                                    "name": fieldname,
                                    "value": fieldvalue 
                                }
                            ]

    }]
                    else:
                        data["embeds"] = [
                            {
                            
                                "type": "rich",
                                "title": title,
                                "description": description,
                                "color": 0x0000                       
                                }]
                else:
                    pass                 

                print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Do you want an image ? y = yes : n = no"))
                answer2 = input("")
                if answer2 == ("y"): 
                    
                    print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Enter Image URL"))
                    url = input("")
                    if answertext == 'y':
                        if answerfield == 'y':
                            data["embeds"] = [
                                {
                                
                                    "type": "rich",
                                    "title": title,
                                    "description": description,
                                    "color": 0x0000,                            
                                    "image": {
                                            "url": url,
                                            "height": 0,
                                            "width": 0
                                },  "fields": [
                                    {
                                        "name": fieldname,
                                        "value": fieldvalue 
                                    }
                                ]

        }]
                            requests.post(webhook_url, json = data)
                            print(Colorate.Horizontal(Colors.green_to_cyan, "[!] Webhook posted !"))
                            sleep(1)
                        else:
                            data["embeds"] = [
                            {
                            
                                "type": "rich",
                                "title": title,
                                "description": description,
                                "color": 0x0000,
                                "image": {
                                            "url": url,
                                            "height": 0,
                                            "width": 0
                                }                              

    }]

                            requests.post(webhook_url, json = data)
                            print(Colorate.Horizontal(Colors.green_to_cyan, "[!] Webhook posted !"))
                            sleep(1)
                    else: 
                        data["embeds"] = [
                                {
                                
                                    "type": "rich",
                                    "title": "",
                                    "description": "",
                                    "color": 0x0000,                            
                                    "image": {
                                            "url": url,
                                            "height": 0,
                                            "width": 0
                                },

        }]
                        requests.post(webhook_url, json = data)
                        print(Colorate.Horizontal(Colors.green_to_cyan, "[!] Webhook posted !"))
                        sleep(1)

                elif answer2 == ("n"):
                    
                    
                    if answertext == 'y':
                        if answerfield == 'y':
                            data["embeds"] = [
                                {
                                
                                    "type": "rich",
                                    "title": title,
                                    "description": description,
                                    "color": 0x0000,
                                    "fields": [
                                        {
                                        "name": fieldname,
                                        "value": fieldvalue
                                        }
                                    ]
                                    
                            }]
                            
                                
                            requests.post(webhook_url, json = data)
                            print(Colorate.Horizontal(Colors.green_to_cyan, "[!] Webhook posted !"))
                            sleep(1)
                        else:
                            data["embeds"] = [
                            {
                            
                                "type": "rich",
                                "title": title,
                                "description": description,
                                "color": 0x0000

    }]

                        requests.post(webhook_url, json = data)
                        print(Colorate.Horizontal(Colors.green_to_cyan, "[!] Webhook posted !"))
                        sleep(1)

                    else:                                                  
                        requests.post(webhook_url, json = data)
                        print(Colorate.Horizontal(Colors.green_to_cyan, "[!] Webhook posted !"))
                        sleep(1)

        except:
            system('cls')
            print(Colorate.Horizontal(Colors.green_to_cyan, "[!] ERROR"))

    else:
            system('cls')
            print(Colorate.Diagonal(Colors.green_to_cyan, Center.XCenter(header_final)))
            print(Colorate.Horizontal(Colors.green_to_cyan, "[!] Please insert a valid link."))
            sleep(1)
            boucle1

            requests.post(webhook_url, json = data)