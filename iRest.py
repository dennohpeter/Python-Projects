# iRest.py - Created by Dema Abu Adas, May 2nd 2017
from appJar import gui

#top slice - Creat the GUI
app = gui()
# add code here #
app.addMeter("progress")
app.setMeterFill("progress", "blue")


# bottom slice - Start the GUI
app.go()
