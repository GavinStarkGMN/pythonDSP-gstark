import numpy as np
import scipy.signal as sig
import matplotlib.pylab as plt

# build a triangle wave as input
x = np.append(np.arange(5),np.arange(5)[::-1])
# and a square wave as the filter
h = np.append(np.append(np.zeros(5),np.ones(5)),np.zeros(5))


# setup the figure with two subplots
fig = plt.figure(1)
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)

# plot the signals in top subplot as a reference
ax1.plot(x)
ax1.plot(h)

# make zero buffer y
y = np.zeros(len(h)+len(x)-1)

def convolve(f, g, t):
    # this function represents the equation:
    # [f * g](t) = integral (from 0 to t) f(i)g(t-i) di
    output = 0
    for i in range(t):
        if i > t or i >= len(f) or t-i >= len(g):
            continue
        output += f[i] * g[t-i]
    return output

for n in range(len(y)):
    # do each step of the convolution here
    # and print each set of results in the 2nd subplot
    y[n] = convolve(x, h, n)
    ax2.clear()
    ax2.plot(y)
    plt.pause(.1)


# compute the convolution in time as the reference answer
ref = sig.convolve(x,h)
err = ref - y

# plot results
fig2 = plt.figure(2)
ax21 = plt.subplot(111)
ax21.plot(ref,label='ref')
ax21.plot(y,label='y')
ax21.legend()
plt.pause(.1)   # non blocking render
plt.show()      # blocking render
