import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
for i in range(18, 26):
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)


for i in range(0, 200, 8):
    bitstr=str("{0:08b}".format(i))
    print bitstr

    for i in range(7,-1,-1):
	if int(bitstr[i]) == 0:
		GPIO.output(i+18, 0)
	elif int(bitstr[i]) == 1:
		GPIO.output(i+18, 1)
	print int(bitstr[i])
    time.sleep(0.5)
'''
for i in range(0, 128):
    bitstr=str('0.08b'.format(i))
    for i in range(0, 8):
        GPIO.output(i+18, bit(bitstr[i]))

        GPIO.output(i+18, int(bitstr[i]))
    #waits 1 second before moving to the next LED
    time.sleep(1)
    for i in range(0, 8):
        GPIO.output(i+18, 0)
'''
'''
for i in range(0, 8):
    GPIO.output(i+18, 1)
    time.sleep(2)
    GPIO.output(i+18, 0)
'''
