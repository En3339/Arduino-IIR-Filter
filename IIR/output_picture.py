#author: Zhengyang Li & En Lu


import scipy.signal as signal
import sys
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
from IIR2Filter import IIR2Filter
from pyfirmata2 import Arduino
samplingRate = 100
Fc=1
PORT = Arduino.AUTODETECT

class IIRFilter:
    def __init__(self, sos = signal.butter(2,Fc*2/samplingRate,'lowpass')): 
        self.b=sos[0]
        self.a=sos[1]
        self.IIR2=IIR2Filter(self.b[0],self.b[1],self.b[2],self.a[0],self.a[1],self.a[2])
    def dofilter(self,x):
        self.output=self.IIR2.filter(x)
        return self.output



# create a global QT application object
app = QtGui.QApplication(sys.argv)
# signals to all threads in endless loops that we'd like to run these
running = True

class QtPanningPlot:

    def __init__(self,title):
        self.win = pg.GraphicsLayoutWidget()
        self.win.setWindowTitle(title)
        self.plt = self.win.addPlot()
        #for a Temperature sensor
        #self.plt.setYRange(0,30)   
        self.plt.setYRange(-1.5,1.5)      
        self.plt.setXRange(0,500)
        self.curve = self.plt.plot()
        self.data = []
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(100)
        self.layout = QtGui.QGridLayout()
        self.win.setLayout(self.layout)
        self.win.show()
        
    def update(self):
        self.data=self.data[-500:]
        if self.data:
            self.curve.setData(np.hstack(self.data))

    def addData(self,d):
        self.data.append(d)

# Let's create two instances of plot windows
qtPanningPlot1 = QtPanningPlot("Raw temperature")
qtPanningPlot2 = QtPanningPlot("Filtered temperature")
#initiallise IIRfilter
IirFilter = IIRFilter()



def callBack(data):
    #Normalise into ℃，optional, only useful in our project
    #data=data*5/0.01-2
    #plot rawsignal
    qtPanningPlot1.addData(data)
    #do filter
    data =IirFilter.dofilter(data)
    #plot filtered signal 
    qtPanningPlot2.addData(data)

# Get the Ardunio board.
board = Arduino(PORT)

# Set the sampling rate in the Arduino
board.samplingOn(1000 / samplingRate)

# Register the callback which adds the data to the animated plot
# The function "callback" (see above) is called when data has
# arrived on channel 0.
board.analog[0].register_callback(callBack)

# Enable the callback
board.analog[0].enable_reporting()


# showing all the windows
app.exec_()

# needs to be called to close the serial port
board.exit()

print("Finished")