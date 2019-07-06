#!/usr/bin/env python3
import argparse
import magic

# Our libraries
import pic
import ani

import formats


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Displays Images or Videos as Emojis in the terminal')
    parser.add_argument('filename', type=str, help='Filename')
    parser.add_argument('--resize', type=int, default=32,
                        help='How many characters to scale this to')
    args = parser.parse_args()

    # determine if we are going to treat it like a video or a image
    filetype = magic.from_file(args.filename, mime=True)
    if filetype in formats.pillow_supported_formats:
        ei = pic.EmojiImage()
        ei.open(args.filename)
        print(ei.make(args.resize)[0])
    elif filetype in formats.opencv_supported_formats:
        ani.main(args.filename, args.resize)
    else:
        print('Format not supported')
