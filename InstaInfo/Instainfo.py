if __name__ == "__main__":
    try:
        import os
        import requests
        import instagramy
        import colorama
        import cfonts
        import time
        import json
        import socket
        import subprocess
        import io
        import sys
        import random
        import builtins
        import shutil
        import platform
    except:
        import subprocess;import sys;subprocess.call(sys.exit(0))

    C = [
        f"{colorama.ansi.Fore.WHITE}",
        f"{colorama.ansi.Fore.GREEN}",
        f"{colorama.ansi.Fore.CYAN}",
        f"{colorama.ansi.Fore.MAGENTA}",
        f"{colorama.ansi.Fore.YELLOW}",
        f"{colorama.ansi.Fore.RED}" 
    ]

    F = [
        "black" , "red" , "green" , "yellow" ,
        "blue" , "magenta" , "cyan" , "white" ,
        "gray"
    ]

    RE_Q = requests.get("https://api.myip.com").content
    LOAD = json.loads(RE_Q)

    H = f"""
             {random.choice(C[0::]) or random.choice(C[0::]) and random.choice(C[0::])}.:--================--:.             
           :+**++================+***+:           
         .+*+-.                    .-**+.         
         +**.                   -++: .**+         
        .**=         {random.choice(C[0::]) or random.choice(C[0::]) and random.choice(C[0::])}:-====-:   +**-  =**:        
        :**-      .=***+==+***=.      -**-        
        -**:     :+*+:      :+**:     :**-        
        -++:    .+++          +**.    :**-        
        -++:    :++-          -**:    :**-        
        -++:    .++=          +**.    :**-        
        :++:     :++=:      :++*:     :**-        
        :++:      .=+++====+++=.      -**-        
        .++-         {random.choice(C[0::]) or random.choice(C[0::]) and random.choice(C[0::])}:--==--:         =**:        
         =++.                        .**+         
          =++-.                    .-**+.         
           :=+++====---==========++**+-           
              ::----=============--:.\n
            {C[1]}Version: {C[0]}10.1.4
            {C[1]}By: {C[0]}https://github.com/shervin-glitch/"""


    def CheckSystem(systemType :builtins.str = platform.system()):
        if systemType == "Linux":
            try:
                os.system("clear")
            except Exception:
                sys.exit(0)
        elif systemType == "Windows":
            try:
                os.system("cls")
            except Exception:
                sys.exit(0)
        else:
            sys.exit(0)
    CheckSystem()


    def HeaderFunc():
        print(f"{H}")
        time.sleep(1.5)
    HeaderFunc()

    def HelperIntro():
        print(f"\n\n{C[1]}[{C[3]}Python Version{C[1]}] {C[0]}: {C[2]}{builtins.str(sys.version[0:6] or platform.python_version())}")
        print(f"\n{C[1]}[{C[3]}Local IP{C[1]}] {C[0]}: {C[2]}{builtins.str(socket.gethostbyname(socket.gethostname()))}")
        print(f"\n{C[1]}[{C[3]}Public IP{C[1]}] {C[0]}: {C[2]}{LOAD['ip']}")
        print(f"\n{C[1]}[{C[3]}Country{C[1]}] {C[0]}: {C[2]}{LOAD['country']}")
        print(f"\n\n{C[0]}<-------------------------------------------------------------------->\n"
                      f"\n{C[3]}HELP"
                      f"\n{C[1]}[{C[3]}?{C[1]}] help => {C[2]}Opening The Help Center\n"
                      f"\n\n{C[3]}SCRIPTS"
                      f"\n{C[1]}[{C[3]}0{C[1]}] scripts/print-info => {C[2]}Enter Username For Getting Page Information"
                      f"\n{C[1]}[{C[3]}1{C[1]}] scripts/get-likes => {C[2]}Enter Post Full URL to Get Likes of a Post"
                      f"\n{C[1]}[{C[3]}2{C[1]}] scripts/get-comments => {C[2]}Enter Post Full URL to Get comments of a Post"
                      f"\n{C[1]}[{C[3]}3{C[1]}] scripts/remover => {C[2]}Enter The Adderss of Old Script Directory to Delete"
                      f"\n{C[1]}[{C[3]}4{C[1]}] clear => {C[2]}Clears The Terminal\n"
                      f"\n\n{C[3]}OPTIONS"
                      f"\n{C[1]}[{C[3]}v{C[1]}] options/version => {C[2]}Shows The Script's Version"
                      f"\n{C[1]}[{C[3]}l{C[1]}] options/license => {C[2]}Shows The Script's License\n"
                      f"\n\n{C[3]}COMMANDS"
                      f"\n{C[1]}[{C[3]}77{C[1]}] show-banner => {C[2]}Shows The Script banner"
                      f"\n{C[1]}[{C[3]}88{C[1]}] update-script => {C[2]}Download The Latest Update Of Script(This Command is Only Able to run in Linux)"
                      f"\n{C[1]}[{C[3]}99{C[1]}] exit => {C[2]}Exit the Script"
                      f"\n\n{C[0]}<-------------------------------------------------------------------->\n"
                )
    HelperIntro()

    def MainScript():
        while True:
            INPUT = builtins.str(input(f"\n\n{C[1]}[{C[3]}~{C[1]}] {C[1]}({C[5]}Inst4Inf0{C[1]})--$ \n{C[2]}[~] >{C[0]} "))
            if builtins.str(INPUT) in ["help" , "Help" , "HELP" , "?"]:
                HelperIntro()
                continue
            elif builtins.str(INPUT) in ["show-banner" , "77"]:
                HEADER = cfonts.render(text = "InstaInfo" , colors = [f"{random.choice(F)}" , f"{random.choice(F)}"] , align = "left")
                print(HEADER)
                continue
            elif builtins.str(INPUT) in ["options/version" , "v"]:
                with io.open(file = "version.txt" , mode = "r") as V:
                    print(builtins.str(V.read(10)))
                    V.close()
                    continue
            elif builtins.str(INPUT) in ["options/license" , "l"]:
                with io.open(file = "license.txt" , mode = "r") as L:
                    print(builtins.str(L.read(5055)))
                    L.close()
                    continue
            elif builtins.str(INPUT) in ["exit" , "Exit" , "EXIT" , "99"]:
                last_input = builtins.str(input(f"{C[1]}[{C[3]}?{C[1]}] {C[0]}Do you want to save The Progress In log.txt ?"))
                if builtins.str(last_input) in ["y" , "Y" , "yes" , "Yes" , "YES"]:
                    with io.open(file = r"{}".format("log/log.txt") , mode = "a" , encoding = "utf-8") as LOG:
                        LOG.write(f"Username : @{builtins.str(i.username)}\n")
                        LOG.write(f"Verified : {builtins.str(i.is_verified)}\n")
                        LOG.write(f"Private : {builtins.str(i.is_private)}\n")
                        LOG.write(f"Full name : {builtins.str(i.fullname)}\n")
                        LOG.write(f"Recently Joined Instagram : {builtins.str(i.is_joined_recently)}\n")
                        LOG.write(f"Follow Requested Other Pages : {builtins.str(i.has_requested_viewer)}\n")
                        LOG.write(f"Followers : {builtins.str(i.number_of_followers):,}\n")
                        LOG.write(f"Followings : {builtins.str(i.number_of_followings):,}\n")
                        LOG.write(f"Posts : {builtins.str(i.number_of_posts):,}\n")
                        LOG.write(f"Website : {builtins.str(i.website)}\n")
                        LOG.write(f"Facebook Page : {builtins.str(i.connected_fb_page)}\n")
                        LOG.write(f"Country Blocked User : {builtins.str(i.has_country_block)}\n")
                        LOG.write(F"Blocked Any Instagram Users : {builtins.str(i.has_blocked_viewer)}\n")
                        LOG.write(f"Blocked By Other Users : {builtins.str(i.is_blocked_by_viewer)}\n")
                        LOG.write(f"Biography : {builtins.str(i.biography)}\n")
                        LOG.write(f"Profile Picture URL : {builtins.str(i.profile_picture_url)}")
                        LOG.write("\n\r\n\r")
                        LOG.close()
                        break
                elif builtins.str(last_input) in ["n" , "N" , "no" , "No" , "NO"]:
                    break
            elif builtins.str(INPUT) in ["update-script" , "88"]:
                try:
                    os.chdir("Desktop")
                    subprocess.call(["git" , "clone" , "https://github.com/shervin-glitch/InstaInfo"])
                    print("[+] The New Script Directory is Cloned in Desktop")
                except Exception as Err:
                    os.chdir("Desktop")
                    subprocess.call(["git" , "clone" , "https://github.com/shervin-glitch/InstaInfo"])
                    print("[+] The New Script Directory is Cloned in Desktop")
                    raise Err
                finally:
                    print("\n")
                continue
            elif builtins.str(INPUT) in ["scripts/print-info" , "0"]:
                INPUT = builtins.str(input(f"\n\n{C[1]}[{C[3]}~{C[1]}] {C[1]}({C[5]}Inst4Inf0{C[1]})--$ \n{C[2]}[scripts/print-info] >{C[0]} "))
                i = instagramy.InstagramUser(INPUT)
                print(f"\n{C[1]}[{C[3]}Verified{C[1]}] {C[0]}: {C[2]}{builtins.str(i.is_verified)}")
                print(f"{C[1]}[{C[3]}Private{C[1]}] {C[0]}: {C[2]}{builtins.str(i.is_private)}")
                print(f"{C[1]}[{C[3]}Username{C[1]}] {C[0]}: {C[2]}@{builtins.str(INPUT)}")
                print(f"{C[1]}[{C[3]}Full name{C[1]}] {C[0]}: {C[2]}{builtins.str(i.fullname)}")
                print(f"{C[1]}[{C[3]}Recently Joined Instagram{C[1]}] {C[0]}: {C[2]}{builtins.str(i.is_joined_recently)}")
                print(f"{C[1]}[{C[3]}Follow Requested Other Pages{C[1]}] {C[0]}: {C[2]}{builtins.str(i.has_requested_viewer)}")
                print(f"{C[1]}[{C[3]}Followers{C[1]}] {C[0]}: {C[2]}{builtins.str(i.number_of_followers):,}")
                print(f"{C[1]}[{C[3]}Followings{C[1]}] {C[0]}: {C[2]}{builtins.str(i.number_of_followings):,}")
                print(f"{C[1]}[{C[3]}Posts{C[1]}] {C[0]}: {C[2]}{builtins.str(i.number_of_posts):,}")
                print(f"{C[1]}[{C[3]}Website{C[1]}] {C[0]}: {C[2]}{builtins.str(i.website)}")
                print(f"{C[1]}[{C[3]}Facebook Page{C[1]}] {C[0]}: {C[2]}{builtins.str(i.connected_fb_page)}")
                print(f"{C[1]}[{C[3]}Country Blocked User{C[1]}] {C[0]}: {C[2]}{builtins.str(i.has_country_block)}")
                print(f"{C[1]}[{C[3]}Blocked Any Instagram Users{C[1]}] {C[0]}: {C[2]}{builtins.str(i.has_blocked_viewer)}")
                print(f"{C[1]}[{C[3]}Blocked By Other Users{C[1]}] {C[0]}: {C[2]}{builtins.str(i.is_blocked_by_viewer)}")
                print(f"{C[1]}[{C[3]}Biography{C[1]}] {C[0]}: {C[2]}{builtins.str(i.biography)}")
                print(f"{C[1]}[{C[3]}Profile Picture Url{C[1]}] {C[0]}: {C[2]}{builtins.str(i.profile_picture_url)}")
                continue
            elif builtins.str(INPUT) in ["scripts/get-likes" , "1"]:
                INPUT = builtins.list(input(f"\n\n{C[1]}[{C[3]}~{C[1]}] {C[1]}({C[5]}Inst4Inf0{C[1]})--$ \n{C[2]}[scripts/get-likes] >{C[0]} ").split("/"))
                l = instagramy.InstagramPost(INPUT[4])
                print(f"\n{C[1]}[{C[3]}Author{C[1]}] {C[0]}: {C[2]}{builtins.str(l.author)}")
                print(f"\n{C[1]}[{C[3]}Post ID{C[1]}] {C[0]}: {C[2]}{builtins.str(INPUT[4])}")
                print(f"\n{C[1]}[{C[3]}Number Of Likes{C[1]}] {C[0]}: {C[2]}{builtins.str(l.number_of_likes):,}")
                continue
            elif builtins.str(INPUT) in ["scripts/get-comments" , "2"]:
                INPUT = builtins.list(input(f"\n\n{C[1]}[{C[3]}~{C[1]}] {C[1]}({C[5]}Inst4Inf0{C[1]})--$ \n{C[2]}[scripts/get-comments] >{C[0]} ").split("/"))
                l = instagramy.InstagramPost(INPUT[4])
                print(f"\n{C[1]}[{C[3]}Author{C[1]}] {C[0]}: {C[2]}{builtins.str(l.author)}")
                print(f"\n{C[1]}[{C[3]}Post ID{C[1]}] {C[0]}: {C[2]}{builtins.str(INPUT[4])}")
                print(f"\n{C[1]}[{C[3]}Number Of Comments{C[1]}] {C[0]}: {C[2]}{builtins.str(l.number_of_comments):,}")
                continue
            elif builtins.str(INPUT) in ["scripts/remover" , "3"]:
                INPUT = builtins.str(input(f"\n\n{C[1]}[{C[3]}~{C[1]}] {C[1]}({C[5]}Inst4Inf0{C[1]})--$ \n{C[2]}[scripts/{C[5]}REMOVER{C[2]}] >{C[0]} "))
                if platform.system() in ["Windows" , "Linux"]:
                    if os.path.exists(builtins.str(INPUT)):
                        if os.path.exists("%s\InstaInfo" % INPUT):
                            os.chdir(INPUT)
                            shutil.rmtree("InstaInfo")
                            print("[+] The Old Folder Successfully removed")
                            continue
                        else:
                            raise Exception
                    else:
                        print("Address Doesn't Exists")
                        continue
            elif builtins.str(INPUT) in ["clear" , "4"]:
                CheckSystem()
                continue
            else:
                print(f"{C[5]}[  !  ] Wrong Command")
                continue
    MainScript()
