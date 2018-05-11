import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
for i in range(0,8):
	GPIO.setup(i+18, GPIO.OUT, initial=0)
time.sleep(2)
for i in range(7,-1,-1):
	GPIO.output(i+18, 1)
	time.sleep(1)
	GPIO.output(i+18,0)
