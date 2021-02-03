#author: Zhengyang Li & En Lu
from pyfirmata2 import Arduino
import time
PORT = Arduino.AUTODETECT
class AnalogPrinter:

    def __init__(self):
        # sampling rate: 100Hz
        self.samplingRate = 100
        self.timestamp = 0
        self.board = Arduino(PORT)

    def start(self):
        self.board.analog[0].register_callback(self.myPrintCallback)
        self.board.samplingOn(1000 / self.samplingRate)
        self.board.analog[0].enable_reporting()

    def myPrintCallback(self, data):
        print("%f,%f" % (self.timestamp, data))
        self.timestamp += 1

    def stop(self):
        self.board.samplingOff()
        self.board.exit()

print("Let's print data from Arduino's analogue pins for 50secs.")

# Let's create an instance
analogPrinter = AnalogPrinter()

# and start DAQ
analogPrinter.start()
a=time.time_ns()
# let's acquire data for 50secs. We could do something else but we just sleep!
time.sleep(50)


# let's stop it
analogPrinter.stop()
b=time.time_ns()
c=b-a


print("finished", c,"ns")
