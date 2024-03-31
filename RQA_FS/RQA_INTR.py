#RQA_Installer_Version
#==============================#
RQA_INTR_Version = "100.0.0.2"
#==============================#

#RCC Packages
#====================================#
import requests
import os
from colorama import Fore,Back,init
init(autoreset=True)
import msvcrt

def PTC():
    msvcrt.getch()

def download_file(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)

def check_files_exist():
    # Files to check for existence
    files_to_check = ['RQAM.py', 'RQA_CBS.py']

    # Check if all files exist
    missing_files = []
    for filename in files_to_check:
        if not os.path.exists(filename):
            missing_files.append(filename)
    return missing_files

# Get LocalAppData directory
localappdata = os.getenv('LOCALAPPDATA')
rqa_folder = os.path.join(localappdata, 'RQA')

def RQA_INTR_Launcher():
    os.makedirs(rqa_folder, exist_ok=True)
    missing_files = check_files_exist()
    if missing_files:
        print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> Installing RQA-Files...\n")
        for filename in missing_files:
            file_url = f"https://raw.githubusercontent.com/Eagisa/RQA/main/RQA_FS/{filename}"
            file_save_path = os.path.join(rqa_folder, filename)
            download_file(file_url, file_save_path)

        os.system("cls")
        print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> Successfully installed RCC-Files\n")
        os.system("cls")
        RQA_CBS_Updater()
    else:
        os.system("cls")
        RQA_CBS_Updater()

def Lauch_RQA():
    try:
        import RQAM
    except ImportError:
        os.system("cls")
        print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> (RQA_INTR) Failed to import RQAM\n")
        PTC()
        exit()
    RQAM.StartRQA()

def Lauch_RQA_Updater():
    try:
        import RQA_CBS
    except ImportError:
        os.system("cls")
        print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> (RQA_INTR) Failed to import RQA_CBS\n")
        PTC()
        exit()
    RQA_CBS.RQA_Updater()

def RQA_CBS_Updater():
    print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> Checking for updates...\n")
    url = RQA_S
    response = requests.get(url)
    data = response.json()
    server_ver = data.get("RQA-CBS", {}).get("Version")

    try:
        import RQA_CBS
    except ImportError:
        os.system("cls")
        print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> (RQA_INTR) Failed to import RQA_CBS\n")
        PTC()
        exit()

    local_ver = RQA_CBS.RQA_CBS_Version

    if local_ver is not None:
        try:
            if local_ver != server_ver:
                os.system("cls")
                print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> Updating RQA_CBS...\n")

                rcc_fs = data.get("RQA-FS", {})
                rcc_cbs_url = rcc_fs.get("RQA_CBS")

                if rcc_cbs_url:
                    file_save_path = os.path.join(rqa_folder, 'RQA_CBS.py')
                    download_file(rcc_cbs_url, file_save_path)
                    os.system("cls")

                    print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> RQA_CBS is up to date\n")
                    Lauch_RQA_Updater()
                    Lauch_RQA()
                else:
                    os.system("cls")
                    print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> No RQA_CBS URL found in the JSON data.\n")
            else:
                Lauch_RQA_Updater()
                Lauch_RQA()

        except ImportError:
            print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> Failed to import RQA_CBS module\n")
        except AttributeError:
            print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> Attribute error in RQA_CBS module\n")
    else:
        print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> Error missing 'RQA_CBS' file\n")

# Connection to the Hosting RCC Server
RQA_S = "https://raw.githubusercontent.com/Eagisa/RQA/main/RQA_S/RQA-S.json"