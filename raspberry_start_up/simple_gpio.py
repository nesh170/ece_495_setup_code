from gpiozero import LED
from time import sleep
import subprocess

led_array = [LED(17),LED(27)];
wifi_LED = LED(22);

def turnOffAll():
	for leds in led_array:
		leds.off();

def checkWiFi(ssid):
        output = subprocess.check_output(['iwconfig', 'wlan0'])
        return (ssid in output)

while True:
	for leds in led_array:
		leds.on();
		sleep(1);
		turnOffAll();
		sleep(1);
        if(checkWiFi("litcrewz")):
                wifi_LED.on()
        else:
                wifi_LED.off()





