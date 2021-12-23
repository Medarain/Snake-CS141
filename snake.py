"""
This module implements the snake class.
"""

from apple import Apple, collides
from gui import Gui
from position import Position
from typing import List

class Snake:
    """This is the Snake.

    It has a list of positions. The head is at index 0.
    The tail occupies the rest of the list.
    """


    def __init__(self, gui):
        self.snake = [Position(gui.get_width()//2, gui.get_height()//2)]
        self.snake.append(Position(gui.get_width()//2 - 1, gui.get_height()//2))
        self.snake.append(Position(gui.get_width()//2 - 2, gui.get_height()//2))
        self.direction = "RIGHT"
        self.snakehead = ">"


    def grow(self,gui):
        self.snake.append(Position(self.snake[1:], self.snake[1:]))

    

    def draw(self, gui):
        gui.draw_text(self.snakehead,int(self.snake[0].get_x()),int(self.snake[0].get_y()), "RED", "BLACK")
        for i in self.snake[1:]:
            gui.draw_text("+",i.get_x() ,i.get_y(), "RED", "BLACK")

    def move(self):
        slithermove = []
        if self.direction == "RIGHT":
            slithermove.append(Position(self.snake[0].get_x() +1, self.snake[0].get_y()))
        
        if self.direction == "UP":
            slithermove.append(Position(self.snake[0].get_x(), self.snake[0].get_y() - 1))

        if self.direction == "LEFT":
            slithermove.append(Position(self.snake[0].get_x() - 1, self.snake[0].get_y()))

        if self.direction == "DOWN":
            slithermove.append(Position(self.snake[0].get_x(), self.snake[0].get_y() + 1))

        for i in self.snake[:-1]:
            slithermove.append(i)
        self.snake = slithermove
        
        

    def change_direction(self, direction):
        if direction == "UP":
            if self.direction == "DOWN":
                pass
            else:
                self.direction = direction
                self.snakehead = "^"

        if direction == "DOWN":      
            if self.direction == "UP":
                pass
            else:
                self.direction = direction
                self.snakehead = "v"

        if direction == "LEFT":
            if self.direction == "RIGHT":
                pass
            else:
                self.direction = direction
                self.snakehead = "<"

        if direction == "RIGHT":
            if self.direction == "LEFT":
                pass
            else:
                self.direction = direction
                self.snakehead = ">"


