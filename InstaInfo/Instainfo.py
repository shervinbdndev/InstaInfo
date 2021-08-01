if __name__ == "__main__":
    try:
        import requests
        import instagramy
        import colorama
        import cfonts
        import time
        import json
        import socket
        import subprocess
    except:
        from requests import get
        from instagramy import InstagramUser
        from colorama.initialise import init
        from colorama.ansi import Fore
        from cfonts import render , cli
        from time import sleep
        from json import loads
        from socket import gethostbyname , gethostname
        from subprocess import call

    C = [
        f"{colorama.ansi.Fore.WHITE}",
        f"{colorama.ansi.Fore.GREEN}",
        f"{colorama.ansi.Fore.CYAN}",
        f"{colorama.ansi.Fore.MAGENTA}",
        f"{colorama.ansi.Fore.YELLOW}",
        f"{colorama.ansi.Fore.RED}"
    ]

    L_IP = socket.gethostbyname(socket.gethostname())
    RE_Q = requests.get("https://api.myip.com").content
    LOAD = json.loads(RE_Q)
    P_IP = LOAD["ip"]

    H = """
             .:--================--:.             
           :+**++================+***+:           
         .+*+-.                    .-**+.         
         +**.                   -++: .**+         
        .**=         :-====-:   +**-  =**:        
        :**-      .=***+==+***=.      -**-        
        -**:     :+*+:      :+**:     :**-        
        -++:    .+++          +**.    :**-        
        -++:    :++-          -**:    :**-        
        -++:    .++=          +**.    :**-        
        :++:     :++=:      :++*:     :**-        
        :++:      .=+++====+++=.      -**-        
        .++-         :--==--:         =**:        
         =++.                        .**+         
          =++-.                    .-**+.         
           :=+++====---==========++**+-           
              ::----=============--:.
        """

    def HeaderFunc():
        print(f"{C[3]}{H}")
        time.sleep(1.5)
    HeaderFunc()

    def MainScript():
        time.sleep(1.5)
        print(f"\n\n{C[1]}[{C[3]}Local IP{C[1]}] {C[0]}: {C[2]}{L_IP}")
        print(f"\n{C[1]}[{C[3]}Public IP{C[1]}] {C[0]}: {C[2]}{P_IP}")
        while True:
            INPUT = str(input(f"\n\n{C[1]}[{C[3]}~{C[1]}] {C[1]}({C[5]}Inst4Inf0{C[1]})--$ \n{C[2]}[~] >{C[0]} "))
            if str(INPUT) == "help" or str(INPUT) == "Help" or str(INPUT) == "HELP":
                print("<====================== Help Center ======================>\n"
                      f"\n{C[3]}Commands :"
                      f"\n{C[1]}help => {C[2]}Opening The Help Center\n"
                      f"\n{C[1]}set username => {C[2]}Setting The Username For Getting Page Information\n"
                      f"\n{C[1]}show banner => {C[2]}Shows The Script banner\n"
                      f"\n{C[1]}script usage => {C[2]}Shows Script Usage\n"
                      f"\n{C[1]}version => {C[2]}Shows The Script's Version\n"
                      f"\n{C[1]}update script => {C[2]}Download The Latest Update Of Script\n"
                      f"\n{C[1]}exit => {C[2]}Exit the Script\n"
                      f"\n{C[0]}<=========================================================>\n"
                )
                continue
            elif str(INPUT) == "show banner" or str(INPUT) == "Show Banner" or str(INPUT) == "SHOW BANNER":
                HEADER = cfonts.render("InstaInfo" , colors = ["magenta" , "yellow"] , align = "left")
                print(HEADER)
                continue
            elif str(INPUT) == "version" or str(INPUT) == "Version" or str(INPUT) == "VERSION":
                with open("version.txt" , "r") as V:
                    print(str(V.read(5)))
                    continue
            elif str(INPUT) == "exit" or str(INPUT) == "Exit" or str(INPUT) == "EXIT":
                break
            elif str(INPUT) == "update script" or str(INPUT) == "Update Script" or str(INPUT) == "UPDATE SCRIPT":
                try:
                    subprocess.call(["git" , "clone" , "https://github.com/shervin-glitch/InstaInfo"])
                    print("[+] The Script Directory is Cloned")
                except Exception as Err:
                    subprocess.call(["rm" , "-rf" , "InstaInfo"])
                    subprocess.call(["git" , "clone" , "https://github.com/shervin-glitch/InstaInfo"])
                    print("[+] The Script Directory is Cloned")
                finally:
                    print("\n")
                continue
            elif str(INPUT) == "set username" or str(INPUT) == "Set Username" or str(INPUT) == "SET USERNAME":
                INPUT = str(input(f"\n\n{C[1]}[{C[3]}~{C[1]}] {C[1]}({C[5]}Inst4Inf0{C[1]})--$ \n{C[2]}[set-username] >{C[0]} "))
                i = instagramy.InstagramUser(INPUT)
                print(f"\n{C[1]}[{C[3]}Verified{C[1]}] {C[0]}: {C[2]}{i.is_verified}")
                print(f"{C[1]}[{C[3]}Private{C[1]}] {C[0]}: {C[2]}{i.is_private}")
                print(f"{C[1]}[{C[3]}Username{C[1]}] {C[0]}: {C[2]}@{INPUT}")
                print(f"{C[1]}[{C[3]}Full name{C[1]}] {C[0]}: {C[2]}{i.fullname}")
                print(f"{C[1]}[{C[3]}Followers{C[1]}] {C[0]}: {C[2]}{i.number_of_followers}")
                print(f"{C[1]}[{C[3]}Followings{C[1]}] {C[0]}: {C[2]}{i.number_of_followings}")
                print(f"{C[1]}[{C[3]}Posts{C[1]}] {C[0]}: {C[2]}{i.number_of_posts}")
                print(f"{C[1]}[{C[3]}Website{C[1]}] {C[0]}: {C[2]}{i.website}")
                print(f"{C[1]}[{C[3]}Biography{C[1]}] {C[0]}: {C[2]}{i.biography}")
                print(f"{C[1]}[{C[3]}Profile Picture Url{C[1]}] {C[0]}: {C[2]}{i.profile_picture_url}")
                continue
    MainScript()
