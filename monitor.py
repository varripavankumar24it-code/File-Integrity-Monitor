import hashlib
import time
import os

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    
    try:
        with open(file_path, "rb") as f:
            while True:
                data = f.read(4096)
                if not data:
                    break
                sha256.update(data)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None


file_path = "test.txt"

# Create sample file if not exists
if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        f.write("Hello")

print("Monitoring file:", file_path)

old_hash = calculate_hash(file_path)

while True:
    time.sleep(5)  # check every 5 seconds
    new_hash = calculate_hash(file_path)

    if new_hash != old_hash:
        print("⚠ File Modified Detected!")
        old_hash = new_hash
    else:
        print("✔ No change detected")