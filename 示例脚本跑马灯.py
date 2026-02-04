import serial, time, colorsys

com_port, baud = "COM21", 115200
T1 = b"\xE0\x11\x01\x05\x31\x01\x00\x00\x00\x00" 
T2 = b"\xE0\x11\x01\x01\x3C\x4F"

def p(led, r, g, b, bri):
    buf = bytearray(T1)
    buf[5:9] = led, min(int(r*bri),255), min(int(g*bri),255), min(int(b*bri),255)
    buf[9] = sum(buf[1:9]) & 0xff
    return buf

with serial.Serial(com_port, baud, timeout=0.5) as s:
    offset = 0.0
    print("🌈 彩虹旋转中... (Ctrl+C 退出)")
    while True:
        for i in range(8):
            # (offset - i/8) 实现顺时针旋转，0.4 为亮度
            rgb = colorsys.hsv_to_rgb((offset - i/8.0) % 1.0, 1.0, 1.0)
            s.write(p(i, rgb[0]*255, rgb[1]*255, rgb[2]*255, 0.4))
        
        s.write(T2)     # 发送生效指令
        offset += 0.005  # 增加此值可提速
        time.sleep(0.01)
