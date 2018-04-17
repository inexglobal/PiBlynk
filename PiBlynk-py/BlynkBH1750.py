import smbus
bus = smbus.SMBus(1) #(512MB ro 1024MB)
addr = 0x23 # i2c adress
from  oled96 import oled 
from PiBlynk import Blynk
token = "---token---"
blynk = Blynk(token)
def cnct_cb():
	print ("Connected: ")
	
blynk.on_connect(cnct_cb)

def _funCb(ACT):
	# Read the light intensity from the BH1750
	data = bus.read_i2c_block_data(addr,0x10) 
	lux=(data[1] + (256 * data[0]) / 1.2)
	strLux=("%.2f" % lux)
	oled.yell(strLux) # Show light intensity on OLED
	blynk.virtual_write(0,strLux) # Use Virtual port V0
blynk.Ticker(_funCb, 140, False) # ~2 Hz

blynk.gpio_auto("button")

blynk.run()



