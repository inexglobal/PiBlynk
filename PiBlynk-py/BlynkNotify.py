from gpiozero import Button
from PiBlynk import Blynk
import time
token = "---token---"
blynk = Blynk(token)

SW_pin = 13
button = Button(SW_pin)

def cnct_cb():
	print ("Connected: ")
blynk.on_connect(cnct_cb)

def fun_notify():
	print("alert")
	blynk.notify("Alert")   # beep the smartphone

button.when_pressed = fun_notify 

blynk.gpio_auto("button")

blynk.run()



