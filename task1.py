from PIL import Image
import pytesseract
from gtts import gTTS
import pygame
import gtts.tts

gtts.tts.LOGGING = True


pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

image_path = r'D:\\task\\Task1\\image2.png'


img = Image.open(image_path)


text = pytesseract.image_to_string(img)
print(text)


if text:

    tts = gTTS(text)

    tts.save("output.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
else:
    print("No text was extracted from the image.")
