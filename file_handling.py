import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn 
import pandas as pd 

def isLineEmpty(line):
    return len(line.strip()) == 0

file1='Data/10Hz_Unbalance1_check2_run1.txt'
filetowrite = open("rpm.txt","w+") 

# ddddd = pd.read_csv("Data/01GENA001DP135RN.csv",thousands=';') 

# print(ddddd.shape)
# print(ddddd)
# err 

data1 = open(file1,"r")
lines1 = data1.readlines()[49:]

time =  []
rpm  =  []
acce1 =  []
acce2 =  []
acce3 =  []
acce4 =  []
acce5 =  []
time1 = np.arange(0,31.0005,0.000976563) 

i= 0 
for line in lines1:
    if not isLineEmpty(line):
        x = line.strip().split()
        x = np.asarray(x)
        rpm.append(float(x[1]))
        acce1.append(float(x[3]))
        acce2.append(float(x[5]))
        acce3.append(float(x[7]))
        acce4.append(float(x[9]))
        acce5.append(float(x[11]))

        
acce1 = np.asarray(acce1)
time1 = time1[1:2130]
rpm   = rpm  [:2129]
acce1 = acce1[:2129]
acce2 = acce2[:2129]
acce3 = acce3[:2129]
acce4 = acce4[:2129]
acce5 = acce5[:2129]

# plt.figure(figsize =(10,6))
# plt.plot(time1,acce1)
# plt.show()

for t,a in zip(time1,rpm):
    filetowrite.write("%f,%f\n"%(t,a))


fig, axs = plt.subplots(3,2)
axs[0,0].plot(time1,rpm)
axs[0,1].plot(time1,acce1)
axs[1,0].plot(time1,acce2)
axs[1,1].plot(time1,acce3)
axs[2,0].plot(time1,acce4)
axs[2,1].plot(time1,acce5)

for ax in fig.get_axes():
    ax.label_outer()

plt.show()