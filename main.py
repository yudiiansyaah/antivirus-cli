import os
import platform
from antivirus.banner import display_banner
from antivirus.scanner import full_device_scan
from antivirus.updater import update_virus_definitions

def main():
    display_banner()

    os_platform = platform.system()
    print(f"Running on {os_platform}!\n")

    # Main menu
    while True:
        print("Options:")
        print("1. Full device scan")
        print("q. Quit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            full_device_scan()
        elif choice.lower() == "q" and choice.upper() =="Q":
            print("Quitting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

