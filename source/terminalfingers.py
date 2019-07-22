from asciimatics.screen import Screen
from asciimatics.event import KeyboardEvent
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
        self.buffer = []
        self.lines = []
        self.first_line_pos = []
        self.needs_refresh = False
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
            if test_index >= len(self.words):
                self.generate_word_batch()
            while space_left - len(self.words[test_index]) > 0:
                line.append(self.words[test_index])
                space_left -= (len(self.words[test_index]) + 1)
                test_index += 1
                if test_index >= len(self.words):
                    self.generate_word_batch()

        self.first_line_pos = [0 for _ in range(len(self.lines[0]))]
        index = 0
        for i, word in enumerate(self.lines[0]):
            self.first_line_pos[i] = index
            index += len(word) + 1

    def generate_word_batch(self):
        space_left = TerminalFingers.max_dimensions[0] * TerminalFingers.max_dimensions[1] + 1
        while space_left > 0:
            new_word = random.choice(self.word_bank)
            self.words.append(new_word)
            space_left -= len(new_word) + 1

    def new_game(self):
        self.generate_word_batch()
        self.recalculate_lines()
        self.word_index = 0

    def draw_border(self):
        dim = self.get_dimensions()
        draw_box(self.screen, Box(0, 0, dim[1], dim[0]), colour=Screen.COLOUR_CYAN, bg=Screen.COLOUR_BLACK)
        self.needs_refresh = True

    def draw_words(self):
        for i in range(len(self.lines)):
            x = self.word_box.x
            for word in self.lines[i]:
                self.screen.print_at(word, x, self.word_box.y + i)
                x += len(word) + 1
        self.needs_refresh = True

    def redraw_all(self):
        self.screen.clear()
        self.draw_border()
        self.draw_words()
        self.needs_refresh = True

    def next_line(self):
        clear_at_box(self.screen, self.word_box)
        self.recalculate_lines()
        self.draw_words()
        self.needs_refresh = True

    def draw_buffer(self):
        self.screen.print_at(''.join(self.buffer), self.first_line_pos[self.word_index] + self.word_box.x, self.word_box.y)
        self.needs_refresh = True

    def output_char(self, c):
        self.buffer.append(chr(c))
        self.draw_buffer()

    def handle_keyboard_event(self, c):
        if c >= 32 and c <= 126:
            self.output_char(c)
        if c in (17, 24):
            exit(0)

    def play(self):
        self.redraw_all()
        while 1:
            self.screen.wait_for_input(1.0)
            event = self.screen.get_event()
            if (event != None):
                if isinstance(event, KeyboardEvent):
                    self.handle_keyboard_event(event.key_code)
                if self.needs_refresh:
                    self.screen.refresh()
                    self.needs_refresh = False




