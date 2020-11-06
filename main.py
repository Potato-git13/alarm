#!/bin/python
import time
import beepy

print("Type HOUR:MINUTE:SECOND")
inp = input(time.strftime("%H:%M:%S") + ">")
while (time.strftime("%H:%M:%S") != inp):
    pass
beepy.beep(sound="ping")
