import argparse
from datetime import datetime
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
    with open("synonyms.yaml") as f:
        synonym_list = yaml.load(f, Loader=yaml.FullLoader)
    synonym_url = synonym_list.get(args.get)
    if synonym_url:
        input_url = synonym_url

    # Run tag download
    tag_getter = tg.TagGetter(input_url, current_date, current_time)
    tag_dict = tag_getter.run()

    for tag, count in tag_dict.items():
        print(tag + ": " + str(count))

    # Load data into sqlite db
    db = dbl.DbLoader(tag_dict, input_url, current_date, 'W')
    db.run()

elif args.view:
    # CONSOLE READ MODE

    # Get input url
    input_url = args.view

    # Read data from sqlite db
    db = dbl.DbLoader(None, input_url, None, 'R')
    tag_dict = db.run()

    print(tag_dict)
    tag_dict = ast.literal_eval(tag_dict[0][0])
    for tag, count in tag_dict.items():
        print(tag + ": " + str(count))
