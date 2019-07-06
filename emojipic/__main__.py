#!/usr/bin/env python3
import argparse
import magic

# Our libraries
import pic
import ani
import formats
from colors import colorschemes


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Displays Images or Videos as Emojis in the terminal')
    parser.add_argument('filename', type=str, help='Filename')
    parser.add_argument('--webcam', action='store_true',
                        help='Use the webcam specified')
    parser.add_argument('--resize', type=int, default=32,
                        help='How many characters to scale this to')
    parser.add_argument('--colors', type=str, default='default',
                        choices=colorschemes.keys(),
                        help='Color Scheme')
    parser.add_argument('--invert', action='store_true',
                        help='Invert the color scheme')
    parser.add_argument('--xscale', type=int, default=1,
                        help='Repeat the characters on the x axis N times')
    parser.add_argument('--yscale', type=int, default=1,
                        help='Repeat the characters on the Y axis N times')
    args = parser.parse_args()

    colors = colorschemes[args.colors]
    scale = (args.xscale, args.yscale)

    if args.webcam:
        ani.main(int(args.filename), args.resize, colors, webcam=True,
                 invert=args.invert, scale=scale)
    else:
        # determine if we are going to treat it like a video or a image
        filetype = magic.from_file(args.filename, mime=True)
        if filetype in formats.pillow_supported_formats:
            ei = pic.EmojiImage(colors, invert=args.invert, scale=scale)
            ei.open(args.filename)
            print(ei.make(args.resize)[0])
        elif filetype in formats.opencv_supported_formats:
            ani.main(args.filename, args.resize, colors, invert=args.invert,
                     scale=scale)
        else:
            print('Format not supported')
