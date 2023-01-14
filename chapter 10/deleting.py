import os
import shutil
from pathlib import Path
a = input("enter path to folder: ")
for foldernames, subfolders, filenames in os.walk(a):
    for i in filenames:
        file = os.path.join(a,i)
        filesize = os.path.getsize(file)
        if filesize >= 104857600:
            print("this file will be deleted: " + file)
a = ''