import microcontroller, board, digitalio, analogio, busio, neopixel, time

def fahrenheit(degrees):
    return (degrees * (9 / 5)) + 32

def degrees(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)

def reading():
    CPU_TEMP_R = microcontroller.cpu.temperature
    CPU_TEMP_F = fahrenheit(CPU_TEMP_R)
    CPU_TEMP_C = degrees(CPU_TEMP_F)
    print("[INFO]:", "{}°C".format(int(CPU_TEMP_C)),
                     "{}°F".format(int(CPU_TEMP_F)),
                     "({}°C)".format(CPU_TEMP_R))
    return CPU_TEMP_R

reading()
print(dir(board))
RGB = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness = 0.1, auto_write = False)
RGB.fill((0xFF, 0x00, 0x07))
RGB.show()
time.sleep(1)

