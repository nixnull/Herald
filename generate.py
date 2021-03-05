from sys import argv
from csv import reader
from datetime import datetime, timezone 

def scroll_center(string):
    #TODO: fix the scroll alignment so I don't have to add an extra 2
    return int((72 / 2) - (len(string) / 2) + 2)

notices_str = "No news since the previous report."
notices = " " * scroll_center(notices_str) + notices_str

# Determine timestamp

now = datetime.now(timezone.utc)

isTest = True

if isTest:
    report_name = "test"
else:
    report_name = str(now.year) + "-" + str(now.month) + "-" + str(now.day)

time_str = now.strftime('%B') + " " + str(now.day).zfill(2) + ", " + str(now.year)

fancy_time = " " * scroll_center(time_str) + time_str

# Apply map and output report

with open('template.txt', 'r') as infile:
    template = infile.read()

mapping = {'notices': notices, 'fancy_time': fancy_time}

with open('Reports/' + report_name + '.txt', 'w') as ofile:
    ofile.write(template.format_map(mapping))

#TODO: implement fresh report
#with open('scroll.txt', 'w') as ofile:
    #ofile.write(template.format_map(mapping))
