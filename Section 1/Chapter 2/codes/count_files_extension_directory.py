import os
from collections import Counter

counts=Counter()

for root, dirnames, filenames in os.walk("."):
    for files in filenames:
        name, extension = os.path.splitext(files)
        counts[extension]+=1

for extension, a in counts.items():
    print(f"{extension:8}{a}")
    
    
