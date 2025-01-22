import urllib.request

def update_virus_definitions(virus_defs_url, local_path="virus_definitions.txt"):
    """
    Update the local virus definitions by downloading from the provided URL.
    
    Args:
        virus_defs_url (str): URL from which to download the virus definitions.
        local_path (str): Path to save the downloaded virus definitions (default is 'virus_definitions.txt').
    """
    try:
        print("Downloading virus definitions...")
        urllib.request.urlretrieve(virus_defs_url, local_path)
        print(f"Virus definitions updated successfully and saved to {local_path}")
    except Exception as e:
        print(f"Failed to update virus definitions: {e}")

