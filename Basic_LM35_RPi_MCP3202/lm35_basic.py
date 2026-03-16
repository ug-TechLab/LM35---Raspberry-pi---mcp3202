import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1350000

def read_mcp3202(channel):
    adc = spi.xfer2([1,(2+channel)<<6,0])
    data = ((adc[1]&31)<<8)+adc[2]
    return data

while True:
    adc = read_mcp3202(0)
    voltage = adc*3.3/4095
    temperature = voltage*100

    print("Temperature : %.2f C"%temperature)

    time.sleep(2)
