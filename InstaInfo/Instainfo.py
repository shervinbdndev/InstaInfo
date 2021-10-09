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
        import io
        import sys
        import pip
        import random
        import builtins
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
              ::----=============--:.
        """

    def HeaderFunc():
        print(f"{H}")
        time.sleep(1.5)
    HeaderFunc()

    def MainScript():
        time.sleep(1.5)
        print(f"\n\n{C[1]}[{C[3]}Python Version{C[1]}] {C[0]}: {C[2]}{pip.__version__}")
        print(f"\n{C[1]}[{C[3]}Local IP{C[1]}] {C[0]}: {C[2]}{builtins.str(socket.gethostbyname(socket.gethostname()))}")
        print(f"\n{C[1]}[{C[3]}Public IP{C[1]}] {C[0]}: {C[2]}{LOAD['ip']}")
        print(f"\n{C[1]}[{C[3]}Country{C[1]}] {C[0]}: {C[2]}{LOAD['country']}")
        print(f"\n\n{C[0]}<-------------------------------------------------------------------->\n"
                      f"\n{C[3]}HELP"
                      f"\n{C[1]}help => {C[2]}Opening The Help Center\n"
                      f"\n\n{C[3]}SCRIPTS"
                      f"\n{C[1]}scripts/print-information => {C[2]}Setting The Username For Getting Page Information"
                      f"\n{C[1]}scripts/get-likes => {C[2]}Get Likes of a Post"
                      f"\n{C[1]}scripts/get-comments => {C[2]}Get comments of a Post"
                      f"\n\n{C[3]}OPTIONS"
                      f"\n{C[1]}options/version => {C[2]}Shows The Script's Version"
                      f"\n{C[1]}options/license => {C[2]}Shows The Script's License\n"
                      f"\n\n{C[3]}COMMANDS"
                      f"\n{C[1]}show-banner => {C[2]}Shows The Script banner"
                      f"\n{C[1]}update-script => {C[2]}Download The Latest Update Of Script"
                      f"\n{C[1]}exit => {C[2]}Exit the Script"
                      f"\n{C[0]}"
                      f"\n<-------------------------------------------------------------------->\n"
                )
        while True:
            INPUT = builtins.str(input(f"\n\n{C[1]}[{C[3]}~{C[1]}] {C[1]}({C[5]}Inst4Inf0{C[1]})--$ \n{C[2]}[~] >{C[0]} "))
            if builtins.str(INPUT) == "help" or builtins.str(INPUT) == "Help" or builtins.str(INPUT) == "HELP":
                print(f"\n\n{C[0]}<-------------------------------------------------------------------->\n"
                      f"\n{C[3]}HELP"
                      f"\n{C[1]}help => {C[2]}Opening The Help Center\n"
                      f"\n\n{C[3]}SCRIPTS"
                      f"\n{C[1]}scripts/print-information => {C[2]}Setting The Username For Getting Page Information"
                      f"\n{C[1]}scripts/get-likes => {C[2]}Get Likes of a Post"
                      f"\n{C[1]}scripts/get-comments => {C[2]}Get comments of a Post"
                      f"\n\n{C[3]}OPTIONS"
                      f"\n{C[1]}options/version => {C[2]}Shows The Script's Version"
                      f"\n{C[1]}options/license => {C[2]}Shows The Script's License\n"
                      f"\n\n{C[3]}COMMANDS"
                      f"\n{C[1]}show-banner => {C[2]}Shows The Script banner"
                      f"\n{C[1]}update-script => {C[2]}Download The Latest Update Of Script"
                      f"\n{C[1]}exit => {C[2]}Exit the Script"
                      f"\n{C[0]}"
                      f"\n<-------------------------------------------------------------------->\n"
                )
                continue
            elif builtins.str(INPUT) == "show-banner":
                HEADER = cfonts.render(text = "InstaInfo" , colors = [f"{random.choice(F)}" , f"{random.choice(F)}"] , align = "left")
                print(HEADER)
                continue
            elif builtins.str(INPUT) == "options/version":
                with io.open(file = "version.txt" , mode = "r") as V:
                    print(builtins.str(V.read(5)))
                    V.close()
                    continue
            elif builtins.str(INPUT) == "options/license":
                with io.open(file = "license.txt" , mode = "r") as L:
                    print(builtins.str(L.read(5055)))
                    L.close()
                    continue
            elif builtins.str(INPUT) == "exit" or builtins.str(INPUT) == "Exit" or builtins.str(INPUT) == "EXIT":
                last_input = builtins.str(input(f"{C[1]}[{C[3]}?{C[1]}] {C[0]}Do you want to save The Progress In log.txt ?"))
                if builtins.str(last_input) == "y" or builtins.str(last_input) == "Y" or builtins.str(last_input) == "yes" or builtins.str(last_input) == "Yes" or builtins.str(last_input) == "YES":
                    with io.open(file = r"{}".format("log/log.txt") , mode = "a" , encoding = "utf-8") as LOG:
                        LOG.write(f"Username : @{builtins.str(i.username)}\n")
                        LOG.write(f"Verified : {builtins.str(i.is_verified)}\n")
                        LOG.write(f"Private : {builtins.str(i.is_private)}\n")
                        LOG.write(f"Full name : {builtins.str(i.fullname)}\n")
                        LOG.write(f"Recently Joined Instagram : {builtins.str(i.is_joined_recently)}\n")
                        LOG.write(f"Follow Requested Other Pages : {builtins.str(i.has_requested_viewer)}\n")
                        LOG.write(f"Followers : {builtins.str(i.number_of_followers)}\n")
                        LOG.write(f"Followings : {builtins.str(i.number_of_followings)}\n")
                        LOG.write(f"Posts : {builtins.str(i.number_of_posts)}\n")
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
                elif builtins.str(last_input) == "n" or builtins.str(last_input) == "N" or builtins.str(last_input) == "no" or builtins.str(last_input) == "No" or builtins.str(last_input) == "NO":
                    break
            elif builtins.str(INPUT) == "update-script":
                try:
                    subprocess.call(["git" , "clone" , "https://github.com/shervin-glitch/InstaInfo"])
                    print("[+] The Script Directory is Cloned")
                except Exception as Err:
                    subprocess.call(["rm" , "-rf" , "InstaInfo"])
                    subprocess.call(["git" , "clone" , "https://github.com/shervin-glitch/InstaInfo"])
                    print("[+] The Script Directory is Cloned")
                    raise Err
                finally:
                    print("\n")
                continue
            elif builtins.str(INPUT) == "scripts/print-information":
                INPUT = builtins.str(input(f"\n\n{C[1]}[{C[3]}~{C[1]}] {C[1]}({C[5]}Inst4Inf0{C[1]})--$ \n{C[2]}[scripts/print-information] >{C[0]} "))
                i = instagramy.InstagramUser(INPUT)
                print(f"\n{C[1]}[{C[3]}Verified{C[1]}] {C[0]}: {C[2]}{builtins.str(i.is_verified)}")
                print(f"{C[1]}[{C[3]}Private{C[1]}] {C[0]}: {C[2]}{builtins.str(i.is_private)}")
                print(f"{C[1]}[{C[3]}Username{C[1]}] {C[0]}: {C[2]}@{builtins.str(INPUT)}")
                print(f"{C[1]}[{C[3]}Full name{C[1]}] {C[0]}: {C[2]}{builtins.str(i.fullname)}")
                print(f"{C[1]}[{C[3]}Recently Joined Instagram{C[1]}] {C[0]}: {C[2]}{builtins.str(i.is_joined_recently)}")
                print(f"{C[1]}[{C[3]}Follow Requested Other Pages{C[1]}] {C[0]}: {C[2]}{builtins.str(i.has_requested_viewer)}")
                print(f"{C[1]}[{C[3]}Followers{C[1]}] {C[0]}: {C[2]}{builtins.str(i.number_of_followers)}")
                print(f"{C[1]}[{C[3]}Followings{C[1]}] {C[0]}: {C[2]}{builtins.str(i.number_of_followings)}")
                print(f"{C[1]}[{C[3]}Posts{C[1]}] {C[0]}: {C[2]}{builtins.str(i.number_of_posts)}")
                print(f"{C[1]}[{C[3]}Website{C[1]}] {C[0]}: {C[2]}{builtins.str(i.website)}")
                print(f"{C[1]}[{C[3]}Facebook Page{C[1]}] {C[0]}: {C[2]}{builtins.str(i.connected_fb_page)}")
                print(f"{C[1]}[{C[3]}Country Blocked User{C[1]}] {C[0]}: {C[2]}{builtins.str(i.has_country_block)}")
                print(f"{C[1]}[{C[3]}Blocked Any Instagram Users{C[1]}] {C[0]}: {C[2]}{builtins.str(i.has_blocked_viewer)}")
                print(f"{C[1]}[{C[3]}Blocked By Other Users{C[1]}] {C[0]}: {C[2]}{builtins.str(i.is_blocked_by_viewer)}")
                print(f"{C[1]}[{C[3]}Biography{C[1]}] {C[0]}: {C[2]}{builtins.str(i.biography)}")
                print(f"{C[1]}[{C[3]}Profile Picture Url{C[1]}] {C[0]}: {C[2]}{builtins.str(i.profile_picture_url)}")
                continue
            elif builtins.str(INPUT) == "scripts/get-likes":
                INPUT = builtins.list(input(f"\n\n{C[1]}[{C[3]}~{C[1]}] {C[1]}({C[5]}Inst4Inf0{C[1]})--$ \n{C[2]}[scripts/get-likes] >{C[0]} ").split("/"))
                l = instagramy.InstagramPost(INPUT[4])
                print(f"\n{C[1]}[{C[3]}Number Of Likes{C[1]}] {C[0]}: {C[2]}{builtins.str(l.number_of_likes)}")
                continue
            elif builtins.str(INPUT) == "scripts/get-comments":
                INPUT = builtins.list(input(f"\n\n{C[1]}[{C[3]}~{C[1]}] {C[1]}({C[5]}Inst4Inf0{C[1]})--$ \n{C[2]}[scripts/get-comments] >{C[0]} ").split("/"))
                l = instagramy.InstagramPost(INPUT[4])
                print(f"\n{C[1]}[{C[3]}Number Of Comments{C[1]}] {C[0]}: {C[2]}{builtins.str(l.number_of_comments)}")
                continue
            else:
                print(f"{C[5]}[  !  ] Wrong Command")
                continue
    MainScript()
