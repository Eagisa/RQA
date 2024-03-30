#RQA_Installer_Version
#==============================#
RQA_INTR_Version = "100.0.0.1"
#==============================#

#RCC Packages
#====================================#
import requests
import os
from colorama import Fore,Back,init
init(autoreset=True)
import msvcrt
import os

def PTC():
        msvcrt.getch()

try:
    import RQA_CBS
except:
    print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> RQA_CBS import failed!\n")
    PTC()

try:
    import RQAM
except:
    print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> RQAM import failed!\n")
    PTC()

#Connection to the Hosting RCC Server
#==============================================================================#
RQA_S = "https://raw.githubusercontent.com/Eagisa/RQA/main/RQA_S/RQA-S.json"
#==============================================================================#

def RQA_INTR():
    def RQA_Installer():
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
            files_to_check = json_data['RQA-FS'].values()

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
            for key, value in json_data['RQA-FS'].items():
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
            print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> Successfully installed RCC-Files\n")
            os.system("cls")
            RQA_CBS_Updater()

        # Example usage:
        json_url = RQA_S
        missing_files = check_files_exist(json_url)
        debug = False
        if missing_files and not debug:
            os.system("cls")
            print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> Installing RCC-Files...\n")
            download_files_from_json(json_url)
            os.system("cls")
            RQA_CBS_Updater()

        else:
            os.system("cls")
            RQA_CBS_Updater()

    def Lauch_RQA():
        RQAM.StartRQA()

    def Lauch_RQA_Updater():
        RQA_CBS.RQA_Updater()

    def RQA_CBS_Updater():
        print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> Checking for updates...\n")
        url = RQA_S
        response = requests.get(url)
        data = response.json()
        server_ver = data.get("RQA-CBS", {}).get("Version")

        # Get local version directly from the imported module
        local_ver = RQA_CBS.RQA_CBS_Version

        # Check if the file exists
        if local_ver is not None:
            try:
                # Check if the local version matches the server version
                if local_ver != server_ver:
                    os.system("cls")
                    print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.Q.A ", Fore.LIGHTYELLOW_EX + "> Updating RQA_CBS...\n")

                    # URL to download RCC_CBS file from the JSON data
                    rcc_fs = data.get("RQA-FS", {})
                    rcc_cbs_url = rcc_fs.get("RQA_CBS")

                    if rcc_cbs_url:
                        # Save the downloaded file in the current directory
                        file_save_path = os.path.join(os.getcwd(), 'RQA_CBS.py')

                        # Download the file
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

    def download_file(url, save_path):
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)


    if __name__ == "__main__":
        try:
            print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> Connecting to RQA Server...\n")
            response = requests.head(RQA_S)
            if response.status_code == 200:
                RQA_Installer()
                PTC()
            else:
                os.system("cls")
                print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> Error couldn't connect to RQA Server!\n")
                PTC()
        except requests.ConnectionError:
            os.system("cls")
            print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.Q.A ", Fore.LIGHTYELLOW_EX+"> No internet , Please check your internet connection!\n")
            PTC()