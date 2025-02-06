import os
import hashlib
from antivirus.utils import get_file_hashes

def scan_file(file_path):
    try:
        file_hash = get_file_hashes(file_path)
        print(f"Scanning file: {file_path} (Hash: {file_hash})")

        if file_hash == "dummy_hash":
            print(f"{file_path} is infected!")
        else:
            print(f"{file_path} is clean.")
    except Exception as e:
        print(f"Error scanning file {file_path}: {e}")

def scan_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            scan_file(file_path)

def full_device_scan():
    print("Performing full device scan...")

    os_platform = os.uname().sysname
    print(f"Running on {os_platform}!")


    if os_platform == "Linux":
        directories = ["/home", "/usr"]
    elif os_platform == "Darwin":  
        directories = ["/Users"]
    elif os_platform == "Windows":
        directories = [r"C:\Users", r"C:\Program Files"]
    else:
        print(f"Unsupported platform: {os_platform}")
        return

    for directory in directories:
        scan_directory(directory)


