import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import os
import importlib.util

# RQA COnfiguration
#======================#
RQA_version = "1.2.5.5"
RQA_RD = "04/05/2024"
#======================#


local_appdata = os.getenv('LOCALAPPDATA')
pyc_file_path = os.path.join(local_appdata, 'RQA', 'RQA_Req.py')
spec = importlib.util.spec_from_file_location("RQA_Req", pyc_file_path)
RQA_Req = importlib.util.module_from_spec(spec)
spec.loader.exec_module(RQA_Req)

def StartRQA():
    def title():
        print(Fore.LIGHTBLACK_EX+"<+>-------------------------<+>",           " ",Fore.LIGHTBLACK_EX+"<+>---------------------------------------------------------------<+>")
        print("    "+Fore.BLACK+Back.LIGHTBLUE_EX +   f" RoQuickAcess v{RQA_version} "," ","        "+Fore.BLACK+Style.NORMAL+Back.LIGHTGREEN_EX + " UPDATE ",":",Fore.LIGHTYELLOW_EX+"RQA is still in-BETA, more updates will come soon!")
        print(Fore.LIGHTBLACK_EX+"<+>-------------------------<+>",                         " ",Fore.LIGHTBLACK_EX+"<+>---------------------------------------------------------------<+>")
        print("\n")
        print(Fore.LIGHTBLACK_EX+"<+>----------------------------------------------<+>")
        print("   ",Back.LIGHTRED_EX+Fore.BLACK + " How to use ? ",">",Fore.LIGHTYELLOW_EX + "Choose an number to request")
        print(Fore.LIGHTBLACK_EX+"<+>----------------------------------------------<+>")
        print('\n')

    def Show_Account_Authenticated():
        session = RQA_Req.session
        try:
            getuser = session.get("https://users.roblox.com/v1/users/authenticated")
            getuser2 = getuser.json()
            getuser4 = getuser2['name']
            print(Fore.LIGHTBLACK_EX+"<+>-------------------------------------------------<+>")
            print("   ",Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ",Fore.LIGHTYELLOW_EX+f"> Authentication Logged in as {getuser4}")
            print(Fore.LIGHTBLACK_EX+"<+>-------------------------------------------------<+>\n")
        except Exception as e:
            print(Fore.LIGHTBLACK_EX+"<+>-----------------------------------------------------------<+>")
            print("   ",Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> Your cookies are invalid")
            print(Fore.LIGHTBLACK_EX+"<+>-----------------------------------------------------------<+>\n")
            
    def menu():
        print("             ",Back.LIGHTWHITE_EX+Fore.BLACK+" Menu ",Fore.BLACK+"Ro")
        print(Fore.LIGHTBLACK_EX+"<+>----------------------------<+>")
        print(Fore.LIGHTBLACK_EX+" |",Fore.LIGHTYELLOW_EX+"(0) -> Install Cookies",Fore.LIGHTBLACK_EX+"      |")
        print(Fore.LIGHTBLACK_EX+" |------------------------------|")
        print(Fore.LIGHTBLACK_EX+" |",Fore.LIGHTYELLOW_EX+"(1) -> Get User Information",Fore.LIGHTBLACK_EX+" |")
        print(Fore.LIGHTBLACK_EX+" |------------------------------|")
        print(Fore.LIGHTBLACK_EX+" |",Fore.LIGHTYELLOW_EX+"(2) -> Coming soon...",Fore.LIGHTBLACK_EX+"       |")
        print(Fore.LIGHTBLACK_EX+" |------------------------------|")
        print(Fore.LIGHTBLACK_EX+" |",Fore.LIGHTYELLOW_EX+"(3) -> Coming soon...",Fore.LIGHTBLACK_EX+"       |")
        print(Fore.LIGHTBLACK_EX+"<+>----------------------------<+>")
        print("\n")

    def main():
        #Main theme of the RoQuickAccess App
        title()
        Show_Account_Authenticated()
        menu()

        while True:
            req_numer = input(Fore.LIGHTYELLOW_EX+"> ")

            #Install Cookies
            if req_numer == '0':
                os.system("cls")
                RQA_Req.Install_Cookie()
            
            #Get User Information
            elif req_numer == '1':
                os.system("cls")
                RQA_Req.Get_User_Information()

            elif req_numer == '2':
                print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> Not-available\n")

            elif req_numer == '3':
                print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> Not-available\n")

            elif req_numer == 'clear':
                os.system("cls")
                main()

            else:
                print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> That was invailed!\n")

    main()