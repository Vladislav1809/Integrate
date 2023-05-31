from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
import draw_function


class Window(Frame):

    def __init__(self, root, radius, h):
        self.radius = radius
        self.h = h
        super().__init__()
        self.root = root
        self.style = Style()
        self.initUI()

    def hide(self):
        pass

    def initUI(self):
        self.master.title("Численное вычистелние интеграла")
        self.style.theme_use("default")

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)
        btn = Button(self, text="Изобразить график",
                     command=lambda: draw(self.root, self.radius.get(), self.h.get()))
        btn.pack(fill=BOTH, side=RIGHT, padx=5, pady=5)


def draw(root: Tk, r: str, h: str):
    root.withdraw()
    draw_function.draw(r, h)
