import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
for i in range(0, 8):
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)

for i in range(0, 8):
    GPIO.output(i+18, 1)
    time.sleep(0.3)
    GPIO.output(i+18, 0)
    time.sleep(0.3)
