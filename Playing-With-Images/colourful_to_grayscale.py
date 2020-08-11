from PIL import Image

img = Image.open("min2.jpeg")
grayscale = img.convert('L')
grayscale.save('graysacle.jpeg')


