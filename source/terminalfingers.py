from asciimatics.screen import Screen
from asciihelper import *


class TerminalFingers:
    min_dimensions = (10, 40)
    max_dimensions = (20, 80)

    def __init__(self, screen):
        self.screen = screen

    def get_dimensions(self):
        cur = self.screen.dimensions
        width = clamp(cur[1], TerminalFingers.min_dimensions[1], TerminalFingers.max_dimensions[1])
        height = clamp(cur[0], TerminalFingers.min_dimensions[0], TerminalFingers.max_dimensions[0])
        return (height, width)

    def play(self):
        self.screen.clear()

        for i in range(8):
            pass
            #self.screen.print_at('Hello world!', 0, i, colour=i, attr=0, bg=(i - 1) % 7, transparent=False)

        draw_box(self.screen, 0, 0, self.get_dimensions()[1], self.get_dimensions()[0])
        self.screen.refresh()




