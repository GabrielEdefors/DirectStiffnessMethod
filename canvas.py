import tkinter as tk

class Canvas(tk.Canvas):

    def __init__(self, parent):
        tk.Canvas.__init__(self, parent)
        self.bind("<Configure>", self.configure)


    def configure(self, event):
        w, h = event.width, event.height
        xy = 0, 0, w - 1, h - 1
        self.create_rectangle(xy)
        self.create_line(xy)
        xy = w - 1, 0, 0, h - 1
        self.create_line(xy)