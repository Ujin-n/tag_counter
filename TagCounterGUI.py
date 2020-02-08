from tkinter import *


class TagCounterGUI(Frame):
    """ GUI for tag counter application. """

    def __init__(self, master):
        """ Initialize GUI class and set some settings. """
        super().__init__(master)
        self.grid()
        self.create_widgets()

        self.url_entry_label = None

    def create_widgets(self):
        """ Create all widgets on a window. """
        # URL input
        url_entry_label = Label(self, text="URL", pady=5, font=("Arial Bold", 13))
        url_entry_label.grid(column=0, row=0)

        self.url_entry_label = Entry(self, width=50)
        self.url_entry_label.grid(column=2, row=0, padx=5)

        btn_download = Button(self, text="Download", command=self.download_tags, width=10, height=1)
        btn_download.grid(column=0, row=1, pady=5, padx=5)

        btn_read = Button(self, text="Read", command=self.read_tags, width=10, height=1)
        btn_read.grid(column=1, row=1, pady=5, padx=5)

    def download_tags(self):
        """ Run downloading and parsing html. """
        pass

    def read_tags(self):
        """ Run reading from database. """
        pass
