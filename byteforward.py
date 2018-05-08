import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#Configs all rpi outputs to low

for i in range(0, 8):
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)

#Takes in coords and converst to coordbits (a list of bits to forward to the FPGA)
coords = {}
coords.append([0,0])
coordbits = {}
coordbits = coordToBitString(coords)

<<<<<<< HEAD
=======
n = 0
lit = len(coordbits)
while True:
    try:
        pushOneBitString(coordbits[n])
	n=n+1

def pushOneBitString(bitstr):
    #bitstr is 8 concatenated bits
    for i in range(0, 8):
        GPIO.output(i, int(bitstr[i]))

#Input a list of lists in format (xlayer1, y1),(xlayer2, y2),...., (xlayern,yn)
def coordToBitString(*argv):
  cordlist = { }
  for arg in argv:
    cordlist.append(str('0.05b'.format(arg[0]))+""+str('0.03b'.format(arg[1])))
  return cordlist
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#Configs all rpi outputs to low

for i in range(0, 8):
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)

#Takes in coords and converst to coordbits (a list of bits to forward to the FPGA)
coords = {}
coords.append([0,0])
coordbits = {}
coordbits = coordToBitString(coords)

>>>>>>> 8563d578b5b6fba2891116634b781a5ff18880dc

while True:
    lit = len(coordbits)
    try:
        coor

def pushOneBitString(bitstr):
    #bitstr is 8 concatenated bits
    for i in range(0, 8):
        GPIO.output(i, int(bitstr[i]))

#Input a list of lists in format (xlayer1, y1),(xlayer2, y2),...., (xlayern,yn)
def coordToBitString(*argv):
  cordlist = { }
  for arg in argv:
    cordlist.append(str('0.05b'.format(arg[0]))+""+str('0.03b'.format(arg[1])))
  return cordlist
<<<<<<< HEAD
=======

>>>>>>> 8563d578b5b6fba2891116634b781a5ff18880dc
