import PIL
from PIL import Image

print("enter image name :")
image_name = str(input())  # image name with relative path(in there is)

img = Image.open(image_name)
mywidth = img.size[0]
myheight = img.size[1]
img = img.resize((mywidth, myheight), PIL.Image.ANTIALIAS)
img.save("resized_3.jpeg")
