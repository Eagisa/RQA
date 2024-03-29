#RCC Packages
#====================================#
import json
import requests
import subprocess
from os.path import exists
import shutil
import os
import urllib.request
from colorama import Fore,Back,init
init(autoreset=True)
import msvcrt
import tempfile
import webbrowser as web
import os
import sys
import importlib.util
#Connection to the Hosting RCC Server
#==============================================================================#
RCC_S = "https://raw.githubusercontent.com/Eagisa/RCC/main/RCC-Ss/RCC-S.json"
#==============================================================================#

def PTC():
        msvcrt.getch()

def RCC_Installer():
    def check_files_exist(json_url):
        debug = False
        # Fetch the JSON file
        response = requests.get(json_url)
        if response.status_code != 200 and not debug:
            print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+">Error: Couldn't fetch RQA-Files information.\n")
            exit()

        # Parse JSON data
        json_data = response.json()

        # Extract links and filenames
        files_to_check = json_data['RCC-FS'].values()

        # Check if all files exist
        missing_files = []
        for file_url in files_to_check:
            filename = os.path.basename(file_url)
            folder_path = os.path.join(os.getenv('LOCALAPPDATA'), 'RQA')
            file_path = os.path.join(folder_path, filename)
            if not os.path.exists(file_path):
                missing_files.append(filename)
        return missing_files

    def download_files_from_json(json_url):
        # Fetch the JSON file
        response = requests.get(json_url)
        if response.status_code != 200:
            print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> Error couldn't connect to RQA-CBS\n")
            exit()

        # Parse JSON data
        json_data = response.json()

        # Extract links and filenames
        files_to_download = []
        for key, value in json_data['RCC-FS'].items():
            filename = os.path.basename(value)  # Extract filename from URL
            files_to_download.append({'url': value, 'filename': filename})

        # Download files
        download_files(files_to_download)

    def download_files(files_to_download):
        folder_path = os.path.join(os.getenv('LOCALAPPDATA'), 'RQA')
        os.makedirs(folder_path, exist_ok=True)
        for file_info in files_to_download:
            url = file_info['url']
            filename = file_info['filename']
            file_path = os.path.join(folder_path, filename)
            # Check if file already exists, if yes, skip download
            if os.path.exists(file_path):
                pass
                continue
            response = requests.get(url, stream=True)
            with open(file_path, 'wb') as f:
                for data in response.iter_content(chunk_size=4096):
                    f.write(data)

        os.system("cls")
        print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> Successfully installed RQA-Files\n")
        os.system("cls")
        RCC_CBS_Updater()

    # Example usage:
    json_url = RCC_S
    missing_files = check_files_exist(json_url)
    debug = False
    if missing_files and not debug:
        os.system("cls")
        print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> Installing RQA-Files...\n")
        download_files_from_json(json_url)
        os.system("cls")
        RCC_CBS_Updater()

    else:
        os.system("cls")
        RCC_CBS_Updater()

def Lauch_RCC():
    local_appdata = os.getenv('LOCALAPPDATA')
    pyc_file_path = os.path.join(local_appdata, 'RCC', 'RCCMP.py')
    spec = importlib.util.spec_from_file_location("RCCMP", pyc_file_path)
    RCCMP = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(RCCMP)

    RCCMP.StartRCC()



def Lauch_RCC_Updater():
    local_appdata = os.getenv('LOCALAPPDATA')
    pyc_file_path = os.path.join(local_appdata, 'RCC', 'RCC_CBS.py')
    spec = importlib.util.spec_from_file_location("RCC_CBS", pyc_file_path)
    RCC_CBS = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(RCC_CBS)

    RCC_CBS.RCC_Updater()

def RCC_CBS_Updater():
    print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> Checking for updates...\n")
    url = RCC_S
    response = requests.get(url)
    data = response.json()
    server_ver = data.get("RCC-CBS", {}).get("Version")

    local_appdata = os.getenv('LOCALAPPDATA')
    pyc_file_path = os.path.join(local_appdata, 'RCC', 'RCC_CBS.py')
    spec = importlib.util.spec_from_file_location("RCC_CBS", pyc_file_path)
    RCC_CBS = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(RCC_CBS)

    local_ver = RCC_CBS.RCC_CBS_Ver

    # Check if the file exists
    if os.path.exists(pyc_file_path):
        # Add the directory containing RCC_CBS.pyc to the Python path
        sys.path.append(os.path.dirname(pyc_file_path))
        try:
            # Check if the local version matches the server version
            if local_ver != server_ver:
                os.system("cls")
                print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> Updating RQA_CBS...\n")
                
                # URL to download RCC_CBS file from the JSON data
                rcc_fs = data.get("RCC-FS", {})
                rcc_cbs_url = rcc_fs.get("RCC_CBS")

                if rcc_cbs_url:
                    # Path to save the downloaded file
                    file_save_path = os.path.join(local_appdata, 'RCC', 'RCC_CBS.py')

                    # Download the file
                    download_file(rcc_cbs_url, file_save_path)
                    os.system("cls")
                    print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> RQA_CBS is up to date\n")
                    Lauch_RCC_Updater()
                    Lauch_RCC()
                else:
                    os.system("cls")
                    print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> No RQA_CBS URL found in the JSON data.\n")
            else:
                Lauch_RCC_Updater()
                Lauch_RCC()

        except ImportError:
            print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> Failed to import RQA_CBS module\n")
        except AttributeError:
            print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> Attribute error in RQA_CBS module\n")
    else:
        print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> Error missing 'RQA_CBS' file\n")

def download_file(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)


if __name__ == "__main__":
    try:
        print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> Connecting to RQA Server...\n")
        response = requests.head(RCC_S)
        if response.status_code == 200:
            RCC_Installer()
            PTC()
        else:
            os.system("cls")
            print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> Error couldn't connect to RQA Server!\n")
            PTC()
    except requests.ConnectionError:
        os.system("cls")
        print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> No internet , Please check your internet connection!\n")
        PTC()