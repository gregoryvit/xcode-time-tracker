# Xcode Time Tracker
This is the tool that allows to track events that are happening in Xcode
This tool simply runs tracking scripts based on Xcode behaviors.
It's independent on the Xcode version (as soon as you have Xcode version higher than 4 :)
It will survive Xcode reinstallations, so it works on 'install and forget basis'

# Raw output example
The result of this tool will be one simple csv file looking like this
```
#Email, ProjectName, Workspace, TimeStart, Event, TimeSpent
gregoryvit@gmail.com,No project,Test.xcworkspace,1518017360394,Build Succeeded,145025298
```

# Installation
There'are two installation steps: 
1) Place scripts to `~/.timecheck` directory
2) Setup Xcode behaviours to run those scripts on every run

## Scripts installation
Simply run 
```
install.sh
```

Or use this for install scripts and remove dir with repo:
```
git clone https://github.com/gregoryvit/xcode-time-tracker && ./xcode-time-tracker/install.sh && rm -rf xcode-time-tracker
```

This will copy `project_start.py` and `project_end.py` to the `~/.timecheck` directory

## Xcode Behaviours setup

1) Edit Xcode Behaviors  
![Behaviors](https://github.com/PaulTaykalo/xcode-time-tracker/blob/images/images/behaviours.png?raw=true)
2) Set project_start.py script as custom script for start behaviors  
![Start Behaviors](https://github.com/PaulTaykalo/xcode-time-tracker/blob/images/images/start_script.png?raw=true)
3) Set project_end.py script as custom script for end behaviors  
![End Behaviors](https://github.com/PaulTaykalo/xcode-time-tracker/blob/images/images/end_script.png?raw=true)


## Next step
There are no more steps. Done.

## Check Installation
Build your precious project and see that there's new file appeared in `~/.timecheck` directory
It should contain line that should look like this
```
No project,HeyYouAreAwesome.xcworkspace,1597876725,1597876729,Build Succeeded,4
```

# Visualization
The next step is to visualize this information.
I used [R](https://www.r-project.org/about.html) language for that. But there's more coming
This how it can look like if you'll be able to setup R correcly :)
![Visualization](https://github.com/PaulTaykalo/xcode-time-tracker/blob/images/images/stats_visualized.png?raw=true)

