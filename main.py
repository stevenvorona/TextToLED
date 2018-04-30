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

pygame.init()
cameras = list_cameras()
if(cameras):
  cam = Camera(cameras[0], cameras[0].get_size())
cam.start()

while(True):
    img = cam.get_image()
    pygame.image.save(img, 'image.jpg')
    print detect_text('image.jpg')
