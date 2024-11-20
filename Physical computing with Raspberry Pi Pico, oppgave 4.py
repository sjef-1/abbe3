import machine
import utime

# Definer pinner
led_external = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Hovedløkken
while True:
    if button.value() == 1:  # Hvis knappen er trykket
        led_external.value(1)  # Slå på LED
        utime.sleep(2)         # Vent i 2 sekunder
        led_external.value(0)  # Slå av LED
