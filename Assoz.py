from httpx import post
from threading import Thread, Lock
from random import choice
from utils import *
import os

def major():
    Clear()
    Title("Nows@Platipus ~ Link_Fucker $")
    print(Vertical.yellow_to_red("""
                 █████  ███████ ███████  ██████  ███████ 
                ██   ██    ███     ███  ██    ██    ███  
                ███████   ███     ███   ██    ██   ███   
                ██   ██  ███     ███    ██    ██  ███    
                ██   ██ ███████ ███████  ██████  ███████
                 
                        [Ip Logger links fucker]
"""))
    th_lock = Lock()
    url = input(Horizontal.yellow_to_red("Link to spam > "))
    proxy = input(Horizontal.yellow_to_red("Drag your proxies file > "))
    file_name = (os.path.splitext(proxy)[0].split("\\"))[-1] + os.path.splitext(proxy)[1]

    Title(f"Nows@Platipus ~ Link_Fucker $ [ Using {file_name} As Proxies List ]")
    return url, proxy, th_lock, 

_return = major()
hit = 0
fail = 0

class Setup:
    def proxy_list():
        with open(_return[1], "r+")as f:
            pro = choice(f.readlines())
            f.close()
            return pro



def fuck_link():
    for _ in range(100):
        global hit, fail

        try:
            post(_return[0],headers={'user-agent': "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.26 Safari/537.11"}, proxies={"http://": "http://"+Setup.proxy_list(), "https://": "http://"+Setup.proxy_list()})
            _return[-1].acquire()
            hit += 1
            _return[-1].release()
        except:
            _return[-1].acquire()
            fail += 1
            _return[-1].release()  

class main:
    print("\n")
    for _ in range(int(10000)):
        Thread(target=fuck_link).start()
        print(Horizontal.yellow_to_red(f"[+] Link: {_return[0]} | Hit: {hit} | Fail: {fail}"), end="\r")

    print(Vertical.yellow_to_red("\n\n[!] Finished "), end="\r")
    input()

if __name__ == '__main__':
    os.system('')
    main()
