import colorsys
import requests #dependency
from pystyle import Colorate, Colors, Center
from os import system
from time import sleep


boucle1 = True
#for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
data = {
    "content" : "message content",
    "username" : "custom username"
}

#leave this out if you dont want an embed
#for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
data["embeds"] = [
    {
        "description" : "text in embed",
        "title" : "embed title"
    }
]

#result: https://i.imgur.com/DRqXQzA.png


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
  V 1.0 - Arthurdufinister#3286 - discord.gg/BtNrFc45B7\n\n\n\n"""



while boucle1:
    system('cls')
    print(Colorate.Diagonal(Colors.green_to_cyan, Center.XCenter(header_final)))
    print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Webhook URL ↓"))
    webhook_url = input("")
    if webhook_url.startswith("https://discord.com/api/webhooks/"):
        try:
            system('cls')
            print(Colorate.Diagonal(Colors.green_to_cyan, Center.XCenter(header_final)))
            print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Webhook Content"))
            content = input("")
            print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Webhook Username"))
            username = input("")
            print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Webhook Avatar URL"))
            avatar = input("")

            data = {
    "content" : content,
    "username" : username,
    "avatar_url" : avatar
    }
            system('cls')
            print(Colorate.Diagonal(Colors.green_to_cyan, Center.XCenter(header_final)))
            print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Do you want an embed ? 1 = yes ; 0 = no"))
            answer = input("")
            if answer == ("0"):
                print(Colorate.Horizontal(Colors.green_to_cyan, "[!] Webhook posted !"))
                requests.post(webhook_url, json = data)
                sleep(2)

            elif answer == ("1"):
                system('cls')
                print(Colorate.Diagonal(Colors.green_to_cyan, Center.XCenter(header_final)))
                print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Embed Title"))
                title = input("")
                print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Embed Description"))
                description = input("")
                print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Do you want an image ? 1 = yes : 0 = no"))
                answer2 = input("")
                if answer2 == ("0"):
                    requests.post(webhook_url, json = data)
                elif answer2 == ("1"):
                    print(Colorate.Horizontal(Colors.green_to_cyan, "[?] Enter Image URL"))
                    url = input("")

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
                    sleep(5)
        except:
            system('cls')
            print(Colorate.Diagonal(Colors.green_to_cyan, Center.XCenter(header_final)))
            print(Colorate.Horizontal(Colors.green_to_cyan, "[!] Error"))
            sleep(2)
    else:
            system('cls')
            print(Colorate.Diagonal(Colors.green_to_cyan, Center.XCenter(header_final)))
            print(Colorate.Horizontal(Colors.green_to_cyan, "[!] Please insert a valid link."))
            sleep(2)

            requests.post(webhook_url, json = data)