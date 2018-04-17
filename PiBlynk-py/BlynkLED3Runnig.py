
from PiBlynk import Blynk
token = "---token---"
blynk = Blynk(token)

def cnct_cb():
    print ("Connected: ")
blynk.on_connect(cnct_cb)

blynk.gpio_auto("button")

blynk.run()



