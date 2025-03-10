#!/usr/bin/python

import random
import time
import subprocess
import threading
import sys
import os
import psutil

WALLPAPERS_DIR = os.path.join(os.path.dirname(__file__), "wallpapers/")
INTERVAL_SECONDS = 60 * 10

def get_wallpapers():
    return [os.path.join(WALLPAPERS_DIR, i) for i in os.listdir(WALLPAPERS_DIR)]

def get_random_wallpaper():
    return random.choice(get_wallpapers())

def create_wallpaper_process(path):
    process = subprocess.Popen(
        ["swaybg", "-m", "fill", "-i", path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return process

def send_wallpaper(path, interval):
    process = create_wallpaper_process(path)
    time.sleep(1)
    kill_old_processes(process.pid)
    time.sleep(interval-1)
    process.kill()
    
def kill_old_processes(new_pid):
    for proc in psutil.process_iter():
        if proc.pid != new_pid and proc.name() == "swaybg":
            print(proc.name(), proc.pid)
            proc.kill()

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
            process = create_wallpaper_process(get_random_wallpaper())
            while process.stdout.read() not in "1234567890-:_":
                time.sleep(1/60)
            if process.poll() is None:
                kill_old_processes(process.pid)
                process.wait()
            return
        
    print("Usage:", sys.argv[0], "<onetime/loop>")

if __name__ == "__main__":
    main()
