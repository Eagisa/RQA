import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import os
import ctypes

# RCC COnfiguration
#======================#
RQA_version = "1.0.0.5"
RQA_RD = "04/1/2024"
#======================#

def StartRQA():
    #Console configuration
    #============================================================================================#
    def change_console_resolution(rows, columns):
        os.system(f"mode con: cols={columns} lines={rows}")

    def disable_console_resize():
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()

        # Retrieve the current window style
        style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)  # -16 corresponds to GWL_STYLE

        # Disable resizing (WS_THICKFRAME and WS_MAXIMIZEBOX)
        style = style & ~0x00040000  # 0x00040000 corresponds to WS_THICKFRAME
        style = style & ~0x00010000  # 0x00020000 corresponds to WS_MAXIMIZEBOX

        # Set the modified style
        ctypes.windll.user32.SetWindowLongW(hwnd, -16, style)

    disable_console_resize()
    #============================================================================================#

    change_console_resolution(20, 64)

    def title():
        print(Fore.LIGHTBLACK_EX+"<+>-----------------------<+>",           " ",Fore.LIGHTBLACK_EX+"<+>----------------------------------------------<+>")
        print("    "+Fore.BLACK+Back.CYAN +   f" RoQuickAcess v{RQA_version} "," ","        "+Fore.BLACK+Style.NORMAL+Back.GREEN + " UPDATE ",":",Fore.LIGHTYELLOW_EX+"Functioning..")
        print(Fore.LIGHTBLACK_EX+"<+>-----------------------<+>",                         " ",Fore.LIGHTBLACK_EX+"<+>----------------------------------------------<+>")
        print("\n")
        print("                       ",Back.LIGHTRED_EX+Fore.BLACK+" How to use ? ",Fore.BLACK+"[How to use?]")
        print(Fore.LIGHTBLACK_EX+"<+>------------------------------------------------------------<+>")
        print("  ",Back.RED+Fore.BLACK + " NOTE ",":",Fore.LIGHTYELLOW_EX + "Choose the number that you wanna access down below!")
        print(Fore.LIGHTBLACK_EX+"<+>------------------------------------------------------------<+>")
        print('\n')
        print("                           ",Back.LIGHTWHITE_EX+Fore.BLACK+" RoQuickAccess ",Fore.BLACK+"Ro")
        print(Fore.LIGHTBLACK_EX+"<+>-----------------------------------------------------------------<+>")
        print(Fore.LIGHTBLACK_EX+" |",Fore.LIGHTYELLOW_EX+"(1) -> Group Information",Fore.LIGHTBLACK_EX+"                      |"," ",Back.GREEN+Fore.BLACK+" Operational ",Fore.LIGHTBLACK_EX+" |",Fore.BLACK+"[Status]",)
        print(Fore.LIGHTBLACK_EX+" |------------------------------------------------|------------------|")
        print(Fore.LIGHTBLACK_EX+" |",Fore.LIGHTYELLOW_EX+"(2) -> Asset Information                      ",Fore.LIGHTBLACK_EX+"|"," ",Back.GREEN+Fore.BLACK+" Operational ",Fore.LIGHTBLACK_EX+" |",Fore.BLACK+"[Status]")
        print(Fore.LIGHTBLACK_EX+" |------------------------------------------------|------------------|")
        print(Fore.LIGHTBLACK_EX+" |",Fore.LIGHTYELLOW_EX+"(3) -> Send ItemAssets                        ",Fore.LIGHTBLACK_EX+"|"," ",Back.GREEN+Fore.BLACK+" Operational ",Fore.LIGHTBLACK_EX+" |",Fore.BLACK+"[Status]")
        print(Fore.LIGHTBLACK_EX+" |------------------------------------------------|------------------|")
        print(Fore.LIGHTBLACK_EX+" |",Fore.LIGHTYELLOW_EX+"(4) -> Get Group Roles",Fore.LIGHTBLACK_EX+"                        |"," ",Back.RED+Fore.BLACK+" Disruption  ",Fore.LIGHTBLACK_EX+" |",Fore.BLACK+"[Status]")
        print(Fore.LIGHTBLACK_EX+" |------------------------------------------------|------------------|")
        print(Fore.LIGHTBLACK_EX+" |",Fore.LIGHTYELLOW_EX+"(5) -> Get Group Description",Fore.LIGHTBLACK_EX+"                  |"," ",Back.RED+Fore.BLACK+" Disruption  ",Fore.LIGHTBLACK_EX+" |",Fore.BLACK+"[Status]")
        print(Fore.LIGHTBLACK_EX+" |------------------------------------------------|------------------|")
        print(Fore.LIGHTBLACK_EX+" |",Fore.LIGHTYELLOW_EX+"(6) -> Get Game Current Players",Fore.LIGHTBLACK_EX+"               |"," ",Back.RED+Fore.BLACK+" Disruption  ",Fore.LIGHTBLACK_EX+" |",Fore.BLACK+"[Status]")
        print(Fore.LIGHTBLACK_EX+"<+>-----------------------------------------------------------------<+>")
        print("\n")

    def main():
        #Main theme of the RoQuickAccess App
        title()

        while True:

            task = input(Fore.LIGHTYELLOW_EX+">:").strip()

            
            #Group Information
            if task == '1':
                print("Erro")

            #Asset Information
            elif task == '2':
                print("Erro")

            #Send Item to Discord
            elif task == '3':
                print("Not avaliable")

            elif task == '4':
                print("The Access was declined! (Due to issue or in-development)")
            
            elif task == '5':
                print("The Access was declined! (Due to issue or in-development)")
            
            elif task == '6':
                print("The Access was declined! (Due to issue or in-development)")

            #Restart the program
            elif task == 'clear':
                os.system("cls")
                main()
            #Print if something went wrong
            else:
                print('Sorry there is no',Fore.LIGHTYELLOW_EX+task,Fore.LIGHTYELLOW_EX+'command in system')



    main()