import subprocess;import sys;import builtins

class InstallDependencies:
    def __init__(self , *args , **kwargs) -> builtins.str:
        super(InstallDependencies , self).__init__(*args , **kwargs)
        self.executable = sys.executable
        self.interpreter = builtins.str("pip")

    def start(self):
        print("[+] Starting . . .")

    def update(self):
        subprocess.call([
            self.executable , "-m" , self.interpreter , "install" ,\
            "--upgrade" , self.interpreter
        ])

    def install(self , package : builtins.str):
        subprocess.call([
            self.executable , "-m" , self.interpreter ,\
            "install" , package
        ])

    def complete(self):
        print("[+] All Packages Installed")

if __name__ == "__main__":
    InstallDependencies().start()
    InstallDependencies().update()
    InstallDependencies().install("sockets")
    InstallDependencies().install("colorama")
    InstallDependencies().install("requests")
    InstallDependencies().install("instagramy")
    InstallDependencies().install("python-cfonts")
    InstallDependencies().complete()
