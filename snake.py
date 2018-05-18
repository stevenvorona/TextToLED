import time
import random
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
for i in range(18, 26):
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
pins = [4,5,6,12,13,17]
for i in pins:
    GPIO.setup(i, GPIO.IN)

directions = [8, -8, 40, -40, 1, -1]
direction = directions[random.randint(0,5)]
snake = [[random.randint(0, 24)*8 + random.randint(0,2), direction]]
food = random.randint(0, 24)*8 + random.randint(0,2)

def display():
    return 0

while(True):
    for i in snake:
        i[0] += i[1]    #snake part moves in it direction
    newdir = 0
    for i in range(1, len(snake)):
        
    for i in range(6):
        if GPIO.input(pins[i]) and not i== directions.index(direction):
            snake[0][1] = directions[i]
