#!/usr/bin/python

import random
import time
import subprocess
import threading
import signal
import sys
import os

WALLPAPERS_DIR = os.path.join(os.path.dirname(__file__), "wallpapers/")
INTERVAL_SECONDS = 60 * 10

def get_wallpapers():
    return [os.path.join(WALLPAPERS_DIR, i) for i in os.listdir(WALLPAPERS_DIR)]

def get_random_wallpaper():
    return random.choice(get_wallpapers())

def create_wallpaper_process(path):
    return os.getpgid(subprocess.Popen(
        "swaybg -m fill -i \""+path+"\"", 
        stdout=subprocess.PIPE, 
        shell=True,
        preexec_fn=os.setsid
    ).pid)

def send_wallpaper(path, interval):
    pid = create_wallpaper_process(path)
    time.sleep(interval)
    os.killpg(pid, signal.SIGTERM)

def main():
    args = sys.argv[1:]

    if len(args) == 1:
        if args[0] == "loop":
            while True:
                wallpapers = get_wallpapers()
                random.shuffle(wallpapers)
            
                for wallpaper in wallpapers:
                    thread = threading.Thread(
                        target = lambda: send_wallpaper(
                            wallpaper, 
                            INTERVAL_SECONDS + 1
                        )
                    )
                    thread.start()
                    time.sleep(INTERVAL_SECONDS)
            return
        elif args[0] == "onetime":
            create_wallpaper_process(get_random_wallpaper())
            while True:
                time.sleep(10)
            return
        
    print("Usage:", sys.argv[0], "<onetime/loop>")

if __name__ == "__main__":
    main()
