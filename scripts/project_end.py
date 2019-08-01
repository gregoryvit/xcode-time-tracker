#!/usr/bin/python
# Simly calling pyton to finish the task
import sys,time,os
from os.path import expanduser
import subprocess


def get_device_info():
    try:
        items = subprocess.check_output(['sysctl', '-n', 'machdep.cpu.brand_string', 'hw.model']).decode('utf-8').split('\n')
        info = "| ".join([i for i in items if i])
    except:
        info = "No model and CPU info"
    return info

milliseconds = int(round(time.time() * 1000))
line = ""
with open(expanduser("~/.timecheck/end_time"), 'w') as f: 
	f.write(str(milliseconds))
with open(expanduser("~/.timecheck/start_time"), 'r') as f: 
	line = f.readline()

start_time = int(line)
diff = milliseconds - start_time

activity = os.environ.get("IDEAlertMessage", "No message")
project_name = os.environ.get("XcodeWorkspace", "No workspace")
workspace_name = os.environ.get("XcodeProject", "No project")

try:
	git_user = subprocess.check_output(['git', 'config', 'user.email'])[:-1]
except:
	git_user = "No git user"

print "It took " + str(diff) + " seconds to [" + activity + "] for " + project_name

device_info = get_device_info()

with open(expanduser("~/.timecheck/results"), 'a') as f: 
	result_string = ",".join([
		git_user,
		device_info,
		workspace_name, 
		project_name, 
		str(start_time), 
		activity, 
		str(diff)
	])
	f.write(result_string + "\n")

# Upload th results somewhere	
