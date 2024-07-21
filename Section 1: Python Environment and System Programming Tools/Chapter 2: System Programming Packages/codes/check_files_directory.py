   
    
import os

for root, directorys, files in os.walk("."):
    print(f"Current directory: {root}")
    print(f"Subdirectorys: {directorys}")
    print(f"Files: {files}")
    print("------------------------------------------")

