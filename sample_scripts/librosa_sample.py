import librosa
import math
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
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

# plt.figure(figsize=(14, 5))
# librosa.display.waveplot(x, sr=sr)
# plt.show()
# plt.plot(t,x)
# plt.ylabel('Time Series')

X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X),ref=np.max)
print(Xdb.shape)
plt.figure(figsize=(14, 5))
librosa.display.specshow(Xdb, y_axis='log', x_axis='time')
plt.title('Power spectrogram')
plt.colorbar(format='%+2.0f dB')
plt.tight_layout()
plt.show()
