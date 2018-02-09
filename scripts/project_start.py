#!/usr/bin/python
# Simple as a hell - writing current seconds to the file
import sys,time,os
from os.path import expanduser

milliseconds = int(round(time.time() * 1000))
with open (expanduser("~/.timecheck/start_time"), 'w') as f: f.write (str(milliseconds))