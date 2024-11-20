import machine
import utime

sensor_pir = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)
buzzer = machine.Pin(14, machine.Pin.OUT)

motion_detected = False  # Variable to track motion state

def pir_handler(pin):
    global motion_detected
    motion_detected = True  # Set motion detected to True
    print("ALARM! Motion detected!")
    for i in range(50):
        led.toggle()
        buzzer.toggle()
        utime.sleep_ms(100)

sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

while True:
    if motion_detected:
        motion_detected = False  # Reset motion detected after handling it
    else:
        print("Motion not detected")

    #led.toggle()
    utime.sleep(5)