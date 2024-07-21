import os, sys

if len(sys.argv) == 2:
    filename=sys.argv[1]

    if not os.path.isfile(filename):
        print(f"[-] {filename} does not exists.")
        
    if not os.access(filename, os.F_OK):
        print(f"[-] {filename} access denied.")

    else:
        print("[+] {filename} exists")

else:
    print("Provide a file")
