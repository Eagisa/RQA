import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import os


RQA_version = "1.0.4"
RQA_RD = "3/30/2024"

def StartRQA():
    def title():
        print(Fore.LIGHTBLACK_EX+"<+>-----------------------<+>",           " ",Fore.LIGHTBLACK_EX+"<+>----------------------------------------------<+>")
        print("    "+Fore.BLACK+Back.CYAN +   f" RoQuickAcess v{RQA_version} "," ","        "+Fore.BLACK+Style.NORMAL+Back.GREEN + " UPDATE ",":",Fore.LIGHTYELLOW_EX+"More Feeatures will be added soon")
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

StartRQA()