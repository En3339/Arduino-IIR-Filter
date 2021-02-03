#author: Zhengyang Li & En Lu
# Realtime oscilloscope at a sampling rate of 100Hz


import scipy.signal as signal
from pyfirmata2 import Arduino
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IIR2Filter import IIR2Filter

PORT = Arduino.AUTODETECT

samplingRate = 100
Fc=1

class IIRFilter:
    def __init__(self, sos=signal.butter(2,Fc*2/samplingRate,output='sos')):
        sos=sos.T
        self.b=sos[:3]
        self.a=sos[-3:]
        self.IIR2=IIR2Filter(self.b[0],self.b[1],self.b[2],self.a[0],self.a[1],self.a[2])
    def dofilter(self,x):
        self.output=self.IIR2.filter(x)
        return self.output
# Creates a scrolling data display
class RealtimePlotWindow:

    def __init__(self):
        # create a plot window
        self.fig, self.ax = plt.subplots()
        # that's our plotbuffer
        self.plotbuffer = np.zeros(500)
        # create an empty line
        self.line, = self.ax.plot(self.plotbuffer)
        #For a temperature sensor
        #self.ax.set_ylim(0, 30)
        self.ax.set_ylim(0, 1.5)
        # That's our ringbuffer which accumluates the samples
        # It's emptied every time when the plot window below
        # does a repaint
        self.ringbuffer = []
        # add any initialisation code here (filters etc)
        self.myfilter=IIRFilter()
        #self.ax.set_ylabel('Temperature/℃')
        #self.ax.set_xlabel('Time/ms')
        # start the animation
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=100)

    # updates the plot
    def update(self, data):
        # add new data to the buffer
        self.plotbuffer = np.append(self.plotbuffer, self.ringbuffer)
        # only keep the 500 newest ones and discard the old ones
        self.plotbuffer = self.plotbuffer[-500:]
        self.ringbuffer = []
        # set the new 500 points of channel 9
        self.line.set_ydata(self.plotbuffer)
        return self.line,

    # appends data to the ringbuffer
    def addData(self, v):
        self.ringbuffer.append(v)


# Create 2 instance of an animated scrolling window

realtimePlotWindow1 = RealtimePlotWindow()
realtimePlotWindow2 = RealtimePlotWindow()
# sampling rate: 100Hz
samplingRate = 100

# called for every new sample which has arrived from the Arduino
def callBack(data):
    # send the sample to the plotwindow
    # add any filtering here:
    #Normalise into ℃,optional, only useful in our project
    #data=data*5/0.01-2
    realtimePlotWindow1.addData(data)
    data = realtimePlotWindow1.myfilter.dofilter(data)    
    realtimePlotWindow2.addData(data)
# Get the Ardunio board.
board = Arduino(PORT)

# Set the sampling rate in the Arduino
board.samplingOn(1000 / samplingRate)

# Register the callback which adds the data to the animated plot
board.analog[0].register_callback(callBack)

# Enable the callback
board.analog[0].enable_reporting()

# show the plot and start the animation
plt.show()

# needs to be called to close the serial port
board.exit()

print("finished")