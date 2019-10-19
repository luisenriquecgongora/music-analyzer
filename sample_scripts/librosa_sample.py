import librosa
import math
import numpy as np
import matplotlib.pyplot as plt
from playsound import playsound

x, sr = librosa.load('worldholdon_bobsinclair.mp3')
## SR is Sample Rate
#print(sr)
## X is Shape
## Each data point is frequency over time
#print(x.shape)

print("GENERAL ANALYSIS")
mins = math.floor(x.shape[0]/(sr*60))
secs = math.floor((x.shape[0]/sr)%(60))
print('Duration - ', '{}:{}'.format(mins,secs))
print("ARRAY SAMPLE")

print("Time Series")
t = np.arange(x.shape[0])/sr
#print(t)


plt.plot(t,x)
plt.ylabel('Time Series')
plt.show()

#playsound('worldholdon_bobsinclair.mp3')
