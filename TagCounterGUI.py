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
        def clicked():
            res = txt.get()

        label_1 = Label(root, text="URL", pady=5, font=("Arial Bold", self.font))
        label_1.grid(column=0, row=0)

        txt = Entry(root, width=50)
        txt.grid(column=2, row=0)

        button_1 = Button(root, text="        OK        ", command=clicked)
        button_1.grid(column=0, row=1, pady=5, padx=5)

    def run(self):
        """ Start application. """
        root = Tk()
        root.title(self.title)
        root.geometry(self.screen_size)

        # Calling widgets creation
        self.create_widgets(root)

        root.mainloop()

