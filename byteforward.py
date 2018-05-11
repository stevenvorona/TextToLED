#Config
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
for i in range(0, 8):
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)

dispalyit = (raw_input("Hey there, what word you wanna print?")).upper()

#turns each letter into a list of bit strings, then cycles through that list for each letter w/ cycleletter()
for c in dispalyit:
    coords = {}
    coords = getCharBytes(c)
    coordbits = coords
    for i in range (0,len(coords)):
        coordbits[i] = "{0:08b}".format(coords[i])
    cycleletter(coordbits)

#illuminates an led once per 0.5 seconds
def cycleletter(coordbits):
    n = 0
    z = 0
    lit = len(coordbits)
    while True:
        try:
            pushOneBitString(coordbits[n])
    	    n=n+1
        except:
            print "Err"
        if n == lit:
            n = 0
            z = z + 1
        if z == 2:
            z = 0
            break
    #waits another second before ouputting another letter
    time.sleep(1)


#Takes a 8-bit string and outputs to the RPI
def pushOneBitString(bitstr):
    #bitstr is 8 concatenated bits
    for i in range(0, 8):
        GPIO.output(i+18, int(bitstr[i]))
    #waits 1 second before moving to the next LED
    time.sleep(1)

#Input a list of lists in format (xlayer1, y1),(xlayer2, y2),...., (xlayern,yn)
'''
def coordToBitString(*argv):
  cordlist = { }
  for arg in argv:
    cordlist.append(str("{0:05b}".format(arg[0]))+str("{0:03b}".format(arg[1])))
  return cordlist
'''

def getCharBytes(ch):
    #dict of hex strings of coords of 0th layer
    #2-dig coords
    coords = []
	dict={
	'A': [8, 16, 24, 48, 64, 88, 96, 104, 128, 144, 168, 184],
	'B': [0, 8, 16, 40, 56, 80, 88, 96, 120, 136, 160, 168, 176],
	'C': [0, 8, 16, 24, 32, 40, 80, 120, 160, 168, 176, 184, 192],
	'D': [0, 8, 16, 24, 40, 72, 80, 112, 120, 152, 160, 168, 176, 184],
	'E': [0, 8, 16, 24, 40, 80, 88, 96, 104, 120, 160, 168, 176, 184],
	'F': [0, 8, 16, 24, 40, 80, 88, 96, 104, 120, 160],
	'G': [0, 8, 16, 24, 32, 40, 80, 104, 112, 120, 152, 160, 168, 176, 184, 192],
	'H': [0, 32, 40, 72, 80, 88, 96, 104, 112, 120, 152, 160, 192],
	'I': [0, 8, 16, 24, 32, 56, 96, 136, 160, 168, 176, 184, 192],
	'J': [0, 8, 16, 24, 32, 56, 96, 136, 160, 168, 176],
	'K': [0, 24, 40, 56, 80, 88, 120, 136, 160, 184],
	'L': [0, 40, 80, 120, 160, 168, 176, 184, 192],
	'M': [0, 8, 16, 24, 32, 40, 56, 72, 80, 96, 112, 120, 136, 152, 160, 192],
	'N': [0, 8, 16, 24, 32, 40, 72, 80, 112, 120, 152, 160, 192],
	'O': [0, 8, 16, 24, 32, 40, 72, 80, 112, 120, 152, 160, 168, 176, 184, 192],
	'P': [0, 8, 16, 24, 32, 40, 72, 80, 88, 96, 104, 112, 120, 160],
	'Q': [0, 8, 16, 24, 32, 40, 72, 80, 112, 120, 128, 136, 144, 152, 176],
	'R': [0, 8, 16, 24, 32, 40, 72, 80, 88, 96, 104, 112, 120, 128, 160, 176],
	'S': [0, 8, 16, 24, 32, 40, 80, 88, 96, 104, 112, 152, 160, 168, 176, 184, 192],
	'T': [0, 8, 16, 24, 32, 56, 96, 136, 176],
	'U': [0, 32, 40, 72, 80, 112, 120, 152, 160, 168, 176, 184, 192],
	'V': [0, 32, 40, 72, 88, 104, 128, 144, 176],
	'W': [0, 32, 40, 72, 80, 96, 112, 128, 144, 168, 184],
	'X': [0, 32, 48, 64, 96, 128, 144, 160, 192],
	'Y': [0, 32, 48, 64, 96, 136, 176],
	'Z': [0, 8, 16, 24, 32, 64, 96, 128, 160, 168, 176, 184, 192]
    }
    if(ch in dict.keys()):
        coord = dict[ch]
        for i in range(5):
            for j in coord:
                coords.append(j+i)
        return coords
    else:
        return []
