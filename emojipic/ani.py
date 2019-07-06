#!/usr/bin/env python3
import argparse
import cv2
import pic
import sys
import time
from PIL import *


def clearscreen(n):
    print('\033[1A\033[K'*n, end='')


def main(filename, resize, colors=None, webcam=False, invert=False,
         scale=(1, 1)):
    vc = cv2.VideoCapture(filename)
    tpf = 1.0/vc.get(cv2.CAP_PROP_FPS)

    ei = pic.EmojiImage(colors=colors, invert=invert, scale=scale)

    if vc.isOpened():
        rval = True
        while rval:
            start = time.time()
            rval, frame = vc.read()
            if rval:
                ei.fromarray(frame)
                res, height = ei.make(resize)
                print(res, end='')
                clearscreen(height*scale[1])
            # determine if we need to sleep. Not really that accurate, but i'm
            # lazy and this is good enough.
            diff = time.time()-start
            if  webcam is False and diff < tpf:
                time.sleep(tpf-diff)

    vc.release()
