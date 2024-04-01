import requests
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import os
import importlib.util


def Get_User_Information():
    def get_user_data_by_username(username):
        url = "https://users.roblox.com/v1/usernames/users"
        data = {
            "usernames": [username],
            "excludeBannedUsers": True
        }
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            user_data = response.json()
            return user_data
        else:
            print(f"Error: {response.status_code}")
            return None

    print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> Enter a username\n")

    while True:
        username = input(Fore.LIGHTYELLOW_EX+"> ")
        
        # Check if the input is 'exit', then break the loop
        if username.lower() == '`':
            os.system("cls")
            local_appdata = os.getenv('LOCALAPPDATA')
            pyc_file_path = os.path.join(local_appdata, 'RQA', 'RQAM.py')
            spec = importlib.util.spec_from_file_location("RQAM", pyc_file_path)
            RQAM = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(RQAM)
            RQAM.StartRQA()
        
        user_data = get_user_data_by_username(username)
        if user_data:
            if user_data["data"]:  # Check if data list is not empty
                user_info = user_data["data"][0]
                id = user_info.get("id")
                name = user_info.get("name")
                displayName = user_info.get("displayName")
                hasVerifiedBadge = user_info.get("hasVerifiedBadge")
                print("")
                print(Fore.LIGHTYELLOW_EX+f"User ID       : {id}")
                print(Fore.LIGHTYELLOW_EX+f"Username      : {name}")
                print(Fore.LIGHTYELLOW_EX+f"DisplayName   : {displayName}")
                print(Fore.LIGHTYELLOW_EX+f"VerifiedBadge : {hasVerifiedBadge}")
                print("")
            else:
                print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> User doesn't exist.\n")