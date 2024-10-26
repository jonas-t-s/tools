import datetime
import argparse

import pytz

parser = argparse.ArgumentParser()
parser.add_argument("inputfilepath", help="path to the file you want to translate")
args = parser.parse_args()
innerlineseperator = "ubuntu-4gb-hel1-2"
datetimeformat = "%b %d %H:%M:%S"
with open(args.inputfilepath, "r") as file:
    lines = file.readlines()
    for line in lines:
        date, line = line.split(innerlineseperator)
        date_time_obj = datetime.datetime.strptime(date.rstrip(" "), datetimeformat).replace(tzinfo=datetime.timezone.utc).replace(year=datetime.datetime.now().year)


        print(f"{date_time_obj.astimezone(pytz.timezone('Europe/Zurich')).strftime(datetimeformat)} {line}")