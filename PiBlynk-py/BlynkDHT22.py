from DHT_Python import dht22
from  oled96 import oled 
from PiBlynk import Blynk

# read data using pin 4
instance = dht22.DHT22(pin=4)

token = "---token---"
blynk = Blynk(token)
def cnct_cb():
	print ("Connected: ")
	
blynk.on_connect(cnct_cb)

def _funCb(ACT):
	result = instance.read()
	if result.is_valid():
		strTemp=("%.2f" % result.temperature)
		strHumi=("%.2f" % result.humidity)
		# Show temperature and humidity on OLED
		oled.yell2("Temp="+strTemp,"Humi="+strHumi) 
		blynk.virtual_write(1,strTemp) # User Virtual port V1
		blynk.virtual_write(2,strHumi) # User Virtual port V2
blynk.Ticker(_funCb, 140, False) # ~2 Hz

blynk.gpio_auto("button")

blynk.run()



