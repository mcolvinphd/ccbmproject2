import numpy as np
ntrials=2500
ndim=30
farray=np.empty(ndim)
for i in range (ndim):
    distarr=np.empty(ntrials)
    for j in range (ntrials):
        pt1=np.random.random(i+1)
        pt2=np.random.random(i+1)
        distarr[j]=np.sqrt(np.sum((pt1 - pt2)**2))
    farray[i]=np.mean(distarr)
print ("{:<10} {:<15} ".format('Dimension','Avg Dist'))
for i in range (ndim):
    print ("{:<10} {:<15} ".format(i+1, farray[i]))
