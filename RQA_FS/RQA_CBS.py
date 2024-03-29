import requests
import os
from colorama import Fore,Back,init
init(autoreset=True)
import msvcrt
import os
import time
import importlib.util

#RQA_CBS Version
#=============================#
RQA_CBS_Version = "101.0.0.0"
#=============================#

#=============================================================================#
RQA_S = "https://raw.githubusercontent.com/Eagisa/RQA/main/RQA_S/RQA-S.json"
#=============================================================================#

def PTC():
    msvcrt.getch()

def RQA_Updater():
    # Function to download a file from a URL
    def download_file(url, filename):
        response = requests.get(url)
        with open(filename, 'wb') as file:
            file.write(response.content)

    # Fetching JSON data from the URL
    url = RQA_S
    response = requests.get(url)
    data = response.json()

    # Getting the version of RCC-C from the JSON object
    rqa_c_version = data.get("RQA-C", {}).get("Version")

    local_appdata = os.getenv('LOCALAPPDATA')
    pyc_file_path = os.path.join(local_appdata, 'RQA', 'RQAM.py')
    spec = importlib.util.spec_from_file_location("RQAM", pyc_file_path)
    RQAM = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(RQAM)

    RQA_ver = RQAM.RQA_version

    debug = False
    # Checking if the version matches
    if not rqa_c_version == RQA_ver and not debug:
        os.system("cls")
        print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> Updating RQA...\n")
        updater_info = data.get("RQA-FS", {}).get("RQAM")
        if updater_info:
            file_url = updater_info
            filename = os.path.basename(file_url)
            local_app_data_folder = os.path.join(os.environ["LOCALAPPDATA"], "RQA")
            destination_path = os.path.join(local_app_data_folder, filename)
            download_file(file_url, destination_path)
            os.system("cls")
            print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> You're up to date!\n")
            time.sleep(2)
            RQAM.StartRQA()
    else:
        RQAM.StartRQA()