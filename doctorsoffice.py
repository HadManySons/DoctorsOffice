import os
import subprocess
import random

#change me to path of the videos
directory = "/home/hadmanysons/Desktop/shows/"

videos = os.listdir(directory)

while True:
    try:
        tonights_feature = videos[random.randint(0, len(videos) - 1)]
        process = subprocess.Popen(["/usr/bin/vlc", directory + tonights_feature, "vlc://quit"])
        process.wait()
    except Exception as err:
        print("Something went wrong: " + err)
