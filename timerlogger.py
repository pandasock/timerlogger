from time import strftime

#how to use keyboard input? {ie; enter key 2 execute f'n}

#AUTOMATion of the f'ns via (lack of) keyboard input - no need to manually type
#
#How to detect mouse (scroll, click) and key input in python 4 MacOS?

def tIN():
    print(strftime("%m/%d/%y   on: %H:%M:%S\nWelcome!"))

def afk():
    print(strftime("%a, %b. %d  AFK: %H:%M:%S\n(far) away from keyboard"))


def brk():
    print(strftime("AFK: %H:%M:%S \nresting..."))

def res():
    print(strftime("%H:%M:%S \nrest ended. Welcome back!"))

def help():
    print("tIN: after logging in \nafk: getting up and walking away \nbrk: resting eyes by closing them \nres: ends break (brk)")
