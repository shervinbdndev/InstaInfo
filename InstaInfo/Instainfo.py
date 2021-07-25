if __name__ == "__main__":
    try:
        import requests
        import instagramy
        import colorama
        import cfonts
        import time
        import json
        import socket
    except:
        from requests import get
        from instagramy import InstagramUser
        from colorama.initialise import init
        from colorama.ansi import Fore
        from cfonts import render , cli
        from time import sleep
        from json import loads
        from socket import gethostbyname , gethostname

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
              ::----=============--:."""

    def GetUsername():
        print(f"{C[3]}{H}")
        time.sleep(1.5)
        HEADER = cfonts.render("InstaInfo" , colors = ["magenta" , "yellow" , "red"] , font = "chrome" , align = "left")
        print(HEADER)
    GetUsername()

    def MainScript():
        time.sleep(1.5)
        print(f"\n\n{C[1]}[{C[3]}Local IP{C[1]}] {C[0]}: {C[2]}{L_IP}")
        print(f"\n{C[1]}[{C[3]}Public IP{C[1]}] {C[0]}: {C[2]}{P_IP}")
        INPUT = str(input(f"\n\n{C[1]}[{C[3]}~{C[1]}] {C[1]}({C[5]}U$ERNAME{C[1]}){C[2]} --@{C[0]} "))
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
    MainScript()
