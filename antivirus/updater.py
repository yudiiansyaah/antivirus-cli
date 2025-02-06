import urllib.request

def update_virus_definitions(virus_defs_url, local_path="virus_definitions.txt"):
    try:
        print("Downloading virus definitions...")
        urllib.request.urlretrieve(virus_defs_url, local_path)
        print(f"Virus definitions updated successfully and saved to {local_path}")
    except Exception as e:
        print(f"Failed to update virus definitions: {e}")

