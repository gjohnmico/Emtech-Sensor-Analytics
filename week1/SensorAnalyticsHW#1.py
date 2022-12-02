#Group Collaboration
#Balberan, Venus Rita Mae
#Baluyot, Jericho
#Delos Reyes, Abigail
#Guevarra, John Mico
#Lorzano, Daryl Khent
#Madrigal, Francis

#import library
import random as rd
import statistics as st

#generate sample of 100 random numbers between 1-100
sample = []
for i in range(0,100):
  n = rd.choice(range(1,100))
  sample.append(n)
print('The sample set is =', sample)

#calculate mean, median, mode
mean = st.mean(sample)
print('The mean is', mean)

median = st.median(sample)
print('The median is', median)

mode = st.multimode(sample)
print('The mode is', mode)