import requests
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import os
import importlib.util
import pytz
import json
from datetime import datetime
import msvcrt
import time

def PTC():
    msvcrt.getch()

#Install new valid cookies
#=================================================================================================================================================#
def Install_Cookie():
    # Get the LocalAppData directory
    local_app_data = os.environ.get('LOCALAPPDATA')
    if not local_app_data:
        print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> Error: LOCALAPPDATA environment variable not set.\n")
        return False
    config_dir = os.path.join(local_app_data, 'RQA')
    config_file_path = os.path.join(config_dir, 'Config.json')
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    os.system("cls")
    print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> Enter the valid cookie\n")
    cookie = input(Fore.LIGHTYELLOW_EX+"> ")

    # Session setup
    session = requests.Session()
    session.cookies[".ROBLOSECURITY"] = cookie
    req = session.post(url="https://auth.roblox.com/")
    if "X-CSRF-Token" in req.headers: 
        csrf_token = req.headers["X-CSRF-Token"]
        session.headers["X-CSRF-Token"] = csrf_token
    
    config_data = {"cookie": cookie}
    try:
        os.system("cls")
        print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> Please wait, Verifying Cookies...\n")
        getuser = session.get("https://users.roblox.com/v1/users/authenticated")
        if getuser.status_code == 200:
            getuser2 = getuser.json()
            getuser4 = getuser2.get('name')
            os.system("cls")
            print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+f"> Congrats, Your Cookies are Validated!\n")
            time.sleep(1.3)
            try:
                with open(config_file_path, 'w') as config_file:
                    json.dump(config_data, config_file, indent=4)
                local_appdata = os.getenv('LOCALAPPDATA')
                pyc_file_path = os.path.join(local_appdata, 'RQA', 'RQAM.py')
                spec = importlib.util.spec_from_file_location("RQAM", pyc_file_path)
                RQAM = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(RQAM)
                os.system("cls")
                RQAM.StartRQA()
                return True
            except Exception as e:
                os.system("cls")
                print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> Error saving Config.json file:", e)
                return False
        else:
            os.system("cls")
            print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> Your Cookies are invalied!\n")
            time.sleep(1.3)
            os.system("cls")
            Install_Cookie()
    except Exception as e:
        os.system("cls")
        print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+f"> Error couldn't authenticate {e}")
        time.sleep(1.3)
        os.system("cls")
        Install_Cookie()
#=================================================================================================================================================#

#loads Config.json file
#================================================================================================================================#
def load_config():
    # Get the LocalAppData directory
    local_app_data = os.environ.get('LOCALAPPDATA')
    if not local_app_data:
        print("Error: LOCALAPPDATA environment variable not set.")
        return None
    
    # Construct the path to the Config.json file
    config_file_path = os.path.join(local_app_data, 'RQA', 'Config.json')
    
    # Check if the Config.json file exists
    if not os.path.exists(config_file_path):
        print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> Error: Config.json file not found.")
        return None
    
    # Load and parse the Config.json file
    try:
        with open(config_file_path, 'r') as config_file:
            config_data = json.load(config_file)
        return config_data
    except Exception as e:
        print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> Error loading Config.json file:", e)
        return None
#================================================================================================================================#

# Loads the Config.json file
#=============================================#
config = load_config()
if config:
    cookie_value = config.get('cookie', '')
#=============================================#
    
#================================================================================#
session = requests.Session()
cookie = cookie_value # Replace "your_cookie_here" with your actual cookie value
session.cookies[".ROBLOSECURITY"] = cookie
req = session.post(url="https://auth.roblox.com/")
if "X-CSRF-Token" in req.headers: 
    csrf_token = req.headers["X-CSRF-Token"]
    session.headers["X-CSRF-Token"] = csrf_token  
#================================================================================#

# (Get User Information)
#===================================================================================================================================================#
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
                User_id = user_info.get("id")
                name = user_info.get("name")
                displayName = user_info.get("displayName")
                hasVerifiedBadge = user_info.get("hasVerifiedBadge")

                #Gets user detailed information by id
                #==========================================================#
                url = f"https://users.roblox.com/v1/users/{User_id}"
                response = requests.get(url)
                # Checking if request was successful (status code 200)
                if response.status_code == 200:
                    # Parsing JSON response
                    data = response.json()
                    is_banned = data.get("isBanned")
                    created = data.get("created")
                    description = data.get("description")
                #==========================================================#

                #=========================================================================================================================================#
                # Make request to Roblox API
                headers = {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                }

                data = {
                    "userIds": list({User_id})
                }

                response = session.post('https://presence.roblox.com/v1/presence/users', headers=headers, data=json.dumps(data))

                def convert_to_ist(timestamp):
                    # Parse the timestamp string
                    dt_object = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")

                    # Convert to UTC timezone
                    dt_object_utc = dt_object.replace(tzinfo=pytz.utc)

                    # Convert to IST timezone
                    dt_ist = dt_object_utc.astimezone(pytz.timezone('Asia/Kolkata'))

                    return dt_ist

                # Check if the request was successful (status code 200)
                if response.status_code == 200:
                    # Parse the response JSON
                    response_data = response.json()
                    # Extract and print the desired fields for each user presence
                    for user_presence in response_data.get('userPresences', []):
                        place_id = user_presence.get('placeId', user_presence.get('rootPlaceId'))  # Corrected key
                        playing_location = user_presence.get('lastLocation')
                        last_online = user_presence.get('lastOnline')
                        userPresenceType = user_presence.get('userPresenceType')

                        # Example timestamp
                        timestamp = last_online
                        # Convert to IST and print the result without seconds
                        ist_time = convert_to_ist(timestamp)
                        User_Last_Online = ist_time.strftime("%Y-%m-%d %I:%M %p")
                else:
                    print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> Presence API Error\n")
                #=========================================================================================================================================#


                # Inventory API
                #==========================================================================================================================#
                try:
                    response = session.get(f"https://inventory.roblox.com/v1/users/{User_id}/can-view-inventory")
                    if response.status_code == 200:
                        inventory_data = response.json()
                        can_view = inventory_data.get('canView')
                    else:
                        print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> Failed to fetch inventory data\n")
                        PTC()
                except Exception as e:
                    print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+f"> Error: {e}\n")
                    PTC()
                #==========================================================================================================================#

                # Friends/Following/Followers, API
                #============================================================================================#
                def get_user_counts(user_id):
                    urls = [
                        f"https://friends.roblox.com/v1/users/{user_id}/followers/count",
                        f"https://friends.roblox.com/v1/users/{user_id}/followings/count",
                        f"https://friends.roblox.com/v1/users/{user_id}/friends/count"
                    ]
                    counts = {}

                    for url in urls:
                        response = requests.get(url)
                        data = response.json()
                        count_type = url.split('/')[-2]
                        counts[count_type] = data.get("count", 0)

                    return counts

                user_player_id = User_id  # Replace with the desired user ID
                user_counts = get_user_counts(user_player_id)
                Followers = user_counts.get("followers", 0)
                Following = user_counts.get("followings", 0)
                Friends = user_counts.get("friends", 0)
                #============================================================================================#

                def User_Status():
                    if userPresenceType == 0:
                        print(Fore.LIGHTYELLOW_EX+f"UserStatus    : Offline")
                    elif userPresenceType == 1:
                        print(Fore.LIGHTYELLOW_EX+f"UserStatus    : Online")
                    elif userPresenceType == 2:
                        print(Fore.LIGHTYELLOW_EX+f"UserStatus    : InGame")
                    elif userPresenceType == 3:
                        print(Fore.LIGHTYELLOW_EX+f"UserStatus    : InStudio")
                    elif userPresenceType == 4:
                        print(Fore.LIGHTYELLOW_EX+f"UserStatus    : Invisible")


                #Prints the user information
                #=================================================================#
                print("")
                print(Fore.LIGHTYELLOW_EX+f"UserID        : {User_id}")
                print(Fore.LIGHTYELLOW_EX+f"Username      : {name}")
                print(Fore.LIGHTYELLOW_EX+f"DisplayName   : {displayName}")
                print(Fore.LIGHTYELLOW_EX+f"VerifiedBadge : {hasVerifiedBadge}")
                print(Fore.LIGHTYELLOW_EX+f"IsBanned      : {is_banned}")
                print(Fore.LIGHTYELLOW_EX+f"Followers     : {Followers}")
                print(Fore.LIGHTYELLOW_EX+f"Followings    : {Following}")
                print(Fore.LIGHTYELLOW_EX+f"Friends       : {Friends}")
                print(Fore.LIGHTYELLOW_EX+f"canView       : {can_view}")
                User_Status()
                print(Fore.LIGHTYELLOW_EX+f"Playing       : {playing_location}")
                print(Fore.LIGHTYELLOW_EX+f"Placeid       : {place_id}")
                print(Fore.LIGHTYELLOW_EX+f"LastOnline    : {User_Last_Online}")
                print(Fore.LIGHTYELLOW_EX+f"Created       : {created}")
                print(Fore.LIGHTYELLOW_EX+f"Description   : {description}")
                print("")
                #=================================================================#
            else:
                print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> User doesn't exist.\n")
#===================================================================================================================================================#