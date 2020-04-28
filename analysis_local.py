## Importing packages and files

    #import os
    

import numpy as np
import mne
import matplotlib.pyplot as plt
import scipy.signal as sg


raw = mne.io.read_raw_cnt(r"C:\Users\taham\OneDrive - UHN\Projects\DBS\Data\recieved\ChenLab\Recieved\Stop-signal_eDBS_Dec17_2018_s05-Block1.cnt", preload=False)
#preload=True makes it load to RAM as well. Normally, it only loads the symlinks to the RAM and the data stays in the local storage


##Choose channel to analyze        #Please input the desired channel name
ch_choice = ['R1']

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
print('MISC INFO: {}'.format(raw.info['description'], '\n'))      #miscellaneous acquisition info

print(raw.info)

print() #adding an extra row 
print()
print('The sensor locations on the cranium:')
raw.plot_sensors();

## Print some metadata
print('the imported data object has {} time samples and {} channels.'
''.format(n_time_samps, n_chan))
print('The last time sample is at {} seconds.'.format(time_secs[-1]))
print('The first few channel names are {}.'.format(', '.join(ch_names[:3])))
print()  # insert a blank line in the output
print('sampling frequency is {}'.format(sampling_rate, 'Hz'))           
print('MISC INFO: {}'.format(raw.info['description'], '\n'))      #miscellaneous acquisition info

print(raw.info)

print() #adding an extra row 
print()
print()

print('The sensor locations on the cranium:')
raw.plot_sensors()
print('The sensor locations in 3D:')
raw.plot_sensors('3d')

#Choose the times below. We will crop the file in this  window.
start_stop_seconds = np.array([16, 16.2]) #select start and end crop times in seconds

#Cropping the file
raw_select=raw.crop(tmin=start_stop_seconds[0], tmax=start_stop_seconds[1], include_tmax=False)
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
raw.plot();


#find events:
amp_max=(max(raw_select[0]))
amp_th=amp_max/5
indx, lrpeaks = sg.find_peaks(raw_select[0], threshold=amp_th)
ltpeaks=lrpeaks['left_thresholds']
rtpeaks=lrpeaks['right_thresholds']
indx_seconds = (indx * dt) + start_stop_seconds[0]
peaks = raw_select._data[0][indx]

ind_pks = list(np.zeros((2,len(indx)), dtype=float))




print("plotting the data")
fig = plt.figure()
axes = fig.add_axes([0, 0, 1, 1]); # left, bottom, width, height
axes.plot(times[0], raw_select[0], 'k');
axes.scatter(indx_seconds, peaks)
axes.set_xlabel('times in seconds');
axes.set_ylabel('activation from baseline, in mV');
plt.show()

##indx = find([0;sig]<Amp_th & [sig;0]>=Amp_th);



# Preprocessing
