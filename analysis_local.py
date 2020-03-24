## Importing packages and files

import numpy as np
import mne
fullraw = mne.io.read_raw_cnt(r"C:\Users\taham\OneDrive - UHN\DBS_PD\Data\recieved\ChenLab\Recieved\130Hz_STN_ON_LeftSTIM.cnt", verbose='INFO')


##Import metadata
n_time_samps = raw.n_times
time_secs = raw.times
ch_names = raw.ch_names
n_chan = len(ch_names)
sampling_rate= raw.info['sfreq']

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
channel_index = 0


#Choose time window to analyze
start_stop_seconds = np.array([11, 13]) #select start and end crop times in seconds
start_sample, stop_sample = (start_stop_seconds * sampling_rate).astype(int)
raw_selection = raw[channel_index, start_sample:stop_sample]

## Loading to RAM and plotting using MNE. Choose only one channel. The whole time

# Preprocessing
    # Lowpass filter = 10 Hz
    # Highpass filter = 200 Hz. Our stimulation is at 130-150 Hz max and will not be affected by this

print("loading the data to RAM and plotting")
raw.crop().load_data() # add tmax or tmin if only a specific period is needed
fig1=raw.plot #raw.plot(highpass=200, lowpass=10)