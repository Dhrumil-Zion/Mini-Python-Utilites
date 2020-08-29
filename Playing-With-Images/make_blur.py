from PIL import Image, ImageFilter

img = Image.open('min2.jpeg')              # image name with relative path(in there is)
blurred = img.filter(ImageFilter.BLUR)
blurred.save("blurred_d.png")
