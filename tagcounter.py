import argparse
import TagGetter as tg
import TagCounterGUI as tcg
from tkinter import *

# Parsing arguments
parser = argparse.ArgumentParser()
parser.add_argument("--get", help="Get the list of tags.")
parser.add_argument("--view", help="Read saved data from database.")
args = parser.parse_args()

if not args.get and not args.view:
    # GUI mode
    root = Tk()
    root.title("Tag Counter")
    tag_counter = tcg.TagCounterGUI(root)
    root.mainloop()

elif args.get:
    # Console mode
    tag_getter = tg.TagGetter(args.get)
    tag_dict = tag_getter.run()

    for tag, count in tag_dict.items():
        print(tag + ':', count)

elif args.view:
    # Reading saved data from database
    ...
