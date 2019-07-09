from asciimatics.screen import Screen
from time import sleep
from terminalfingers import TerminalFingers


def parse_words(file):
    words = []
    with open(file) as f:
        for line in f.readlines():
            words.append(line.strip('\n'))
    return words


def main(screen):
    screen.set_title("terminalfingers")
    tf = TerminalFingers(screen, parse_words("../data/words.txt"))
    tf.new_game()
    tf.play()


if __name__ == "__main__":
    Screen.wrapper(main)
