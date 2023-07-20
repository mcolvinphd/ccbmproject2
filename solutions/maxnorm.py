import numpy as np
import matplotlib.pyplot as plt

N = 200 #number of random values
ntrials = 5000 #number of trials
mu = 0.0
sd = 1.0
maxes = np.zeros(200)

#Loop over values of N (1 to 200):
for i in range(N):
    #Initialize sum variable to zero for calculating average maximum value
    sum = 0
    #Loop over trial (0 to ntrials-1):
    for j in range(ntrials):
        #Calculate set of N normally distributed random numbers (NumPy)
        set = np.random.normal(mu, sd, i+1)
        #Select largest value (NumPy)
        max_val = np.max(set)
        #Add largest value to sum variable
        sum += max_val
    #Divide sum by number of trials to get average maximum value
    av_max = sum/ntrials
    #Store the average maximum value in an array
    maxes[i] = av_max

#Plot the average maximum values vs N using matplotlib
plt.plot(range(1,N+1),maxes)
plt.title("Largest of N normally distributed numbers using NumPy")
plt.xlabel("N")
plt.ylabel("Mean Maximum Value")
plt.show()