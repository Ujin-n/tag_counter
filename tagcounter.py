import argparse
from datetime import datetime
from urllib.error import URLError

import TagGetter as tg
import TagCounterGUI as tcg
from tkinter import *
import yaml
import DbLoader as dbl
import ast

# Parsing arguments
parser = argparse.ArgumentParser()
parser.add_argument("--get", help="Get the list of tags.")
parser.add_argument("--view", help="Read saved data from database.")
args = parser.parse_args()

# getting date/time
now = datetime.now()
current_time = now.time().strftime("%H:%M:%S")
current_date = now.date()


def synonym_check(url):
    with open("synonyms.yaml") as f:
        synonym_list = yaml.load(f, Loader=yaml.FullLoader)

    synonym_url = synonym_list.get(url)

    if synonym_url:
        return synonym_url
    else:
        return url


if not args.get and not args.view:
    # GUI mode

    # Start tkinter GUI
    root = Tk()
    root.title("Tag Counter")
    tag_counter = tcg.TagCounterGUI(root, current_date, current_time)
    root.mainloop()

elif args.get:
    # CONSOLE DOWNLOAD MODE

    # Get input url
    input_url = args.get

    # Synonym check
    full_url = synonym_check(input_url)

    # Run tag download
    tag_getter = tg.TagGetter(full_url, current_date, current_time)

    try:
        tag_dict = tag_getter.run()
    except URLError:
        print("Incorrect URL.")
        exit()

    for tag, count in tag_dict.items():
        print(tag + ": " + str(count))

    # Load data into sqlite db
    db = dbl.DbLoader(tag_dict, full_url, current_date, 'W')
    db.run()

elif args.view:
    # CONSOLE READ MODE

    # Get input url
    input_url = args.view

    # Synonym check
    full_url = synonym_check(input_url)

    # Read data from sqlite db
    db = dbl.DbLoader(None, full_url, None, 'R')
    tag_dict = db.run()

    if tag_dict:
        tag_dict = ast.literal_eval(tag_dict[0][0])
        for tag, count in tag_dict.items():
            print(tag + ": " + str(count))
    else:
        print("No data found.")
