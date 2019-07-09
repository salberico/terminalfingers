from asciimatics.screen import Screen

def clamp(x, a, b):
    return max(a, min(x, b))

def draw_box(screen, x, y, width, height, colour=7, bg=0):
    if width <= 0 or height <= 0:
        return

    screen.print_at('+', x, y, colour, 0, bg)
    screen.print_at('+', x+width-1, y, colour, 0, bg)
    screen.print_at('+', x, y+height-1, colour, 0, bg)
    screen.print_at('+', x+width-1, y+height-1, colour, 0, bg)

    if width > 2:
        screen.print_at('-'*(width-2), x+1, y, colour, 0, bg)
        screen.print_at('-'*(width-2), x+1, y+height-1, colour, 0, bg)

    if height > 2:
        for i in range(1, height-1):
            screen.print_at('|', x, y+i, colour, 0, bg)
            screen.print_at('|', x+width-1, y+i, colour, 0, bg)

