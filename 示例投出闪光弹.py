import serial, time

com_port = "COM21"
baud_rate = 115200
T1 = b"\xE0\x11\x01\x05\x31\x01\x00\x00\x00\x00"
T2 = b"\xE0\x11\x01\x01\x3C\x4F"

def p(led, r, g, b, bri):
    buf = bytearray(T1)
    buf[5:9] = led, min(int(r*bri),255), min(int(g*bri),255), min(int(b*bri),255)
    buf[9] = sum(buf[:9][1:]) & 0xff
    return buf

try:
    with serial.Serial(com_port, baud_rate, timeout=0.5) as s:
        print("💥 闪光弹已就绪！按下 Ctrl+C 停止（注意保护眼睛）")
        while True:            
            for i in range(8): 
                s.write(p(i, 255, 255, 255, 1.0))
            s.write(T2)
            time.sleep(0.02) # 20毫秒高频

            
            for i in range(8): 
                s.write(p(i, 0, 0, 0, 0))
            s.write(T2)
            time.sleep(0.02)
except KeyboardInterrupt:
    print("\n已撤收")
