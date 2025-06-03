from machine import Pin, I2C, ADC
import sh1106
from framebuf import FrameBuffer, MONO_HLSB
from sprites import root
import time
import dht

dht_sensor = dht.DHT22(Pin(10))
soil_adc = ADC(Pin(1))
soil_adc.width(ADC.WIDTH_13BIT)
soil_adc.atten(ADC.ATTN_11DB)

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)
oled = sh1106.SH1106_I2C(128, 64, i2c, None, 0x3c)
oled.sleep(False)
oled.invert(0)

time.sleep(2)

def thick_hline(oled, x, y, width, thickness, color=1):
    for i in range(thickness):
        oled.hline(x, y + i, width, color)

def thick_vline(oled, x, y, height, thickness, color=1):
    for i in range(thickness):
        oled.vline(x + i, y, height, color)

def invert_fb_percent(fb, width, height, percent):
    lines_to_invert = int(height * percent / 100)
    for y in range(height - lines_to_invert, height):
        for x in range(width):
            current = fb.pixel(x, y)
            fb.pixel(x, y, 1 - current)

def draw_temperature(oled, temp, x, y, color=1):
    temp_str = str(temp)
    oled.text(temp_str, x, y, color)
    offset = len(temp_str) * 9
    oled.pixel(x + offset + 1, y, color)
    oled.pixel(x + offset + 2, y, color)
    oled.pixel(x + offset + 1, y + 3, color)
    oled.pixel(x + offset + 2, y + 3, color)
    oled.pixel(x + offset, y + 1, color)
    oled.pixel(x + offset, y + 2, color)
    oled.pixel(x + offset + 3, y + 1, color)
    oled.pixel(x + offset + 3, y + 2, color)
    oled.text("C", x + offset + 6, y, color)

while True:
    root_copy = bytearray(root)
    fb_root = FrameBuffer(root_copy, 80, 64, MONO_HLSB)
    invert_fb_percent(fb_root, 80, 64, 0)
    try:
        dht_sensor.measure()
        temperature_c = int(dht_sensor.temperature())
        humidity_percent = int(dht_sensor.humidity())
    except:
        temperature_c, humidity_percent = -1, -1

    soil_moisture = 100 - (soil_adc.read() * 100 // 8191)

    oled.fill(0)
    print("Soil Moisture:", soil_moisture)

    invert_fb_percent(fb_root, 80, 64, soil_moisture)
    oled.blit(fb_root, 0, 0)

    thick_vline(oled, 0, 0, 64, 3)
    thick_vline(oled, 77, 0, 64, 3)
    thick_vline(oled, 125, 0, 64, 3)
    thick_hline(oled, 0, 0, 128, 3)
    thick_hline(oled, 0, 61, 128, 3)
    thick_hline(oled, 80, 32, 48, 3)

    draw_temperature(oled, temperature_c, 87, 15)
    oled.text(f"{humidity_percent}%", 92, 45)
    oled.show()
    time.sleep(1)
