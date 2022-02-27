#import
import time
from subprocess import check_output
import pathlib
import os

ruta = str(pathlib.Path().absolute())
directory_separator = os.path.sep
ruta_2 = ruta.split(os.path.sep)
if ruta_2[len(ruta_2) - 1] == "versión 1.0":
    pass
else:
    print("Error Fatal")
    exit()

check_output("cd " + ruta, shell=True)
check_output("pip install pyttsx3", shell=True)

time.sleep(5)