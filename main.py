from PIL import Image
import math

def distance_3d(a, b):

    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 + (b[2] - a[2]) ** 2)

def distance_2d(a, b):

    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


def get_point_preferences(point_a, set_b):

    preferences = []

    for point in set_b:
        preferences.append((point, distance_3d(point_a['location'], set_b[point]['location'])))

    preferences = sorted(preferences, key = lambda e: e[1])

    return [x[0] for x in preferences]

def get_preferences(set_a, set_b):

    for point in set_a:

        set_a[point]['preferences'] = get_point_preferences(set_a[point], set_b)

    for point in set_b:

        set_b[point]['preferences'] = get_point_preferences(set_b[point], set_a)

    return set_a, set_b

def stable_marriage(set_a, set_b):

    a_prefs = {}
    b_prefs = {}

    for a in set_a:
        a_prefs[a] = set_a[a]['preferences']
    for b in set_b:
        b_prefs[b] = set_b[b]['preferences']

    a_list = sorted(a_prefs.keys())
    b_list = sorted(b_prefs.keys())

    a_free = a_list[:]
    matches  = {}

    a_prefs_2 = a_prefs
    b_prefs_2 = b_prefs

    while a_free:

        a = a_free.pop(0)
        a_list = a_prefs_2[a]

        b = a_list.pop(0)
        match = matches.get(b)

        if not match:
            matches[b] = a

        else:

            b_list = b_prefs_2[b]

            if b_list.index(match) > b_list.index(a):

                matches[b] = a

                if a_prefs_2[match]:
                    a_free.append(match)

            else:

                if a_list:
                    a_free.append(a)

    return matches

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

if __name__ == '__main__':

    input_colors = get_colors(Image.open('imgs/vik.jpg'), 4)
    output_colors = get_colors(Image.open('imgs/ponies.jpg'), 4)

    input_colors, output_colors = get_preferences(input_colors, output_colors)

    # print input_colors, output_colors

    print stable_marriage(input_colors, output_colors)
