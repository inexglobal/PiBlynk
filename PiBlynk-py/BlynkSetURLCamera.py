import RPi.GPIO as GPIO
from PiBlynk import Blynk
token = "---token---"
blynk = Blynk(token)
def cnct_cb():
	print ("Connected: ")
blynk.on_connect(cnct_cb)
def geturl_ngrok():
	import os
	import http.client
	GET_IP_CMD ="hostname -I" # command get ip
	strStart='\\"URL\\":\\"http://'
	strEnd='.ngrok.io\\",'
	try:
		strlanght = len(strStart)
		conn = http.client.HTTPConnection("localhost", 4040)
		conn.request("GET", "/inspect/http")
		r1 = conn.getresponse()
		if r1.status==200:
			data1 = r1.read().decode('utf-8')   # This will return entire content.
			beg=data1.find(strStart)
			d=data1[beg+strlanght:]
			end = d.find(strEnd)
			d=d[0:end]
			if len(d) < 20 :
				return "http://%s.ngrok.io" % d
			else:
				len()
		conn.close()
	except:
		ip=os.popen(GET_IP_CMD).read()
		ip=ip.split(' ')
		ipLAN = ip[0]
		ipWiFi = ip[1]
		return "http://%s:8000" % ipLAN #Connect it with LAN.
		#return "http://%s:8000" % ipWiFi #Connect it with Wi-Fi.
def _funCb(ACT):
	url = "%s/stream.mjpg" % geturl_ngrok()
	print(url)
	blynk.set_property(4, "url",url)
blynk.Ticker(_funCb,1400, False) # ~7 second
blynk.gpio_auto("button")
blynk.run()



