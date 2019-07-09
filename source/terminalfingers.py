from asciimatics.screen import Screen
from asciihelper import *
from box import Box
import random


class TerminalFingers:
    min_dimensions = (10, 40)
    max_dimensions = (20, 80)

    def __init__(self, screen, words):
        self.screen = screen
        self.word_bank = words
        self.words = []
        self.word_index = -1
        self.lines = []

        dim = self.get_dimensions()
        self.word_box = Box(2, 2, dim[1]-4, dim[0]-4)

    def get_dimensions(self):
        cur = self.screen.dimensions
        width = clamp(cur[1], TerminalFingers.min_dimensions[1], TerminalFingers.max_dimensions[1])
        height = clamp(cur[0], TerminalFingers.min_dimensions[0], TerminalFingers.max_dimensions[0])
        return (height, width)

    def recalculate_lines(self):
        self.lines = [[] for _ in range(self.word_box.height)]
        test_index = self.word_index
        for i in range(len(self.lines)):
            line = self.lines[i]
            space_left = self.word_box.width + 1
            while space_left - len(self.words[test_index]) > 0:
                line.append(self.words[test_index])
                space_left -= (len(self.words[test_index]) + 1)
                test_index += 1

    def generate_word_batch(self):
        space_left = TerminalFingers.max_dimensions[0] * TerminalFingers.max_dimensions[1] + 1
        while space_left > 0:
            new_word = random.choice(self.word_bank)
            self.words.append(new_word)
            space_left -= len(new_word) + 1

    def new_game(self):
        self.generate_word_batch()
        self.recalculate_lines()

    def draw_border(self):
        dim = self.get_dimensions()
        draw_box(self.screen, Box(0, 0, dim[1], dim[0]), colour=Screen.COLOUR_CYAN, bg=Screen.COLOUR_BLACK)

    def redraw_all(self):
        self.screen.clear()
        self.draw_border()

        for i in range(len(self.lines)):
            x = self.word_box.x
            for word in self.lines[i]:
                self.screen.print_at(word, x, self.word_box.y + i)
                x += len(word) + 1

        self.screen.refresh()

    def play(self):
        self.redraw_all()
        while 1:
            self.screen.wait_for_input(1.0)
            event = self.screen.get_event()
            if (event != None):
                clear_at_box(self.screen, self.word_box)
                self.screen.refresh()




