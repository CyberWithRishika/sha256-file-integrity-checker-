import hashlib

filename = input("Enter file path: ")

sha256_hash = hashlib.sha256()

try:
    with open(filename, "rb") as file:
        for block in iter(lambda: file.read(4096), b""):
            sha256_hash.update(block)

    generated_hash = sha256_hash.hexdigest()

print("\nGenerated SHA-256 Hash:")
print(generated_hash)

expected_hash = input("\nEnter expected hash (or press Enter to skip): ")

if expected_hash:
    if generated_hash == expected_hash:
        print("File integrity verified")
    else:
        print("Warning: File may have been modified")
except FileNotFoundError:
       print("file not found!")
