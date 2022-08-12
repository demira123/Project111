import pandas as pd
import random as r
import statistics as st
import plotly.figure_factory as pff

data = pd.read_csv("project111.csv")


readingTime = data["reading_time"].tolist()

graph=pff.create_distplot([readingTime],["reading_time"],show_hist=False)
graph.show()

mean = st.mean(readingTime)
stdev = st.stdev(readingTime)

print("Mean Of Population : " , mean)

print("stdev Of Population : " , stdev)

print("------------------------------------")


# -----------------------------------------------------------

dataSet=[]

for i in range(0,100):
    f=[]
    for g in range(0,30):
        f.append(r.choice(readingTime))

    dataSet.append(st.mean(f))
    
MeanofSample=st.mean(dataSet)
stdevofSample=st.stdev(dataSet)

print("Mean Of Sample : " , MeanofSample)

print("stdev Of sample : " , stdevofSample)

print("------------------------------------")

graph=pff.create_distplot([dataSet],["reading_time"],show_hist=False)
graph.show()



