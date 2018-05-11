import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
for i in range(18, 26):
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)

<<<<<<< HEAD
for i in range(0, 192, 8):
    bitstr=str("{0:08b}".format(i))
    print bitstr
    
    for i in range(7,-1,-1):
	if int(bitstr[i]) == 0:
		GPIO.output(i+18, 0)
	elif int(bitstr[i]) == 1:
		GPIO.output(i+18, 1)

	print int(bitstr[i])
=======
for i in range(0, 128):
    bitstr=str('0.08b'.format(i))
    for i in range(0, 8):
<<<<<<< HEAD
        GPIO.output(i+18, bit(bitstr[i]))
=======
        GPIO.output(i+18, int(bitstr[i]))
>>>>>>> 24ebc9d757173b34b61a8e4c220d393bff7c0b88
>>>>>>> df18b4d9a220ff7a1096e819266f0c2ebf2d52aa
    #waits 1 second before moving to the next LED
    time.sleep(1)
    for i in range(0, 8):
        GPIO.output(i+18, 0)
<<<<<<< HEAD
    
=======
'''
for i in range(0, 8):
    GPIO.output(i+18, 1)
    time.sleep(2)
    GPIO.output(i+18, 0)
'''
>>>>>>> 24ebc9d757173b34b61a8e4c220d393bff7c0b88
