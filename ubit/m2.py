from microbit import *
import radio

# Timing settings
SECONDS_PER_MINUTE = 60
MILLISECONDS_PER_SECOND = 1000
MILLISECONDS_PER_MINUTE = SECONDS_PER_MINUTE * MILLISECONDS_PER_SECOND
SAMPLING_RATE = 25 
SAMPLING_INTERVAL = int(MILLISECONDS_PER_SECOND / SAMPLING_RATE)

radio.on()
radio.config(address=0x75626974)  # Bitte eigene Adresse verwenden
while True:
    incoming = radio.receive()
    if incoming is not None:
        display.show(incoming)  
        print(incoming)
        sleep(SAMPLING_INTERVAL)
        display.clear()