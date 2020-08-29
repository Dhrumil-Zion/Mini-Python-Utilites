from PIL import Image

img = Image.open("smit.jpg")  # image name with relative path(in there is)
grayscale = img.convert('L')
grayscale.save('graysacle_smit.jpeg')
