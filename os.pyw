OS_KEY = "1.0U"
UI_KEY = "1.3E"
GAME_KEY = ['KEY = "RRAT"\n']

import os

def channel1():
    drive_connected = 1
    while 1:
        if drive_connected == 1:
            os.system("cls")
            print("not connected")
            drive_connected = 0
        if drive_connected == 2:
            try:
                KEY_CHECK = open("d:/disc.pyw", "r")
                DISC_KEY = KEY_CHECK.readlines(1)
                if DISC_KEY == GAME_KEY:
                    os.system("cls")
                    print("connected")
                    drive_connected = 3
                    TT = open("d:/disc.pyw", "r")
                    title = TT.read()[22:27]
                    print(f"title: {title}")
                    play = input("Play?: ")
                    if play == "yes":
                        os.system("cls")
                        FILES = open("d:/disc.pyw", "r")
                        exec(FILES.read(9000000))
                        print('The Software Has Closed Because An Error Occoured.')
                        os.system('pause')
                else:
                    if drive_connected == 2:
                        drive_connected = 4
                    if drive_connected == 4:
                        os.system("cls")
                        print('Unknown Disc')
                        drive_connected = 5

            except:
                if drive_connected == 2:
                        drive_connected = 4
                if drive_connected == 4:
                        os.system("cls")
                        print('Unknown Disc')
                        drive_connected = 5
        import win32file
        drive_list = []
        drivebits = win32file.GetLogicalDrives()
        for d in range(1, 26):
            mask = 1 << d
            if drivebits & mask:
                # here if the drive is at least there
                drname = '%c:\\' % chr(ord('A') + d)
                t = win32file.GetDriveType(drname)
                if t == win32file.DRIVE_REMOVABLE:
                    drive_list.append(drname)
        if drive_list == []:
            if drive_connected == 3:
                drive_connected = 1
            if drive_connected == 5:
                drive_connected = 1
        elif drive_list == ['D:\\']: 
            if drive_connected == 1:
                drive_connected = 2
            if drive_connected == 0:
                drive_connected = 2
def channel2():
    import urllib.request
    def connect(host='htttps://www.google.com'):
        try:
            urllib.request.urlopen(host) #Python 3.x
            return True
        except:
            return False
#    test
    print( "connected" if connect() else "no internet!" )
print("Avalible Channels:")
print('game channel')
print('shop channel')
print('settings channel')
chan = input()
if chan == 'game':
    channel1()
elif chan == "shop":
    channel2()