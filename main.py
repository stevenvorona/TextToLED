import io
import pygame
from pygame.locals import *
from google.cloud import vision

def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()
    # [START migration_text_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    descriptions = []
    for text in texts:
        descriptions.append(text.description)
    return descriptions

def getCharBin(ch):
    chars = {
    'A':['01110', '01010', '01110', '01010', '01010'],
    'B':['11100', '10100', '11100', '10100', '11100'],
    'C':['11111', '10000', '10000', '10000', '11111'],
    'D':['11110', '10001', '10001', '10001', '11110'],
    'E':['11110', '10000', '11110', '10000', '11110'],
    'F':['11110', '10000', '11110', '10000', '10000'],
    'G':['00000', '00000', '00000', '00000', '00000'],
    'H':['00000', '00000', '00000', '00000', '00000'],
    'I':['00000', '00000', '00000', '00000', '00000'],
    'J':['00000', '00000', '00000', '00000', '00000'],
    'K':['00000', '00000', '00000', '00000', '00000'],
    'L':['00000', '00000', '00000', '00000', '00000'],
    'M':['00000', '00000', '00000', '00000', '00000'],
    'N':['00000', '00000', '00000', '00000', '00000'],
    'O':['00000', '00000', '00000', '00000', '00000'],
    'P':['00000', '00000', '00000', '00000', '00000'],
    'Q':['00000', '00000', '00000', '00000', '00000'],
    'R':['00000', '00000', '00000', '00000', '00000'],
    'S':['00000', '00000', '00000', '00000', '00000'],
    'T':['00000', '00000', '00000', '00000', '00000'],
    'U':['00000', '00000', '00000', '00000', '00000'],
    'V':['00000', '00000', '00000', '00000', '00000'],
    'W':['00000', '00000', '00000', '00000', '00000'],
    'X':['00000', '00000', '00000', '00000', '00000'],
    'Y':['00000', '00000', '00000', '00000', '00000'],
    'Z':['00000', '00000', '00000', '00000', '00000']
    }
    if(ch in chars.keys()):
        return chars[ch]
    else:
        return ['00000', '00000', '00000', '00000', '00000']

pygame.init()
cameras = list_cameras()
if(cameras):
  cam = Camera(cameras[0], cameras[0].get_size())
cam.start()

while(True):
    img = cam.get_image()
    pygame.image.save(img, 'image.jpg')
    detected = detect_text('image.jpg')
    print detected
