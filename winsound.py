import winsound
import time

#range of frequency is from 37 to 32,767 hertz
freq = 500

# duration is in milliseconds
dur = 100

#simple beep sound
winsound.Beep(freq, dur)

#beep sound in a loop with delay of 2 seconds
for i in range(0,5):
    winsound.Beep(freq, dur)
    freq += 100
    dur += 100
    time.sleep(2)

#system alert sounds
winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)

#same as above 'SystemQuestion'
winsound.MessageBeep()

#it only supports .wav files
#winsound.PlaySound(a .wav file, flag)

#https://www.geeksforgeeks.org/python-winsound-module/
