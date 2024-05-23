import os
import sys
from os import listdir, mkdir
from ..logging import LOGGER

def dirr():
    if "assets" not in listdir("AnonX"):
        LOGGER(__name__).warning("Assets Folder not Found. Please clone the repository again.")
        sys.exit()

    for file in listdir():
        if file.endswith((".jpg", ".jpeg")):
            os.remove(file)

    for folder in ["downloads", "cache"]:
        if folder not in listdir():
            mkdir(folder)

    LOGGER(__name__).info("Directories Updated.")
