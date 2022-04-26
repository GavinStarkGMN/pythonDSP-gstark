import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.signal as sig
from scipy.io import wavfile
from time import process_time_ns

CHANNELS = 1
FS = 16000
BLKSIZE = int(.020 * FS)        # modify this value to make sure many blocksizes work
xp2 = np.ceil(np.log2(BLKSIZE))
fftsize = int(np.power(2, xp2))

def pad(input, size, begin=0):
    output = np.zeros(size)
    for i in range(len(input)):
        if i >= len(input) or i + begin >= len(output):
            break
        output[i + begin] = input[i]
    return output

# process the input and fir filter.
# the function is expected to process the buffer in blocks of a configurable size
# input : numpy array of float32 limited to [-1,1]
# h: fir numerator coefficients
def stftFilter(input,h):
    output = np.zeros(len(input))
    bfft = np.fft.fft(pad(b, BLKSIZE * 2))
    # you can implement the block processing however you like, this is just an example
    for i in range(0, len(input), BLKSIZE):
        ''' ************* YOUR CODE HERE ************* '''
        fft = np.fft.fft(pad(input[i:i+BLKSIZE], BLKSIZE * 2))
        ifft = np.fft.ifft(fft * bfft)
        output += pad(ifft.real, len(output), i)
    return output


testfileLengthInSeconds = 30
t = np.arange(testfileLengthInSeconds*FS)/FS
# create an input signal
inp = sig.chirp(t,1,testfileLengthInSeconds,10000)
# create an fir filter
b = sig.firwin(5,.3)
bfft = np.fft.fft(pad(b, len(inp)))

#process the input via one huge fft arrray
fftStart = process_time_ns()

''' ************* YOUR CODE HERE ************* '''
fft = np.fft.fft(inp)
ifft = np.fft.ifft(fft * bfft)
y = ifft.real

fftEnd = process_time_ns()
fftExecTime = fftEnd - fftStart
print("FFT execution time: %i ms" % (fftExecTime/1000))


fftStartBlocks = process_time_ns()
#process the input in blocks
yBlocks = stftFilter(inp,b)
fftEndBlocks = process_time_ns()
fftExecTimeBlocks = fftEndBlocks - fftStartBlocks
print("FFT block execution time: %i ms" % (fftExecTimeBlocks/1000))


convStart = process_time_ns()
#generate a reference answer using convolution
ref = sig.convolve(inp,b)
convEnd = process_time_ns()
convExecTime = convEnd - convStart
print("convolution execution time: %i ms" % (convExecTime/1000))

#plot the results
fig = plt.figure()
# plot the specgram
ax1 = plt.subplot(211)
f, t, Sxx = sig.spectrogram(y,fs=FS,nfft=fftsize)
ax1.pcolormesh(t, f, Sxx, shading='gouraud')
# also there is an easier to use specgram from pylab
plt.ylabel('Ref Freq[Hz]')

# plot the time response
ax2 = plt.subplot(212)
ax2.plot(y,label='y')
ax2.plot(yBlocks,label='yBlocks')
ax2.plot(ref,label='ref')
plt.xlabel('Time [sec]')
plt.legend()

plt.pause(.1)
plt.show()
