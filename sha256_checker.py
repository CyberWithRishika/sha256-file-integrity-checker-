import hashlib

filename = input("Enter file path: ")

sha256_hash = hashlib.sha256()

try:
    with open(filename, "rb") as file:
        for block in iter(lambda: file.read(4096), b""):
            sha256_hash.update(block)

    print("\nSHA-256 Hash:")
    print(sha256_hash.hexdigest())

except FileNotFoundError:
    print("File not found!")
