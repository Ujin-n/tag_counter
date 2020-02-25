import argparse
from datetime import datetime

import TagGetter as tg
import TagCounterGUI as tcg
from tkinter import *
import DbLoader as dbl

# Parsing arguments
parser = argparse.ArgumentParser()
parser.add_argument("--get", help="Get the list of tags.")
parser.add_argument("--view", help="Read saved data from database.")
args = parser.parse_args()

# getting date/time
now = datetime.now()
current_time = now.time().strftime("%H:%M:%S")
current_date = now.date()

if not args.get and not args.view:
    # GUI mode
    root = Tk()
    root.title("Tag Counter")
    tag_counter = tcg.TagCounterGUI(root, current_date, current_time)
    root.mainloop()

    # saving tag dictionary into database
    db = dbl.DbLoader(tag_counter.tag_dict, tag_counter.url_address, current_date)
    db.run()

elif args.get:
    # Console mode
    tag_getter = tg.TagGetter(args.get)
    tag_dict = tag_getter.run()

    # print tag dictionary
    for tag, count in tag_dict.items():
        print(tag + ':', count)

elif args.view:
    # Reading saved data from database
    ...
