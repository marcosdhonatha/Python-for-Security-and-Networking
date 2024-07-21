import os

count_files=0
for currentdir, dir, files in os.walk("."):
    count_files+= len(files)
print(f"The number os files in current directory is {count_files}")

