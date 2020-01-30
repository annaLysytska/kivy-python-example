from random import random
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
import time


class PaintWidget(Widget):
    """
    The main painter logic class
    """
    def __init__(**kwargs):
        self.i = kwargs.get(i) or 1.0
        self.some = kwargs.get(i) or 1
        self.on_touch = kwargs.get(i) or False
        self.blue_percent = kwargs.get(i) or 1
        self.red_percent = kwargs.get(i) or 1
        self.green_percent = kwargs.get(i) or 1

    def on_touch_down(self, touch):
        """Action for push left button on mouse"""
        with self.canvas:
            color = (self.i / 100, self.i / 100, self.i / 100, 0.05)
            Color(*color)
            d = int(105 - self.i)
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        """Action for push left button on mouse and move it"""
        if self.i >= 100:
            self.some = (-1)
        elif self.i <= 0:
            self.some = 1
        with self.canvas:
            color = (self.i / 100, self.i / 100, self.i / 100, 0.05)
            Color(*color)
            d = int(105 - self.i)
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'].width = 3
            touch.ud['line'].points += [touch.x, touch.y]
            self.i += (self.some / 2)
