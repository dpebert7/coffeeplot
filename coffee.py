import matplotlib.pyplot as plt
import matplotlib.figure as fig
import matplotlib.ticker as ticker
from matplotlib.ticker import AutoMinorLocator
import pandas as pd
import os
os.chdir("/home/david/Documents/GitRepos/coffeeplot")


from matplotlib.ticker import AutoMinorLocator

# One can supply an argument to AutoMinorLocator to
# specify a fixed number of minor intervals per major interval, e.g.:
minorLocator = AutoMinorLocator(3)
# would lead to a 2 minor ticks between major ticks.

#minorLocator = AutoMinorLocator()



#time = pd.Series([i for i in range(1,89)])

parker = pd.Series([0.5]*88)

mary = pd.Series([3.0]*6+[6.0]*32+[6.01]*10+[6.02]*10+[6.05]*10+[6.09]*10+[6.10]*2+[6.11]*2+[6.12]*2+[6.13]*2+[6.14]+6.15)

david = pd.Series([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                    0.05, 0.1, 0.1, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.05, 0.05, 
                    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                    0.0, 0.0, 0.01, 0.05, 0.1, 0.2, 0.25, 0.1, 0.05, 0.01, 0.0, 0.0, 
                    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.05, 0.1, 0.15, 0.2, 0.25, 
                    0.3, 0.25, 0.3, 0.4, 0.35, 0.35, 0.4, 0.35, 0.35, 0.35, 0.3, 0.35, 
                    1.0, 1.05, 1.1, 1.15])

joseph = pd.Series([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0,
                    2.0, 2.0, 2.0, 2.0, 3.0, 3.0, 3.0, 0.2, 0.2, 0.2, 0.3, 0.5,
                    1.0, 1.0, 1.0, 1.5, 2.0, 2.0, 2.0, 2.0, 2.0, 3.0, 3.0, 3.0,
                    3.0, 3.0, 3.0, 1.5, 1.5, 1.5, 1.5, 0.4, 0.4, 0.4, 0.4, 0.4,
                    0.4, 0.4, 1.0, 1.5, 1.5, 2.0, 2.0, 2.0, 2.5, 3.0, 3.0, 3.0,
                    3.5, 4.0, 4.0, 4.0, 3.0, 2.0, 1.0, 0.0, 0.0, 0.5, 1.0, 2.0, 
                    3.0, 1.0, 3.0, 1.0, 4.5, 3.0, 2.0, 3.25, 1.5, #np.nan, np.nan, 
                    3.0, 1.0, 2.75, 1.5, 2.5, 1.5, 2.5])

"""    
mikaela =pd.Series([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                    1.0, 1.0, 1.0, 1.0])
"""

adam = pd.Series([  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.05,
                    0.08, 0.12, 0.19, 0.36, 0.57, 0.72, 0.98, 1.22, 1.45, 1.66, 1.88, 1.99,
                    2.17, 2.26, 2.35, 2.42, 2.47, 2.48, 2.49, 2.5, 2.5, 2.5, 2.5, 2.5,
                    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                    1.1, 2.0, 4.0, 4.05, 4.09, 4.15, 4.17, 4.19, 4.22, 4.25, 4.27, 4.29,
                    4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3,
                    4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 5.95, 4.4, 4.4, 4.4, 4.4, 4.35,
                    4.3, 4.3, 4.3, 4.3])



xlabels = ["Aug '15", "Nov '15", "Feb '16", "May '16", "Aug '16", "Nov '16", "Feb '17", "May '17"]
ylabels = ["0","1","2","3","4","5","6+",""]            

plt.plot(x, y, 'ro')
# You can specify a rotation for the tick labels in degrees or with keywords.


threshold = 78
below = time <= threshold
above = time >= threshold

fig = plt.figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
with plt.xkcd():
    ax = plt.subplot(111)
    ax.plot(time[below], mary[below], 'b-')
    ax.plot(time[below], adam[below], 'g-')
    ax.plot(time[below], joseph[below], 'r-')
    ax.plot(time[below], parker[below], 'c-')
    ax.plot(time[below], david[below], 'm-')
    ax.plot(time[above], mary[above], 'b:')
    ax.plot(time[above], adam[above], 'g:')
    ax.plot(time[above], joseph[above], 'r:')
    ax.plot(time[above], parker[above], 'c:')
    ax.plot(time[above], david[above], 'm:')
    #ax.text(81.6, 2.9, r'??', fontsize = 16, color = 'red')
    #ax.text(81.5, 1.7, r'???', fontsize = 18, color = 'red')
    ax.xaxis.set_minor_locator(minorLocator)
    plt.tick_params(which='both', width=2)
    plt.tick_params(which='major', length=8)
    plt.tick_params(which='minor', length=4)
    #plt.xticks(np.arange(0,89,4.0))
    plt.xticks(np.arange(0, 89, 12.0), xlabels, rotation = 30)
    plt.yticks(np.arange(0,7,1.0), ylabels)
    plt.ylim(0,7)
    #plt.xlabel("Time")
    plt.ylabel("Cups of coffee per day")
    plt.title("GTA Coffee consumption")
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width*0.9, box.height])
    ax.legend(['Mary', 'Adam', 'Joseph', 'Parker', 'David'], bbox_to_anchor=(1.2, .75))
    plt.savefig('coffee.png')


"""
Matplotlib color options
b: blue
g: green
r: red
c: cyan
m: magenta
y: yellow
k: black
w: white
"""