# Arduino-IIR-Filter
Author: En Lu & Zhengyang Li

All right reserved

These scripts are focusing on an Arduino UNO API.

Before testing ,connect your computer with an arduino, and make sure
the arduino is uploaded firmata!(https://pypi.org/project/pyFirmata2/)
and make sure you have installed pyfirmata2 in your PC

If you are using an arduino uno, I recommand using pinA0 for DAQ

IIR2Filter.py: 		An IIR2Filter class. 

jitter_detector.py	Run it in command window and it prints data in 50 secs with sampling rate of 100Hz. 
			Finally it prints 'finished' and total processing time(in nanoseconds)) By comparing the 
			number of samples and the number expected, you will find the changes in sampling rate.

realtime_iir_main.py:	Realtime IIR filter processing. Implement a 2 order Butterworth filter in realtime.
			After sampling data in real time, it is filtered by IIR Filter and showed.
			Run it in command window such as 'Anaconda Prompt (anaconda3)'
		
output_picture.py:	Optional
			Output picture: time domain diagram and power spectrum in real time
			Run it in command window such as 'Anaconda Prompt (anaconda3)'
			
Here is an example of filter result(Time Domain):
Original Signal:




![image](https://user-images.githubusercontent.com/56938146/155969197-ce001f8d-d175-49d4-baad-23bb39b98a61.png)







Filtered:






![image](https://user-images.githubusercontent.com/56938146/155969332-b1cc16b2-55da-46c7-8673-16c407c48515.png)






