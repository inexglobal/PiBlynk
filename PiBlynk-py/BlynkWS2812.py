from PiBlynk import Blynk
from neopixel import *
token = "---token---"
blynk = Blynk(token)

# LED strip configuration:
LED_COUNT      = 1       # Number of LED pixels.
LED_PIN        = 12      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT,LED_PIN,LED_FREQ_HZ,LED_DMA, LED_INVERT, LED_BRIGHTNESS)
# Intialize the library (must be called once before other functions).
strip.begin()

def virt_in_h(val, pin,st):  
	print("Incoming on VP: %d , %s" % (pin, val))
	if pin==3:
		R=int(val[1]) # Red
		G=int(val[0]) # Green 
		B=int(val[2]) # Blue
		strip.setPixelColor(0, Color(R,G,B))
		strip.show()
blynk.add_virtual_pin(3,write=virt_in_h)   # we place a LISTEN for incoming writes on V3

def cnct_cb():
	print ("Connected: ")
blynk.on_connect(cnct_cb)
blynk.gpio_auto("button")
blynk.run()


