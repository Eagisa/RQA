import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import os
import importlib.util
from playsound import playsound

# RQA COnfiguration
#======================#
RQA_version = "2.2.6.9"
RQA_RD = "04/12/2024"
#======================#

#Sound effects for RQA
#================================================================#
# Get the path to the LocalAppData folder
localappdata_path = os.environ.get('LOCALAPPDATA')
# Construct the path to the file within the RQA folder
Error_sound = os.path.join(localappdata_path, 'RQA', 'Error.mp3')
#================================================================#


local_appdata = os.getenv('LOCALAPPDATA')
pyc_file_path = os.path.join(local_appdata, 'RQA', 'RQA_Req.py')
spec = importlib.util.spec_from_file_location("RQA_Req", pyc_file_path)
RQA_Req = importlib.util.module_from_spec(spec)
spec.loader.exec_module(RQA_Req)

def StartRQA():
    def title():
        print("\n "+Fore.BLACK+Back.LIGHTBLUE_EX + f" RoQuickAcess v{RQA_version} "," ",""+Fore.BLACK+Style.NORMAL+Back.LIGHTGREEN_EX + " UPDATE ",Fore.LIGHTYELLOW_EX+"> New UI Update, Group Feature is still in-BETA")
        print("\n")
        print("",Back.LIGHTRED_EX+Fore.BLACK + " How to use ? ",">",Fore.LIGHTYELLOW_EX + "Choose an number to request")
        print('\n')

    def Show_Account_Authenticated():
        session = RQA_Req.session
        try:
            getuser = session.get("https://users.roblox.com/v1/users/authenticated")
            getuser2 = getuser.json()
            getuser4 = getuser2['name']
            print("",Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ",Fore.LIGHTYELLOW_EX+f"> Authentication Logged in as {getuser4}")
            print('\n')
        except Exception as e:
            print("",Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> Your cookies are invalid")
            print('\n')
            
    def menu():
        print("          ",Back.LIGHTYELLOW_EX+Fore.BLACK+" Menu ",Fore.BLACK+"Ro\n")
        print("",Back.LIGHTYELLOW_EX+Fore.BLACK+" 0 ",Fore.LIGHTYELLOW_EX+"> Install Cookies\n")
        print("",Back.LIGHTYELLOW_EX+Fore.BLACK+" 1 ",Fore.LIGHTYELLOW_EX+"> Get User Information\n")
        print("",Back.LIGHTYELLOW_EX+Fore.BLACK+" 2 ",Fore.LIGHTYELLOW_EX+"> Group Features\n")
        print("",Back.LIGHTYELLOW_EX+Fore.BLACK+" 3 ",Fore.LIGHTYELLOW_EX+"> Coming soon...\n")

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
                os.system("cls")
                RQA_Req.GroupFeatures()

            elif req_numer == '3':
                print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> Not-available\n")
                playsound(Error_sound)

            elif req_numer == 'clear':
                os.system("cls")
                main()

            else:
                print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> That was invailed!\n")
                playsound(Error_sound)

    main()