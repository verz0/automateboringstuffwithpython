from pathlib import Path
import glob
import re
 
loc = input("enter a path to the directory(with no sub folders in it): ")
loco = Path(loc)
regex = input("enter regex: ")
find = re.compile(regex)

for i in list(loco.glob('*.txt')):
    with open(i) as a:
        look= a.readlines()
        for e in look:
            if find.search(regex):
                print("found a match: " + e)
        
        

        