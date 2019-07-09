from asciimatics.screen import Screen
from time import sleep
from terminalfingers import TerminalFingers


def main(screen):
    screen.set_title("terminalfingers")
    tf = TerminalFingers(screen)
    tf.play()
    sleep(1)


if __name__ == "__main__":
    Screen.wrapper(main)
