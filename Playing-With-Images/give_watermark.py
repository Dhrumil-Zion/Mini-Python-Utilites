from PIL import Image, ImageDraw, ImageFont

img = Image.open("min2.jpeg")  # image name with relative path(in there is)

idraw = ImageDraw.Draw(img)
text = "ZION"  # WATERMARK NAME GOES HERE
font = ImageFont.truetype("arial.ttf", size=300)  # FONT-STYLE AND SIZE GOES HERE
idraw.text((100, 100), text, font=font)  # HERE BOTH 100 ARE PADDING-LEFT AND PADDING-TOP
img.save('watermarked.jpeg')
