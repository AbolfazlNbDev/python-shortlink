from PIL import Image, ImageDraw, ImageFont
import random


lastnumber = []
num = 0

for i in range(8):
    data = random.randint(1,200000)
    num += data

lastnumber.append(num)

width = 800
height = 400


img = Image.new("RGB", (width, height), "white")


draw = ImageDraw.Draw(img)


text = f"{lastnumber[0]}"
new = num
lastnumber.remove(new)


font = ImageFont.load_default(100)

bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]


x = (width - text_width) / 2
y = (height - text_height) / 2


draw.text((x, y), text, fill="red", font=font)


img.save("captcha.png")



print(lastnumber)
