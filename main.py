from PIL import Image

img = Image.open('imgs/ponies.jpg')

reduced_img = img.convert('P', palette = Image.ADAPTIVE, colors = 64)

colors = reduced_img.convert('RGB').getcolors()

print colors
