import hashlib
import os
def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while chunk := file.read(1024):
            sha256.update(chunk)
    return sha256.hexdigest()
def load_hashes():
    hashes = {}
    if os.path.exists("hashes.txt"):
        with open("hashes.txt", "r") as f:
            for line in f:
                path, hash_value = line.strip().split("|")
                hashes[path] = hash_value
    return hashes
def save_hash(file_path, hash_value):
    with open("hashes.txt", "a") as f:
        f.write(f"{file_path}|{hash_value}\n")
file_path = input("Enter file path: ").strip().strip('"')
if not os.path.exists(file_path):
    print("File not found ❌")
    exit()
new_hash = calculate_hash(file_path)
hashes = load_hashes()
if file_path in hashes:
    if hashes[file_path] == new_hash:
        print("File is SAFE ✅")
    else:
        print("WARNING ⚠️ File MODIFIED!")
else:
    save_hash(file_path, new_hash)
    print("Hash stored successfully ✅")