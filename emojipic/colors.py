# These are the default colors that I picked out based on the websafe
# colors list available here:
# https://en.wikipedia.org/wiki/Web_colors#HTML_color_names
# Colors are represented as 32bit values of the form RGBA.
default_colors = [
    (0x00000000, '⬛'),  # Black
    (0xffffff00, '⬜'),  # White
    (0xff000000, '🍎'),  # Red
    (0x80000000, '🌇'),  # Maroon
    (0x00ff0000, '🍀'),  # Lime
    (0x00800000, '🐸'),  # Green
    (0x0000ff00, '🆕'),  # Blue
    (0xff7f0000, '🆚'),  # Orange
    (0xffff0000, '😶'),  # Yellow
    (0x80800000, '🐻'),  # Olive
    (0x80008000, '😈'),  # Purple
    (0x80808000, '🐭'),  # Gray
    (0xc0c0c000, '👽'),  # Silver
    (0x00808000, '🗽'),  # Teal
    (0x00008000, '🌃'),  # Navy
    (0xff00ff00, '🐽'),  # Fuchsia
    (0x00ffff00, '🐳'),  # Aqua
]

blackwhite_colors = [
    (0x00000000, ' '),  # Black
    (0xffffff00, '█'),  # White
]

block_colors = [
    (0x00000000, ' '),  # Black
    (0x3f3f3f00, '░'),  # Light
    (0x7e7e7e00, '▒'),  # Medium
    (0xbdbdbd00, '▓'),  # Dark
    (0xffffff00, '█'),  # White
]

# Generate the colors because we are lazy :)
# We are using the ubuntu color scheme.
ansi_spec = [
    (30, 0x000000),
    (31, 0xde382b),
    (32, 0x39b54a),
    (33, 0xff7706),
    (34, 0x006fb8),
    (35, 0x762671),
    (36, 0x29b571),
    (37, 0xcccccc),
    (90, 0x808080),
    (91, 0xff0000),
    (92, 0x00ff00),
    (93, 0xffff00),
    (94, 0x0000ff),
    (95, 0xff00ff),
    (96, 0x00ffff),
    (97, 0xffffff),
]

ansi_colors = []
for code, value in ansi_spec:
    color = '\033[{}m█\033[0m'.format(code)
    ansi_colors.append((value*0x100, color))

# Object exposed to make it easier for the user to select the scheme
colorschemes = {
    'blackwhite': blackwhite_colors,
    'blocks': block_colors,
    'default': default_colors,
    'ansi': ansi_colors,
}
