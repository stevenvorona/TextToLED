import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
time.sleep(5)
for i in range(18, 26):
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)

for i in range(0, 8):
    GPIO.output(i+18, 1)
    time.sleep(2)
    GPIO.output(i+18, 0)
    
