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
    # Calling GUI
    root = Tk()
    root.title("Tag Counter")
    tag_counter = tcg.TagCounterGUI(root)
    root.mainloop()

elif args.get:
    # Getting the list of tags
    tag_getter = tg.TagGetter(args.get)
    tag_getter.run()

elif args.view:
    # Reading saved data from database
    ...
