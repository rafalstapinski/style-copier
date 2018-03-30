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

    set_a_prefs = {}
    set_b_prefs = {}

    for a in set_a:
        set_a_prefs[a] = set_a[a]['preferences']
    for b in set_b:
        set_b_prefs[b] = set_b[b]['preferences']

    guys = sorted(set_a_prefs.keys())
    gals = sorted(set_b_prefs.keys())

    guysfree = guys[:]
    engaged  = {}
    guyprefers2 = set_a_prefs
    galprefers2 = set_b_prefs
    while guysfree:
        guy = guysfree.pop(0)
        guyslist = guyprefers2[guy]
        gal = guyslist.pop(0)
        fiance = engaged.get(gal)
        if not fiance:
            # She's free
            engaged[gal] = guy
            # print("  %s and %s" % (guy, gal))
        else:
            # The bounder proposes to an engaged lass!
            galslist = galprefers2[gal]
            if galslist.index(fiance) > galslist.index(guy):
                # She prefers new guy
                engaged[gal] = guy
                # print("  %s dumped %s for %s" % (gal, fiance, guy))
                if guyprefers2[fiance]:
                    # Ex has more girls to try
                    guysfree.append(fiance)
            else:
                # She is faithful to old fiance
                if guyslist:
                    # Look again
                    guysfree.append(guy)
    return engaged


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
