from buttons import Buttons
from tkinter import Tk
class Window:
    def __init__(self):
        self.window = Tk()
        self.window.title("Typing speed test")
        self.window.geometry("700x500")
        self.window.config(bg="white")

        #buttons
        buttons = Buttons()

        self.window.mainloop()