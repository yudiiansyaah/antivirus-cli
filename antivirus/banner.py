import platform
from termcolor import colored

def display_banner():

    banner_text2 = """
    Antivirus
    Created by
    """
    
    banner_text = """
    Y   Y  U   U  DDDD   SSSS
     Y Y   U   U  D   D  S
      Y    U   U  D   D  SSS
      Y    U   U  D   D     S
      Y     UUU   DDDD   SSSS
    """
    
    lolcat_banner = colored(banner_text, 'yellow')
    lolcat_message = colored("Check your device! Is there a virus\n", 'red')
    
    print(colored(banner_text2, 'green')) 
    print(lolcat_banner)
    print(lolcat_message)

    os_platform = platform.system()

    if os_platform == "Windows":
        print("Running on Windows!")
    elif os_platform == "Darwin":
        print("Running on macOS!")
    elif os_platform == "Linux":
        print("Running on Linux!")
    else:
        print(f"Unknown OS: {os_platform}")

