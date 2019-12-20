import librosa
import math
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
from playsound import playsound

x, sr = librosa.load('worldholdon_bobsinclair.mp3')
####READING ANALYSIS
print("READING ANALYSIS")
print('Sample Rate - ', '{} Hz'.format(sr))
print('Number of Samples - ', '{}'.format(x.shape[0]))

####TIME ANALYSIS
print("TIME ANALYSIS")
mins = math.floor(x.shape[0]/(sr*60))
secs = math.floor((x.shape[0]/sr)%(60))
print('Duration - ', '{}:{}'.format(mins,secs))
print("ARRAY SAMPLE")


#####SECOND OF ANALYSIS
print("SPECTRUM ANALYSIS")
seconds_of_analysis = 4
samples_of_analysis = seconds_of_analysis * sr
print ('Number of Seconds to Analyze - ', '{}'.format(seconds_of_analysis))
print ('Number of Samples to Take- ', '{}'.format(samples_of_analysis))

#print("Time Series")
#t = np.arange(x.shape[0])/sr

# plt.figure(figsize=(14, 5))
# librosa.display.waveplot(x, sr=sr)
# plt.show()
# plt.plot(t,x)
# plt.ylabel('Time Series')
print(samples_of_analysis)
X = librosa.stft(x[0:samples_of_analysis])
Xdb = librosa.amplitude_to_db(abs(X),ref=np.max)
print(Xdb)
print(Xdb[20])
print(Xdb[0].shape)
print(Xdb.shape)
print(librosa.fft_frequencies(sr=22050, n_fft=2048))
# plt.figure(figsize=(14, 5))
# plt.plot(Xdb[0])
# plt.show()
plt.figure(figsize=(14, 5))
librosa.display.specshow(Xdb, y_axis='log', x_axis='time')
plt.title('Power spectrogram')
plt.colorbar(format='%+2.0f dB')
plt.tight_layout()
plt.show()
