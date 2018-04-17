# Python Program to Get IP Address
'''
import socket   
hostname = socket.gethostname()   
IPAddr = socket.gethostbyname(hostname)   
print("Your Computer Name is:" + hostname)   
print("Your Computer IP Address is:" + IPAddr)   

import subprocess 
GET_IP_CMD ="hostname -I" 
def run_cmd(cmd):
	return subprocess.check_output(cmd, shell=True).decode('utf-8') 
ip = run_cmd(GET_IP_CMD) 
print('ip:',ip) 
'''
GET_IP_CMD ="hostname -I" 
import os
ip=os.popen(GET_IP_CMD).read()
print('IPAd:',ip.strip())

