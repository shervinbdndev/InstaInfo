if __name__ == "__main__":
    try:
        import requests
        import instagramy
        import colorama
        import cfonts
        import time
    except:
        from requests import get
        from instagramy import InstagramUser
        from colorama.initialise import init
        from colorama.ansi import Fore
        from cfonts import render , cli
        from time import sleep

    C = [
        f"{colorama.ansi.Fore.WHITE}",
        f"{colorama.ansi.Fore.GREEN}",
        f"{colorama.ansi.Fore.CYAN}",
        f"{colorama.ansi.Fore.MAGENTA}",
        f"{colorama.ansi.Fore.YELLOW}",
        f"{colorama.ansi.Fore.RED}"
    ]

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
        INPUT = str(input(f"{C[1]}[{C[3]}~{C[1]}] {C[1]}({C[5]}U$ERNAME{C[1]}){C[2]} --@{C[0]} "))
        i = instagramy.InstagramUser(INPUT)
        print(f"{C[1]}[{C[3]}Verified{C[1]}] {C[0]}: {C[2]}{i.is_verified}")
        print(f"{C[1]}[{C[3]}Username{C[1]}] {C[0]}: {C[2]}{INPUT}")
        print(f"{C[1]}[{C[3]}Full name{C[1]}] {C[0]}: {C[2]}{i.fullname}")
        print(f"{C[1]}[{C[3]}Followers{C[1]}] {C[0]}: {C[2]}{i.number_of_followers}")
        print(f"{C[1]}[{C[3]}Followings{C[1]}] {C[0]}: {C[2]}{i.number_of_followings}")
        print(f"{C[1]}[{C[3]}Posts{C[1]}] {C[0]}: {C[2]}{i.number_of_posts}")
        print(f"{C[1]}[{C[3]}Website{C[1]}] {C[0]}: {C[2]}{i.website}")
    MainScript()