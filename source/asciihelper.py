from asciimatics.screen import Screen
from box import Box

def clamp(x, a, b):
    return max(a, min(x, b))


def draw_box(screen, box, colour=7, bg=0):
    if box.width <= 0 or box.height <= 0:
        return

    screen.print_at('+', box.x, box.y, colour, 0, bg)
    screen.print_at('+', box.x+box.width-1, box.y, colour, 0, bg)
    screen.print_at('+', box.x, box.y+box.height-1, colour, 0, bg)
    screen.print_at('+', box.x+box.width-1, box.y+box.height-1, colour, 0, bg)

    if box.width > 2:
        screen.print_at('-'*(box.width-2), box.x+1, box.y, colour, 0, bg)
        screen.print_at('-'*(box.width-2), box.x+1, box.y+box.height-1, colour, 0, bg)

    if box.height > 2:
        for i in range(1, box.height-1):
            screen.print_at('|', box.x, box.y+i, colour, 0, bg)
            screen.print_at('|', box.x+box.width-1, box.y+i, colour, 0, bg)


def clear_at_box(screen, box):
    for i in range(box.height):
        screen.print_at(' '*box.width, box.x, box.y + i)