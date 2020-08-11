from PIL import Image, ImageFilter

img = Image.open('mine.png')              # image name with relative path(in there is)
blurred = img.filter(ImageFilter.BLUR)
blurred.save("blurred.png")
