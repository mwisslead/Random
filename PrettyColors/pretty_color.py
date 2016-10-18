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

def hsv_stretch(angle):
    '''modify the hsv angle so that each "color" inhabits an equal amount of space'''
    angles = np.arange(0, 360, 30)
    mapped = [0, 8, 27, 51, 74, 109, 136, 226, 250, 270, 300, 336]
    angle = np.interp(angle, angles, mapped)
    return angle

def pretty_color(integer):
    '''create a nice looking color'''
    angle = (integer * GOLDEN_ANGLE) % 360
    angle = hsv_stretch(angle)
    hsv = np.float32([[[angle, 0.95, 0.95]]])
    return lrgb2srgb(cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB))

def main(args=None):
    '''main function to run if ran as main'''
    if args is None:
        args = parse_args()

    img = np.zeros((4, 6, 3))

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i, j, :] = pretty_color(img.shape[1]*i + j)

    img = cv2.resize(img, None, fx=200., fy=200., interpolation=cv2.INTER_NEAREST)
    plt.imshow(img)
    plt.show()

if __name__ == '__main__':
    main()
