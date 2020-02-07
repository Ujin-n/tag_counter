from tkinter import *


class TagCounterGUI:
    """ GUI for tag counter application. """
    def __init__(self):
        """ Initialize GUI class and set some settings. """
        # main window settings
        self.screen_size = '400x250'
        self.title = "Tag Counter"

        # widget settings
        self.font = 13

    def create_widgets(self, root):
        """ Create widgets. """
        # URL input
        label_1 = Label(root, text="Enter url: ", font=("Arial Bold", self.font))
        label_1.grid(column=0, row=0)

    def run(self):
        """ Start application. """
        root = Tk()
        root.title(self.title)
        root.geometry(self.screen_size)

        # Calling widgets creation
        self.create_widgets(root)

        root.mainloop()

