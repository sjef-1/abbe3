import machine
import utime
import _thread

# Definer pinner
led_red = machine.Pin(15, machine.Pin.OUT)
led_amber = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.Pin(12, machine.Pin.OUT)

# Global variabel for knappetrykk
button_pressed = False

# Funksjon for å lese knappetrykk i egen tråd
def button_reader_thread():
    global button_pressed
    while True:
        if button.value() == 1:  # Hvis knappen er trykket
            button_pressed = True
            utime.sleep(0.2)  # Debounce for knappen

# Start tråden for knappelesing
_thread.start_new_thread(button_reader_thread, ())

# Hovedløkken
while True:
    if button_pressed:  # Hvis knappen er trykket
        led_red.value(1)
        for i in range(10):  # Buzzer 10 ganger
            buzzer.value(1)
            utime.sleep(0.2)
            buzzer.value(0)
            utime.sleep(0.2)
        button_pressed = False  # Nullstill knappetrykk

    # Trafikklyssekvens
    led_red.value(1)
    utime.sleep(5)
    led_amber.value(1)
    utime.sleep(2)
    led_red.value(0)
    led_amber.value(0)
    led_green.value(1)
    utime.sleep(5)
    led_green.value(0)
    led_amber.value(1)
    utime.sleep(5)
    led_amber.value(0)
