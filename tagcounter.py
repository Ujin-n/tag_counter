import argparse
from datetime import datetime

import TagGetter as tg
import TagCounterGUI as tcg
from tkinter import *
import DbLoader as dbl


def db_load(tag_dic, url_address, curr_date):
    """ Method load data into sqlite db. """
    db = dbl.DbLoader(tag_dic, url_address, curr_date)
    db.run()


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

    # Load data into sqlite db
    db_load(tag_counter.tag_dict, tag_counter.url_address, current_date)

elif args.get:
    # Console mode
    tag_getter = tg.TagGetter(args.get, current_date, current_time)
    tag_dict = tag_getter.run()

    # Load data into sqlite db
    db_load(tag_dict, args.get, current_date)

elif args.view:
    # Reading saved data from database
    ...
