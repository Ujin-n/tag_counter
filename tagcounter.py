import argparse
import tagcounter_get as tg

# Parsing arguments
parser = argparse.ArgumentParser()
parser.add_argument("--get", help="Get the list of tags.")
parser.add_argument("--view", help="Read saved data from database.")
args = parser.parse_args()

if not args.get and not args.view:
    # Calling GUI
    ...

elif args.get:
    # Getting the list of tags
    tag_counter = tg.TagCounter(args.get)
    tag_counter.run()

elif args.view:
    # Reading saved data from database
    ...
