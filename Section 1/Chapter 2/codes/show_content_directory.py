import os

pwd=os.getcwd()
list_dir = os.listdir(pwd)
for dir in list_dir:
    print(f"[+] {dir}")