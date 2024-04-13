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
from playsound import playsound
from winotify import Notification
import psutil
import subprocess
import winsound


def PTC():
    msvcrt.getch()

#Sound effects for RQA
#================================================================#
# Get the path to the LocalAppData folder
localappdata_path = os.environ.get('LOCALAPPDATA')
# Construct the path to the file within the RQA folder
Error_sound = os.path.join(localappdata_path, 'RQA', 'Error.mp3')
Res_sound = os.path.join(localappdata_path, 'RQA', 'Res.mp3')
#================================================================#

# Cookie instaler (Requires)
#================================================================================================================================================#
def Install_Cookie():
    # Get the LocalAppData directory
    local_app_data = os.environ.get('LOCALAPPDATA')
    if not local_app_data:
        print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> Error: LOCALAPPDATA environment variable not set.\n")
        playsound(Error_sound)
        PTC()
        return False
    
    config_dir = os.path.join(local_app_data, 'RQA')
    config_file_path = os.path.join(config_dir, 'Config.json')
    
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    os.system("cls")
    
    print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> Enter the valid cookie\n")
    cookie = input(Fore.LIGHTYELLOW_EX + "> ")

    if cookie.lower() == '`':
        os.system("cls")
        local_appdata = os.getenv('LOCALAPPDATA')
        pyc_file_path = os.path.join(local_appdata, 'RQA', 'RQAM.py')
        spec = importlib.util.spec_from_file_location("RQAM", pyc_file_path)
        RQAM = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(RQAM)
        RQAM.StartRQA()

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
        print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> Please wait, Verifying Cookies...\n")
        getuser = session.get("https://users.roblox.com/v1/users/authenticated")
        
        if getuser.status_code == 200:
            getuser2 = getuser.json()
            getuser4 = getuser2.get('name')
            os.system("cls")
            print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + f"> Congrats, Your Cookies are Validated!\n")
            playsound(Res_sound)
            time.sleep(1.3)
            
            try:
                # Read existing config data
                with open(config_file_path, 'r') as config_file:
                    existing_config_data = json.load(config_file)
                
                # Update existing config data with new key-value pair
                existing_config_data.update(config_data)
                
                # Write updated config data back to file
                with open(config_file_path, 'w') as config_file:
                    json.dump(existing_config_data, config_file, indent=4)
                
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
                print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> Error saving Config.json file:", e)
                return False
        else:
            os.system("cls")
            print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> That Cookies was invalied!\n")
            playsound(Error_sound)
            time.sleep(1.3)
            os.system("cls")
            Install_Cookie()
    except Exception as e:
        os.system("cls")
        print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + f"> Error couldn't authenticate {e}")
        playsound(Error_sound)
        time.sleep(1.3)
        os.system("cls")
        Install_Cookie()
#================================================================================================================================================#

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
                
                def Description():
                    if description == "":
                        print(Fore.LIGHTYELLOW_EX+"Description   : This user has no description")
                    else:
                        print(Fore.LIGHTYELLOW_EX+f"Description   : {description}")
                
                def PlayingCheck():
                    if userPresenceType == 0:
                        print(Fore.LIGHTYELLOW_EX+"Playing       : {User is Offline}")
                    else:
                        if playing_location == "":
                            print(Fore.LIGHTYELLOW_EX+"Playing       : {Encrypted}")
                        else:
                            print(Fore.LIGHTYELLOW_EX+f"Playing       : {playing_location}")
                
                def PlaceID_Check():
                    if userPresenceType == 0 or userPresenceType == 1 or userPresenceType == 3 or userPresenceType == 4:
                        print(Fore.LIGHTYELLOW_EX+"Placeid       : {User is not playing}")
                    else:
                        if userPresenceType == 2:
                            if place_id == None:
                                print(Fore.LIGHTYELLOW_EX+"Placeid       : {Encrypted}")
                            else:
                                print(Fore.LIGHTYELLOW_EX+f"Placeid       : {place_id}")
            
                #Prints the user information
                #=================================================================#
                print("")
                playsound(Res_sound)
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
                PlayingCheck()
                PlaceID_Check()
                print(Fore.LIGHTYELLOW_EX+f"LastOnline    : {User_Last_Online}")
                print(Fore.LIGHTYELLOW_EX+f"Created       : {created}")
                Description()
                print("")
                #=================================================================#
            else:
                print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> User doesn't exist.\n")
                playsound(Error_sound)
#===================================================================================================================================================#

# Group Join Request notifier, 
#=========================================================================================================================#
def Group_Join_Request_Notifier():
    # Authentication into Roblox account
    # Set User-Agent header
    user_agent = "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; en) Opera 9.27"
    session.headers["User-Agent"] = user_agent

    # Store already seen requester IDs to avoid duplicate notifications
    seen_requesters = set()

    #Loads Config.json "groupId"
    #==================================================================================#
    # Get the path to the local app data folder
    local_app_data = os.environ.get('LOCALAPPDATA')
    if local_app_data is None:
        print("Error: LOCALAPPDATA environment variable not found.")

    # Construct the path to the config.json file
    config_file_path = os.path.join(local_app_data, 'RQA', 'config.json')

    # Check if the config file exists
    if not os.path.exists(config_file_path):
        os.system("cls")
        print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"(RQA_Req) Error: config.json file not found.\n")
        PTC()
        exit()

    # Load the config file
    with open(config_file_path, 'r') as config_file:
        try:
            config_data = json.load(config_file)
            # Check if 'groupId' key exists in the config file
            if 'groupId' in config_data:
                group_id = config_data['groupId']

            else:
                os.system("cls")
                print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"You have not setup Group ID\n")
                time.sleep(1.3)
                os.system("cls")
                Start_Group_Setup()
        except json.JSONDecodeError:
            os.system("cls")
            print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"Unable to parse config.json file\n")
            PTC()
            exit()
    #==================================================================================#

    while True:
        try:
            # Make GET request to the provided API endpoint
            api_url = f"https://groups.roblox.com/v1/groups/{group_id}/join-requests?limit=100&sortOrder=Asc"
            response = session.get(url=api_url)
            
            # Check response status
            if response.status_code == 200:
                data = response.json()["data"]
                
                # Check if there are any join requests
                if data:
                    new_requesters = []

                    # Loop through each requester
                    for item in data:
                        requester_id = item["requester"]["userId"]
                        requester_username = item["requester"]["username"]
                        if requester_id not in seen_requesters:
                            new_requesters.append({"id": requester_id, "username": requester_username})
                            seen_requesters.add(requester_id)
                    
                    # Notify about new requesters
                    if new_requesters:
                        for requester in new_requesters:
                            print(f"New join request from user '{requester['username']}' (ID: {requester['id']})")
                            api_url = "https://thumbnails.roblox.com/v1/users/avatar-headshot"
                            # Define the parameters for the API request
                            params = {
                                "userIds": {requester['id']},
                                "size": "720x720",
                                "format": "Png",
                                "isCircular": "false"
                            }

                            # Send a GET request to the API
                            response = requests.get(api_url, params=params)

                            # Check if the request was successful
                            if response.status_code == 200:
                                # Extract the imageUrl from the API response
                                data = response.json()
                                imageUrl = data["data"][0]["imageUrl"]
                                
                                # Download the image
                                image_response = requests.get(imageUrl, stream=True)
                                if image_response.status_code == 200:
                                    # Define the path to the LocalAppData folder
                                    local_appdata_path = os.getenv('LOCALAPPDATA')
                                    # Define the path to the RQA folder within LocalAppData
                                    rqa_folder_path = os.path.join(local_appdata_path, 'RQA')
                                    # Define the path to the Data folder within RQA
                                    data_folder_path = os.path.join(rqa_folder_path, 'Data')
                                    
                                    # Create the RQA folder if it doesn't exist
                                    if not os.path.exists(rqa_folder_path):
                                        os.makedirs(rqa_folder_path)
                                    
                                    # Create the Data folder if it doesn't exist
                                    if not os.path.exists(data_folder_path):
                                        os.makedirs(data_folder_path)
                                    
                                    # Save the image to the Data folder
                                    image_path = os.path.join(data_folder_path, 'Profile.png')
                                    with open(image_path, 'wb') as file:
                                        image_response.raw.decode_content = True
                                        for chunk in image_response:
                                            file.write(chunk)
                                else:
                                    os.system("cls")
                                    image_eror = image_response.status_code
                                    print("Failed to load image. Status code:")
                                    PTC()
                                    exit()
                            else:
                                os.system("cls")
                                res_eror = response.status_code
                                print(f"Failed to fetch image URL from API. Status code: {res_eror}")
                                PTC()
                                exit()
                        
                        url = f"https://groups.roblox.com/v2/groups?groupIds={group_id}"
                        # Sending GET request to the API
                        response = requests.get(url)
                        # Parsing JSON response
                        data = response.json()
                        # Extracting name from the response
                        group_name = data["data"][0]["name"]

                        local_appdata_path = os.getenv('LOCALAPPDATA')
                        image_path = os.path.join(local_appdata_path, 'RQA', 'Data', 'Profile.png')

                        # Display notification with the downloaded image as the icon
                        toast = Notification(app_id="RQA Notifier",
                                            title=f"{group_name} New Join Request ",
                                            msg=f"{requester['username']}'s join request is pending",
                                            icon=image_path)
                        toast.show()
                        winsound.PlaySound("SystemNotification", winsound.SND_ALIAS)
                else:
                    # if there is no request it will pass and keep repeating...
                    pass

            else:
                print(f"API Status code: {response.status_code}\n")
                #print("Response:", response.text)
                print("You have insufficient permissions for this request.\n")
                print("Insufficient permissions to complete the request.\n")
                print("This account has no permission to manage the group.\n")
                PTC()

        except Exception as e:
            print(f"[Error] {e}\n")
            print("[Info] Your cookie is invalid")
            print("[Info] Please restart the program with a valid cookie")
        # Add a delay before the next iteration
        time.sleep(1)  # Adjust the delay as needed (in seconds)
#=========================================================================================================================#

# Group Features, Options
#========================================================================================================================#
def GroupFeatures():
    print(Fore.LIGHTYELLOW_EX+"           Group Features \n")
    print("",Back.LIGHTYELLOW_EX+Fore.BLACK+" 1 ",Fore.LIGHTYELLOW_EX+"> Setup Group ID (Required)\n")
    print("",Back.LIGHTYELLOW_EX+Fore.BLACK+" 2 ",Fore.LIGHTYELLOW_EX+"> Group Settings\n")
    
    while True:
        entry = input(Fore.LIGHTYELLOW_EX+"> ")

        if entry == "1":
            os.system("cls")
            Start_Group_Setup()
        
        elif entry == "2":
            os.system("cls")
            Group_Notifier_Settings()
        
        elif entry == "clear":
            os.system("cls")
            GroupFeatures()

        elif entry == '`':
            os.system("cls")
            local_appdata = os.getenv('LOCALAPPDATA')
            pyc_file_path = os.path.join(local_appdata, 'RQA', 'RQAM.py')
            spec = importlib.util.spec_from_file_location("RQAM", pyc_file_path)
            RQAM = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(RQAM)
            RQAM.StartRQA()
        else:
            print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> That was invailed!\n")
            playsound(Error_sound)
#========================================================================================================================#

# Setup Group ID
#======================================================================#
def Start_Group_Setup():
    def Group_ID_Setup(key, value):
        # Get the path to the LocalAppData directory
        local_app_data = os.getenv('LOCALAPPDATA')
        
        # Create the folder path if it doesn't exist
        folder_path = os.path.join(local_app_data, 'RQA')
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Define the full path to the config file
        config_file_path = os.path.join(folder_path, 'config.json')

        # Load existing config data if the file exists
        if os.path.exists(config_file_path):
            with open(config_file_path, 'r') as file:
                config_data = json.load(file)
        else:
            config_data = {}

        # Update the config data with the new key-value pair
        config_data[key] = value

        # Write the updated config data back to the file
        with open(config_file_path, 'w') as file:
            json.dump(config_data, file, indent=4)

    def get_numeric_input(prompt):
        while True:
            try:
                num = int(input(prompt))  # Convert input to integer
                os.system("cls")
                return num
            except ValueError:
                os.system("cls")
                print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"Please enter a valid group ID:\n")

    print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"Please enter a valid group ID:\n")
    enter_group_id = get_numeric_input(Fore.LIGHTYELLOW_EX+"> ")
    Group_ID_Setup('groupId', enter_group_id)
    GroupFeatures()
#======================================================================#

# Group Notifier Settings
#==================================================================================================================================================================#
def Group_Notifier_Settings():
    print("\n",Fore.LIGHTYELLOW_EX+"          Group Settings \n")

    def find_process(exe_name):
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == exe_name:
                return True
        return False

    exe_name = "RQA_Notifier.exe"  # Change this to the name of the .exe file you're looking for
    is_running = find_process(exe_name)

    if is_running == True:
        print("",Back.LIGHTYELLOW_EX+Fore.BLACK+" 1 ",Fore.LIGHTYELLOW_EX+f"> Notify New Join Request",Fore.BLACK+Back.LIGHTGREEN_EX+" Enabled ",Fore.BLACK+"Ro\n")
    else:
        print("",Back.LIGHTYELLOW_EX+Fore.BLACK+" 1 ",Fore.LIGHTYELLOW_EX+f"> Notify New Join Request",Fore.BLACK+Back.LIGHTRED_EX+" Disabled ",Fore.BLACK+"Ro\n")

    while True:
        entry = input(Fore.LIGHTYELLOW_EX+"> ")

        if entry == "clear":
            os.system("cls")
            Group_Notifier_Settings()

        elif entry == "disable=1" or entry == "d=1":
            def find_and_terminate_processes(exe_name):
                terminated = False
                while True:
                    found = False
                    for proc in psutil.process_iter(['pid', 'name']):
                        if proc.info['name'] == exe_name:
                            proc.terminate()
                            found = True
                    if not found:
                        break
                    terminated = True
                return terminated
            
            exe_name = "RQA_Notifier.exe"  # Change this to the name of the .exe file you're looking to terminate
            # Use this "terminated" to verify there is no problem
            #===================================================#
            terminated = find_and_terminate_processes(exe_name) 
            #===================================================#
            
            os.system("cls")
            Group_Notifier_Settings()
        
        elif entry == "enable=1" or entry == "e=1":
            localappdata_path = os.environ.get('LOCALAPPDATA')
            # Construct the path to the file within the RQA folder
            RQA_Notifier_Launcher = os.path.join(localappdata_path, 'RQA', 'RQA_Notifier.exe')
            # Execute the .exe file without capturing output
            subprocess.Popen(RQA_Notifier_Launcher)

            os.system("cls")  # This line might not be necessary if you want to keep the console output visible

            Group_Notifier_Settings()
        
        elif entry == "`":
            os.system("cls")
            GroupFeatures()
        
        else:
            print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> That was invalied!\n")
            playsound(Error_sound)
#==================================================================================================================================================================#