# EmojiPic

This is program that converts videos and images into emojis and outputs them to
your terminal.

Requires Python 3.

## Usage

```
emojipic [-h] [--webcam] [--resize RESIZE]
    [--colors {blackwhite,blocks,default,ansi}] [--invert]
    [--xscale XSCALE] [--yscale YSCALE]
    filename

```

Use the `--webcam` option if you intend to use the webcam. Make the filename
the device number (usually zero).

User the `--resize` option to scale the images down to a certain number of
pixels. Works by generating a thumbnail. 

The `--colors` options supports different palettes. These include emoji, ansi
characters, blocks, etc.

The `--invert` option reverses the color scheme.

`--xscale` and `--yscale` allow you to specify how many characters a pixel on
the x and y axis are. Useful if your monospaced font is longer vertically than
horizontally.

## License

MIT
