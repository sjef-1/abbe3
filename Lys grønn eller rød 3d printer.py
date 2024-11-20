import urequests as requests
import time
import machine

# Konfigurer pinner for lysdiodene
green_led = machine.Pin(14, machine.Pin.OUT)  # Grønn diode
red_led = machine.Pin(15, machine.Pin.OUT)   # Rød diode

def connect():
    import network
    ssid = 'DATO IOT'
    password = 'Admin:123'
    # Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print('Waiting for connection...')
        time.sleep(1)
    print('Connected to WiFi!')

def update_leds(status):
    """
    Oppdaterer LED-ene basert på printerstatus.
    status: str, status fra printer API
    """
    if status == "Printing":
        red_led.on()     # Tenn rød diode
        green_led.off()  # Slå av grønn diode
    elif status == "Operational":  # Klar for ny jobb
        green_led.on()   # Tenn grønn diode
        red_led.off()    # Slå av rød diode
    else:
        green_led.off()  # Slå av begge dioder for ukjent status
        red_led.off()

# Main-program
def main():
    connect()

    #headers = {'X-Api-Key': '999C572FC32A423DBC102A2E56FF4B43'}
    #printer_url = 'http://10.13.37.25/api/'
    
    headers = {'X-Api-Key': 'D6DBFC5EFD954E7E89EF7400FF1D7565'}
    printer_url = 'http://10.13.37.24/api/'
    job_url = printer_url + 'job'

    while True:
        try:
            # Forespørsel til printer-API
            r = requests.get(job_url, headers=headers)
            data = r.json()

            # Hent status fra API-data
            status = data['state']
            print('Status:', status)
            print('Completion:', data['progress']['completion'])
            print('Estimated Print time:', data['job']['estimatedPrintTime'])
            print('File:', data['job']['file']['name'])

            # Oppdater lysdioder basert på status
            update_leds(status)

        except Exception as e:
            print("Error:", e)
            red_led.on()  # Tenn rød diode for feilindikasjon

        # Vent før neste oppdatering
        time.sleep(5)

# Kjør hovedprogrammet
main()