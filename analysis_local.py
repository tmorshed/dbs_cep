## Importing packages and files

    #import os
    
#reset -sf

import numpy as np
import mne
import matplotlib.pyplot as plt
import scipy.signal as sg


raw = mne.io.read_raw_cnt(r"C:\Users\taham\OneDrive - UHN\Projects\DBS\Data\recieved\ChenLab\Recieved\130Hz_STN_ON_LeftSTIM.cnt", preload=False)
#preload=True makes it load to RAM as well. Normally, it only loads the symlinks to the RAM and the data stays in the local storage


##Choose channel to analyze                                                     #Please input the desired channel name
ch_choice = ['L3']
#Choose the times below. We will crop the file in this  window.
start_stop_seconds = np.array([0, 15])                                         #Please select start and end crop times in seconds

##Import metadata to internal variables
n_time_samps = raw.n_times
time_secs = raw.times
ch_names = raw.ch_names
n_chan = len(ch_names)
sampling_rate= raw.info['sfreq']
dt=1/sampling_rate


## Print some metadata
print('the imported data object has {} time samples and {} channels.'
''.format(n_time_samps, n_chan))
print('The last time sample is at {} seconds.'.format(time_secs[-1]))
print()  # insert a blank line in the output
print('sampling frequency is {}'.format(sampling_rate, 'Hz'))           
print('MISC INFO: {}'.format(raw.info['description'], '\n')) #misc  info

print(raw.info)

print() #adding an extra row 
print()
print('The sensor locations on the cranium:')

print(raw.info)

print() #adding an extra row 
print()
print()

print('The sensor locations on the cranium:')
raw.plot_sensors(show_names=True)
print('The sensor locations in 3D:')
raw.plot_sensors('3d')

#Cropping the file
raw_select = raw.copy().load_data()
raw_select.crop(tmin=start_stop_seconds[0], tmax=start_stop_seconds[1], include_tmax=True);
raw_select.pick_channels(ch_choice);
raw_select.load_data()
start_sample, stop_sample = (start_stop_seconds * sampling_rate).astype(int)
times=np.arange(start_stop_seconds[0],start_stop_seconds[1],dt)

#extracting some internal variables from above input
duration_selection = start_stop_seconds[1]-start_stop_seconds[0]
start_sample, stop_sample = (start_stop_seconds * sampling_rate).astype(int)
times=np.arange(start_stop_seconds[0],start_stop_seconds[1],dt)
lsel=len(times)
times=times.reshape(1,lsel)

#printing some metadata
print('We will use the timewindow of {} to {} seconds.'.format(start_stop_seconds[0],start_stop_seconds[1]))
print('this is equal to {} milliseconds in length'.format(duration_selection*1000))
print('this is equal to {} datapoints in length'.format(lsel))
raw_select.plot(duration = duration_selection, );



#Find Spikes



