import os, random,threading
try:
    import requests
    from pystyle import *
    from fake_useragent import UserAgent
except(ModuleNotFoundError):
    (input
        (Center.XCenter
            (Colorate.Vertical
                (Colors.purple_to_blue,"""

 █████╗ ███████╗███████╗ ██████╗ ███████╗
██╔══██╗██╔════╝██╔════╝██╔═══██╗╚══███╔╝
███████║███████╗███████╗██║   ██║  ███╔╝ 
██╔══██║╚════██║╚════██║██║   ██║ ███╔╝  
██║  ██║███████║███████║╚██████╔╝███████╗
╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝
 Install all package in requirements.txt"""
                )
            )
        )
    )
proxies = []

time = int(input
(Center.XCenter
    (Colorate.Vertical
        (Colors.purple_to_blue,"""

 █████╗ ███████╗███████╗ ██████╗ ███████╗
██╔══██╗██╔════╝██╔════╝██╔═══██╗╚══███╔╝
███████║███████╗███████╗██║   ██║  ███╔╝ 
██╔══██║╚════██║╚════██║██║   ██║ ███╔╝  
██║  ██║███████║███████║╚██████╔╝███████╗
╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝
      Assoz -> Grabify link Spammer          
         Made by PLATIPUS#2535                                        
                                        
How much spam > """
        )
    )
))
url = input(Center.XCenter(Colorate.Horizontal(Colors.purple_to_blue,"Url To Spam > ")))
if not os.path.exists("proxies.txt"):
    input(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue,"""

 █████╗ ███████╗███████╗ ██████╗ ███████╗
██╔══██╗██╔════╝██╔════╝██╔═══██╗╚══███╔╝
███████║███████╗███████╗██║   ██║  ███╔╝ 
██╔══██║╚════██║╚════██║██║   ██║ ███╔╝  
██║  ██║███████║███████║╚██████╔╝███████╗
╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝
File proxies.txt doesn't exists, create one !""")))

    exit()
with open("proxies.txt", "r", encoding = "UTF-8") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        proxies.append(line)
            
    if not len(proxies):
        input("\nNo proxies loaded in proxies.txt")
        exit()
def spam(proxies):
    hit = 0        
    while time != hit:

        headers = {
            'authority': 'grabify.link',
            'user-agent': UserAgent().random,
        }


        try:
            req = requests.get(url, headers=headers, proxies=random.choice(proxies))
            print(f"Successfully Spammed at {url} | Proxy used: {proxies}")
        except:
            req = requests.get("https://wrongurltoskip.com")

        if req.status_code == 200:
            hit += 1
            os.system(f'title Grabify Spammer / Made by PLATIPUS#2535 Hit: {hit}')
        else:
            pass
    
    os.system('cls&&title Grabify Spammer / Made by PLATIPUS#2535 Spam Is Over')
    (input
    (Center.XCenter
        (Colorate.Vertical
            (Colors.purple_to_blue,"""

 █████╗ ███████╗███████╗ ██████╗ ███████╗
██╔══██╗██╔════╝██╔════╝██╔═══██╗╚══███╔╝
███████║███████╗███████╗██║   ██║  ███╔╝ 
██╔══██║╚════██║╚════██║██║   ██║ ███╔╝  
██║  ██║███████║███████║╚██████╔╝███████╗
╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝
    Assoz -> Grabify link Spammer          
        Made by PLATIPUS#2535"""
            )
        )
    ))
if __name__ == '__main__':
    for i in range(time):
        threading.Thread(target=spam()).start()
