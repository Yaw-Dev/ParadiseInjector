import os
import sys
import psutil
from pyinjector import inject

os.system("title Paradise Injector")

while True:
    os.system("cls")
    print("Welcome to Paradise Injector!\n\nSelect an option:\n[1] Inject DLL\n[2] Github\n[3] Exit\n")
    user_choice = input(">> ")
    match user_choice:

        case '1':
            dll_to_inject = str(input("\n[>] Drag your DLL file here.\n>> "))
            if not dll_to_inject.endswith(".dll"):
                print("ERROR: Selected file is not a DLL!")
                print("\n[>] Press any key to retry...")
                os.system("pause > nul")
            elif not os.path.exists(dll_to_inject):
                print("ERROR: DLL file does not exist!")
                print("\n[>] Press any key to retry...")
                os.system("pause > nul")
            else:
                process_to_inject = str(input("[>] Enter a process to inject into.\n>> "))
                if not process_to_inject.endswith(".exe"): process_to_inject = process_to_inject + ".exe"

                process_found = False
                print("\n[+] Searching for game process...")
                for process in psutil.process_iter(attrs=['pid', 'name']):
                    try:
                        if process.info['name'] == process_to_inject:
                            process_id = process.info['pid']
                            process_name = process.info['name']
                            process_found = True
                    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        pass
                    
                if process_found:
                    #dll_to_inject = os.path.basename(dll_to_inject)
                    print(f"[+] Process {process_name} located at PID:{process_id}")
                    print("\nPress any key to inject!")
                    os.system("pause > nul")

                    try:
                        inject(process_id, dll_to_inject)
                        print(f"[+] Injected {dll_to_inject} into {process_name}:{process_id}")
                        print("\n[+] Enjoy!")

                    except Exception as e:
                        os.system("cls")
                        print("\nERROR: Injection failed!\n[-] Check error.log for more information.")
                        with open("error.log", "w") as errorfile:
                            errorfile.write(str(e))
                        print("\n[>] Press any key to retry...")
                    os.system("pause > nul")

                else:
                    print("[-] Failed to locate the game process.")
                    print("\n[>] Press any key to retry...")
                    os.system("pause > nul")

        case '2':
            os.system("start https://github.com/Yaw-Dev/ParadiseInjector")

        case '3':
            sys.exit(0)

        case _:
            print("[-] Invalid option!")
            print("\n[>] Press any key to retry...")
            os.system("pause > nul")