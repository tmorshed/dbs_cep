# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:13:31 2020

@author: taham
"""




#find events:
amp_max=(max(raw[0]))
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
