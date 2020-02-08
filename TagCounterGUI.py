from tkinter import *
from tkinter import messagebox
from urllib.error import URLError
import tkinter.scrolledtext as scrolledtext

import TagGetter as tg


class TagCounterGUI(Frame):
    """ GUI for tag counter application. """

    def __init__(self, master):
        """ Initialize GUI class and set some settings. """
        super().__init__(master)
        self.grid()

        self.url_entry_label = None
        self.output = None
        self.url_address = None
        self.tag_dict = {}

        self.create_widgets()

    def create_widgets(self):
        """ Create all widgets on a window. """
        # create Label for url entry
        url_entry_label = Label(self, text="Enter URL:", pady=5, font=("Arial Bold", 10))
        url_entry_label.grid(column=0, row=0, sticky=W)

        # create url Entry
        self.url_entry_label = Entry(self, width=50)
        self.url_entry_label.grid(column=0, row=1, padx=5)

        # create "Download" Button
        btn_download = Button(self, text="Download", command=self.download_tags, width=10, height=1)
        btn_download.grid(column=0, row=2, pady=5, padx=5)

        # create "Read" Button
        btn_read = Button(self, text="Read", command=self.read_tags, width=10, height=1)
        btn_read.grid(column=0, row=3, pady=5, padx=5)

        # create output Scrolled Text field
        self.output = scrolledtext.ScrolledText(self, width=30, height=10)
        self.output.grid(row=4, column=0, pady=5)

    def download_tags(self):
        """ Run downloading and parsing html. """
        # Getting the list of tags
        self.url_address = self.url_entry_label.get()
        tag_getter = tg.TagGetter(self.url_address)

        # catch url request exception
        try:
            self.tag_dict = tag_getter.run()
        except URLError:
            self.url_error_message()

        # print tags counts
        self.tag_show()

    def read_tags(self):
        """ Run reading from database. """
        ...

    def tag_show(self):
        """ Print tag:count dictionary in output area. """
        for tag, count in self.tag_dict.items():
            self.output.insert(0.0, tag + ': ' + str(count) + '\n')

    def url_error_message(self):
        """ Throw URL error Message Box"""
        messagebox.showinfo("Error", "Incorrect URL: " + self.url_address)
