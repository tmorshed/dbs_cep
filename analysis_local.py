## Importing packages and files

    #import os
import numpy as np
import mne
import matplotlib.pyplot as plt
import scipy.signal as sg
raw = mne.io.read_raw_cnt(r"C:\Users\taham\OneDrive - UHN\Projects\DBS\Data\recieved\ChenLab\Recieved\130Hz_STN_ON_LeftSTIM.cnt", verbose='INFO',preload=False)
#preload=True makes it load to RAM as well. Normally, it only loads the symlinks to the RAM and the data stays in the local storage


##Import metadata
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
print('The first few channel names are {}.'.format(', '.join(ch_names[:3])))
print()  # insert a blank line in the output
print('sampling frequency is {}'.format(sampling_rate, 'Hz'))           
print('MISC INFO: {}'.format(raw.info['description'], '\n'))      #miscellaneous acquisition info

print(raw.info)

print() #adding an extra row 

##Choose channel to analyze
channel_name = ['R2']


#Choose time window to analyze
start_stop_seconds = np.array([11, 11.2]) #select start and end crop times in seconds
start_sample, stop_sample = (start_stop_seconds * sampling_rate).astype(int)
times=np.arange(start_stop_seconds[0],start_stop_seconds[1],dt)
lsel=len(times) #number of datapoints in the selected time window
times=times.reshape(1,lsel)
raw_selection = np.asarray(raw[channel_name, start_sample:stop_sample])[0] 
#raw_selection.append(np.arange[start_stop_seconds[0],start_stop_seconds[1],dt])
#raw_selection.append(-1*raw_selection[0].T) #correcting the dimensions
#del raw_selection[0]
raw_selection=np.average(raw_selection)-raw_selection # re-aligned from zero


#find events:
amp_max=(max(raw_selection[0]))
amp_th=amp_max/5
indx, lrpeaks = sg.find_peaks(raw_selection[0], threshold=amp_th)
ltpeaks=lrpeaks['left_thresholds']
rtpeaks=lrpeaks['right_thresholds']
indx_seconds = (indx * dt) + start_stop_seconds[0]
peaks = raw_selection[0][indx]

ind_pks = list(np.zeros((2,len(indx)), dtype=float))

for i in range(1:lsel):
    if i>=amp_th:
        ind_pks
        


print("plotting the data")
fig = plt.figure()
axes = fig.add_axes([0, 0, 1, 1]); # left, bottom, width, height
axes.plot(times[0], raw_selection[0], 'k');
axes.scatter(indx_seconds, peaks)
axes.set_xlabel('times in seconds');
axes.set_ylabel('activation from baseline, in mV');
plt.show()

##indx = find([0;sig]<Amp_th & [sig;0]>=Amp_th);



# Preprocessing
    # Lowpass filter = 10 Hz
    # Highpass filter = 200 Hz. Our stimulation is at 130-150 Hz max and will not be affected by this
