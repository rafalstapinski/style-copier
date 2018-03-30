from PIL import Image
import math

def distance_3d(a, b):

    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 + (b[2] - a[2]) ** 2)

def distance_2d(a, b):

    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


def get_preferences(set_a, set_b):

    preferences

    for point_a in set_a:

        for point_b in set_b:

            pass

def get_colors(img, palette_size):

    colors_data = img.convert('P',
        palette = Image.ADAPTIVE,
        colors = palette_size
    ).convert('RGB').getcolors()

    colors = {}

    for d in colors_data:

        hex = '#%02x%02x%02x' % d[1]

        colors[hex] = {
            'location': d[1],
            'frequency': d[0]
        }

    return colors

img = Image.open('imgs/vik.jpg')
print get_colors(img, 4)
