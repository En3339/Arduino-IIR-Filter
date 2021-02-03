# Arduino-IIR2-Filter-
Author: En Lu(2601258L) & Zhengyang Li (GUID:2567005L)
All right reserved

These scripts are focusing on an Arduino UNO API.

Before testing ,connect your computer with an arduino, and make sure
the arduino is uploaded firmata!(https://pypi.org/project/pyFirmata2/)
and make sure you have installed pyfirmata2 in your PC

If you are using an arduino uno, I recommand using pinA0 for DAQ

IIR2Filter.py: 		It is a IIR2Filter class definition. 
jitter_detector.py：		Run it in command window and it prints data in 50 secs with sampling rate of 100Hz. 
			Finally it prints 'finished' and total processing time(in nanoseconds)) By comparing the 
			number of samples and the number expected, you will find the changes in sampling rate.

realtime_iir_main.py:		Realtime IIR filter processing. Implement a 2 order Butterworth filter in realtime.
			After sampling data in real time, it is filtered by IIR Filter and showed.
			Run it in command window such as 'Anaconda Prompt (anaconda3)'
		
output_picture.py:		Optional
			Output picture: time domain diagram and power spectrum in real time
			Run it in command window such as 'Anaconda Prompt (anaconda3)'
