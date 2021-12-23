"""
This module represents the apple that appears at random places on the screen.
"""
import random
from typing import List
from gui import Gui
from position import Position



def collides(p, positions):
    """Return true if p is any of the positions in the list."""
    for position in positions:
        if p.get_x() == position.get_x() and p.get_y() == position.get_y():
            return True
    return False


class Apple:
    """The apple's location is randomly generated."""

    def __init__(self,gui):
        self.position = Position(randnumx(gui), randnumy(gui))

    def draw(self, gui):
        gui.draw_text("*", self.position.get_x(), self.position.get_y(), "GREEN", "RED")

    def get_position(self):
        return self.position


def randnumx(gui):
    x = random.randint(2, gui.get_width() -2)
    return x

def randnumy(gui):
    y = random.randint(2, gui.get_height() -2)
    return y