from machine import Pin
import dht
import time

# Sett opp DHT11-sensoren på GPIO15 (kan endres)
dht_sensor = dht.DHT11(Pin(15))

while True:
    try:
        # Les av data fra sensoren
        dht_sensor.measure()
        temp = dht_sensor.temperature()  # Temperatur i °C
        hum = dht_sensor.humidity()      # Fuktighet i %

        # Print resultatene til konsollen
        print("Temperatur: {}°C".format(temp))
        print("Fuktighet: {}%".format(hum))

    except OSError as e:
        print("Feil ved lesing fra DHT11-sensor:", e)

    # Vent 2 sekunder før neste måling
    time.sleep(2)
