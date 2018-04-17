import RPi.GPIO as GPIO
import time
LED_pin = 25

GPIO.setwarnings(0)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_pin,GPIO.OUT)
print ('Start blinking LED')
while 1:
	GPIO.output(LED_pin,1)
	time.sleep(1)
	GPIO.output(LED_pin,0)
	time.sleep(1)


