#!/usr/bin/env python3
import math
import argparse
from PIL import Image

import colors as colorschemes


class EmojiImage:
    def __init__(self, colors=None, invert=False, scale=(1, 1)):
        self.invert = invert
        self.scale = scale
        if colors is not None:
            self.colors = colors
        else:
            self.colors = colorschemes.default_colors

    # We provide this method as we may want to use this class with in memory
    # objects instead of files.
    def open(self, filename):
        self.img = Image.open(filename)
        self.img = self.img.convert('RGBA')

    def fromarray(self, array):
        self.img = Image.fromarray(array)
        self.img = self.img.convert('RGBA')

    def make(self, resize=64):
        img = self.img.copy()
        # check if we need to make it a thumbnail
        width, height = img.size
        if width > resize and height > resize:
            img.thumbnail((resize, resize))
            width, height = img.size
        # Go through and build our output string up pixel by pixel
        output = ""
        for y in range(height):
            line = ""
            for x in range(width):
                r, g, b, a = img.getpixel((x, y))

                selection = self._distcolor(r, g, b, a)
                line += selection*self.scale[0]
            output += (line + '\n')*self.scale[1]
        return (output, height)

    def _distcolor(self, r1, g1, b1, a1):
        best = {'value': None, 'symbol': ' '}

        for color, symbol in self.colors:
            r2, g2, b2, a2 = color.to_bytes(4, byteorder='big')

            dist = math.sqrt(
                (r1-r2)**2+(g1-g2)**2+(b1-b2)**2+(a1-a2)**2
            )
            if self.invert:
                if best['value'] is None or dist > best['value']:
                    best = {'value': dist, 'symbol': symbol}
            else:
                if best['value'] is None or dist < best['value']:
                    best = {'value': dist, 'symbol': symbol}

        return best['symbol']
