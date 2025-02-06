import hashlib

def get_file_hashes(file_path):
    hash_sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as file:
            while True:
                chunk = file.read(4096)
                if not chunk:
                    break
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

