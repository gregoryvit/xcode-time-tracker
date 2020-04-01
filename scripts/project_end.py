#!/usr/bin/python
# Simly calling pyton to finish the task
import sys,time,os
from os.path import expanduser
import subprocess
import re
from sender import send_results


def get_device_info():
    try:
        items = subprocess.check_output(['sysctl', '-n', 'machdep.cpu.brand_string', 'hw.model', 'hw.memsize', '']).decode('utf-8').split('\n')
        info = "| ".join([i for i in items if i])
    except:
        info = "No model, CPU or RAM info"
    return info

def get_git_user():
	try:
		git_user = subprocess.check_output(['git', 'config', 'user.email'])[:-1]
	except:
		git_user = "No git user"
	return git_user

def is_allowed_to_save(res):
	project_name = res["project"]
	with open(expanduser("~/.timecheck/white_list"), 'r') as f: 
		for line in f.readlines():
			if re.match(line.strip(), project_name.strip()):
				return True
	return False

milliseconds = int(round(time.time() * 1000))
line = ""
with open(expanduser("~/.timecheck/end_time"), 'w') as f: 
	f.write(str(milliseconds))
with open(expanduser("~/.timecheck/start_time"), 'r') as f: 
	line = f.readline()

start_time = int(line)
duration = milliseconds - start_time

activity = os.environ.get("IDEAlertMessage", "No message")
project_name = os.environ.get("XcodeProject", "No project")
workspace_name = os.environ.get("XcodeWorkspace", "No workspace")

build_entity_name = workspace_name if workspace_name != "No workspace" else project_name

device_info = get_device_info()
git_user = get_git_user()

print "It took " + str(duration) + " seconds to [" + activity + "] for " + build_entity_name

device_info = get_device_info()

results = {
	"user": git_user,
	"event": activity,
	"device": device_info,
	"project": build_entity_name,
	"duration": duration,
	"started": start_time
}

def save_results_to_file(res):
	with open(expanduser("~/.timecheck/results"), 'a') as f: 
		result_string = ",".join([
			res["user"],
			res["device"],
			res["project"], 
			str(res["started"]), 
			res["event"], 
			str(res["duration"])
		])
		f.write(result_string + "\n")


if is_allowed_to_save(results):
	save_results_to_file(results)
	send_results(results)