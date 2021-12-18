import os 

import time


print('Made by Brisk')


def split(f): # Checks if the path is the correct path
    try:
        t = f.split(chr(92))
        l = t[len(t)-1]
        if l.find('app-')>-1:
            return f
        else:
            return False
    except Exception:
        return False

def getpath(path): # Gets the path where Discord is located
    folders = list(os.walk(path))
    for f in folders:
        for f2 in f:
            spl = split(f2)
            if spl:
                return spl + '\Discord.exe'

def startdiscord(): # Attempts to start Discord automatically
    try:
        path = getpath(os.path.expanduser("~") + "\AppData\Local\Discord")
        os.startfile(path)
        quit()
    except Exception:
        print('[FAILED]: Attempt to start Discord')

def enddiscord(): # Attempts to end Discord automatically
    print("Attempting to kill Discord processes")
    try:
        os.system("taskkill /im discord.exe /F")
        return True

    except Exception:
        return False


if enddiscord():
    print('[SUCCESS]: Attempt to kill Discord processes')
    time.sleep(.5)
    print('Attempting to start Discord')
    startdiscord()
else:
    print('[FAILED]: Attempt to kill Discord processes,\nseems like Discord does not have a problem')
    time.sleep(.5)
    print('Attempting to start Discord')
    startdiscord()


input("Do not close this or it will cause Discord to close")
