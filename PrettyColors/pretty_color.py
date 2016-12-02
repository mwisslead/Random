'''generate pretty colors by stretching hsv to have each color inhabit an equal amount of the hsv
   angle and then returning a srgb color with h = n times the golden angle and s and v equal to 0.95
   '''

import math
import argparse

import numpy as np

import matplotlib.pyplot as plt

import cv2

GOLDEN_ANGLE = 720/(3+math.sqrt(5))

def parse_args(argv=None):
    '''parse args in the future'''
    parser = argparse.ArgumentParser(description='Show some pretty colors')
    return parser.parse_args(argv)

def lrgb2srgb(lrgb):
    '''convert linear rgb to srgb'''
    func = lambda lval: (12.92*lval) if lval < 0.0031308 else (1+0.055)*(lval**(1/2.4)) - 0.055
    return np.vectorize(func)(lrgb)

def hue_stretch(hue):
    '''stretch different regions of the hue so that each "color" is equally likely'''
    hues = np.linspace(-22.5, 382.5, 10)
    mapped = np.array([-13, 8, 27, 81, 134, 230, 243, 255, 347, 368])
    return np.interp(hue, hues, mapped)

def pretty_color(integer, saturation=0.9, value=0.9):
    '''create a nice looking color'''
    hue = (integer * GOLDEN_ANGLE) % 360
    hue = hue_stretch(hue)
    hsv = np.float32([[[hue, saturation, value]]])
    return lrgb2srgb(cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB))

def get_hue(rgb_color):
    '''get hsv hue from an srgb color'''
    return cv2.cvtColor(rgb_color.astype('float32'), cv2.COLOR_RGB2HSV)[0][0][0]

def pretty_colors(integer, saturation=0.9, value=0.9):
    '''create a sorted list of colors containing \'integer\' elements'''
    return sorted([pretty_color(i, saturation, value) for i in range(integer)], key=get_hue)

def main(args=None):
    '''main function to run if ran as main'''
    if args is None:
        args = parse_args()

    colors = 24
    factor = next(i for i in range(int(math.sqrt(colors)), 0, -1) if colors % i is 0)
    img = np.reshape(pretty_colors(colors), (factor, colors//factor, 3))

    plt.imshow(img, interpolation='none')
    plt.show()

if __name__ == '__main__':
    main()
