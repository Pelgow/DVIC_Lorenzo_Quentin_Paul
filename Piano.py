import network   #import des fonction lier au wifi
import urequests    #import des fonction lier au requetes http
import utime    #import des fonction lier au temps
import ujson    #import des fonction lier aà la convertion en Json

buzzer_pin = machine.Pin(15, machine.Pin.OUT)
led_pins = [machine.Pin(16, machine.Pin.OUT), machine.Pin(17, machine.Pin.OUT), machine.Pin(18, machine.Pin.OUT)]
#led_pin[0].value(1)  # allume la LED bleu
#led_pin[1].value(1)  # allume la LED vert
#led_pin[2].value(1)  # allume la LED rouge
#led_pin.value(0)  # éteint la LED


def play_note(frequency, duration):
    buzzer = machine.PWM(buzzer_pin)
    buzzer.freq(frequency)
    buzzer.duty_u16(32768)
    utime.sleep(duration)
    buzzer.duty_u16(0)
    buzzer.deinit()

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = "Paul's Galaxy S20 FE"
password = 'gratteur'
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "http://192.168.175.209:3000/play"

while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

last_note = None # initialise la variable pour stocker la dernière note jouée

while(True):
    try:
        print("GET")
        r = urequests.get(url) # lance une requete sur l'url
        note = r.json()["msg"]["note"]["freq"]
        print(r.json())# traite sa reponse en Json
        r.close() # ferme la demande
         # vérifie si la note est différente de la dernière note jouée
        if note < 300 :
            led_pins[0].value(1)  # allume la LED
            play_note(note, 0.2) # joue la nouvelle note
            led_pins[0].value(0)  # éteint la LED            utime.sleep(0.1) # temporisation d'une seconde
            last_note = note # met à jour la variable pour stocker la dernière note jouée
        elif 300 < note < 400 :
            led_pins[1].value(1)  # allume la LED
            play_note(note, 0.2) # joue la nouvelle note
            led_pins[1].value(0)  # éteint la LED            utime.sleep(0.1) # temporisation d'une seconde
            last_note = note # met à jour la variable pour stocker la dernière note jouée  
        else :
            led_pins[2].value(1)  # allume la LED
            play_note(note, 0.2) # joue la nouvelle note
            led_pins[2].value(0)  # éteint la LED            utime.sleep(0.1) # temporisation d'une seconde
            last_note = note # met à jour la variable pour stocker la dernière note jouée             

            

        utime.sleep(0.01)
    except Exception as e:
        print(e)