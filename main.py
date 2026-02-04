# Copyright (C) 2026 Saya147
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License.
#
# Protocol logic inspired by MajdataPlay (LingFeng-bbben)

import serial, time

com_port = "COM21" #灯光的串口号
baud_rate = 115200
T1 = b"\xE0\x11\x01\x05\x31\x01\x00\x00\x00\x00" 
T2 = b"\xE0\x11\x01\x01\x3C\x4F"

def p(led, r, g, b, bri):
    buf = bytearray(T1)
    buf[5:9] = led, min(int(r*bri),255), min(int(g*bri),255), min(int(b*bri),255)
    buf[9] = sum(buf[:9][1:]) & 0xff
    return buf

led, r, g, b, bri = map(float, input("灯号(0-7),r,g,b,亮度: ").split(','))
led = int(led)

with serial.Serial(com_port, baud_rate, write_timeout=2, timeout=0.5) as s:
    time.sleep(0.1)
    s.write(p(led, r, g, b, bri))
    time.sleep(0.01)
    s.write(T2)


