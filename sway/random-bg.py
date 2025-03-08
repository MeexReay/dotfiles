#!/usr/bin/python

import random
import time
import subprocess
import threading
import signal
import os

WALLPAPERS_DIR = os.path.join(os.path.dirname(__file__), "wallpapers/")
INTERVAL_SECONDS = 60 * 10

def get_wallpapers():
    return [os.path.join(WALLPAPERS_DIR, i) for i in os.listdir(WALLPAPERS_DIR)]

def get_random_wallpaper():
    return random.choice(get_wallpapers())

def send_wallpaper(path, interval):
    process = subprocess.Popen(
        "swaybg -m fill -i \""+path+"\"", 
        stdout=subprocess.PIPE, 
        shell=True,
        preexec_fn=os.setsid
    ) 

    time.sleep(interval)
    os.killpg(os.getpgid(process.pid), signal.SIGTERM)

def main():
    while True:
        thread = threading.Thread(
            target = lambda: send_wallpaper(
                get_random_wallpaper(), 
                INTERVAL_SECONDS + 1
            )
        )
        thread.start()
        time.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    main()
