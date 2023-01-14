import os
import shutil
from pathlib import Path
print("you are copying files from your current working directory")
a = input("enter the path of the folder you want to copy to: ")
for folderName, subfolders, filenames in os.walk(Path.cwd()):
    for i in filenames:
        if i.endswith(".txt"):
            print(i)
            shutil.copy(os.path.join(str(folderName), i), a)
            