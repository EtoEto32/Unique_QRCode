from PIL import Image

image = Image.open("neko.jpg")

image.convert("1").save("sirokuro.png")
image.convert("L").save("gure.png")
image.convert("P").save("8bit_color.png")
