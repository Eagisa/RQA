import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import os
import time
import requests
import importlib.util

# RQA COnfiguration
#======================#
RQA_version = "1.0.6.0"
RQA_RD = "04/1/2024"
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
    
    def menu():
        print("             ",Back.LIGHTWHITE_EX+Fore.BLACK+" Menu ",Fore.BLACK+"Ro")
        print(Fore.LIGHTBLACK_EX+"<+>----------------------------<+>")
        print(Fore.LIGHTBLACK_EX+" |",Fore.LIGHTYELLOW_EX+"(1) -> Get User Information",Fore.LIGHTBLACK_EX+" |")
        print(Fore.LIGHTBLACK_EX+" |------------------------------|")
        print(Fore.LIGHTBLACK_EX+" |",Fore.LIGHTYELLOW_EX+"(2) -> Coming soon...",Fore.LIGHTBLACK_EX+"       |")
        print(Fore.LIGHTBLACK_EX+" |------------------------------|")
        print(Fore.LIGHTBLACK_EX+" |",Fore.LIGHTYELLOW_EX+"(3) -> Coming soon...",Fore.LIGHTBLACK_EX+"       |")
        print(Fore.LIGHTBLACK_EX+" |------------------------------|")
        print(Fore.LIGHTBLACK_EX+" |",Fore.LIGHTYELLOW_EX+"(4) -> Coming soon...",Fore.LIGHTBLACK_EX+"       |")
        print(Fore.LIGHTBLACK_EX+"<+>----------------------------<+>")
        print("\n")

    def main():
        #Main theme of the RoQuickAccess App
        title()
        menu()

        while True:
            req_numer = input(Fore.LIGHTYELLOW_EX+"> ")

            if req_numer == '1':
                os.system("cls")
                RQA_Req.Get_User_Information()

            elif req_numer == '2':
                print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> Not-available\n")

            elif req_numer == '3':
                print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> Not-available\n")

            elif req_numer == '4':
                print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> Not-available\n")

            elif req_numer == 'clear':
                os.system("cls")
                main()

            else:
                print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> That was invailed!\n")

    main()