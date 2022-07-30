
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df=pd.read_csv("studentMarks.csv")
data=df["Math_score"].tolist()


#calculating mean and std deviation

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean



mean_list = []
for i in range(0,1000):
     set_of_means= random_set_of_mean(100)
     mean_list.append(set_of_means)
    
    
mean = statistics.mean(mean_list)
print("Mean of sampling distribution :-",mean )

st_dev=statistics.stdev(mean_list)
print("ST Dev of sampling distribution- ", st_dev)

mean = statistics.mean(data)
print("Mean of distribution :-",mean )

st_dev=statistics.stdev(data)
print("ST Dev of distribution- ", st_dev)

first_std_deviation_start,first_std_deviation_end=mean-st_dev,mean+st_dev
second_std_deviation_start,second_std_deviation_end=mean-(2*st_dev),mean+(2*st_dev)
third_std_deviation_start,third_std_deviation_end=mean-(3*st_dev),mean+(3*st_dev)


print("std1",first_std_deviation_start, first_std_deviation_end)
print("std2",second_std_deviation_start, second_std_deviation_end)
print("std3",third_std_deviation_start, third_std_deviation_end)


#mean of data set 
#df=pd.read_csv("data1.csv")
#data=df["Math_score"].tolist()
#mean_of_sample1=statistics.mean(data)
#print("Mean of Sample 1 :-",mean_of_sample1)
#fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
#fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
#fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN OF STUDNETS WHO GOT FUNSHEETS"))
#fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
#fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
#fig.show()

#df=pd.read_csv("data2.csv")
#data=df["Math_score"].tolist()
#mean_of_sample2=statistics.mean(data)
#print("Mean of Sample 2 :-",mean_of_sample2)
#fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
#fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
#fig.add_trace(go.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0, 0.17], mode="lines", name="MEAN OF STUDNETS WHO GOT FUNSHEETS"))
#fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
#fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
#fig.show()

#df=pd.read_csv("data3.csv")
#data=df["Math_score"].tolist()
#mean_of_sample3=statistics.mean(data)

#print("Mean of Sample 3 :-",mean_of_sample1)
#fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
#fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
#fig.add_trace(go.Scatter(x=[mean_of_sample3, mean_of_sample3], y=[0, 0.17], mode="lines", name="MEAN OF STUDNETS WHO GOT FUNSHEETS"))
#fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
#fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
#fig.show()

#School_Sample

df=pd.read_csv("School_1_Sample.csv")
data=df["Math_score"].tolist()
mean_of_sample1=statistics.mean(data)
print("Mean of Sample 1 :-",mean_of_sample1)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN OF STUDNETS WHO GOT FUNSHEETS"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

df=pd.read_csv("School_2_Sample.csv")
data=df["Math_score"].tolist()
mean_of_sample2=statistics.mean(data)
print("Mean of Sample 2 :-",mean_of_sample2)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0, 0.17], mode="lines", name="MEAN OF STUDNETS WHO GOT FUNSHEETS"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

df=pd.read_csv("School_3_Sample.csv")
data=df["Math_score"].tolist()
mean_of_sample3=statistics.mean(data)
print("Mean of Sample 3 :-",mean_of_sample3)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample3, mean_of_sample3], y=[0, 0.17], mode="lines", name="MEAN OF STUDNETS WHO GOT FUNSHEETS"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

z_score=(mean-mean_of_sample1)/st_dev
print("Z_Score 1 is- ", z_score)

z_score=(mean-mean_of_sample2)/st_dev
print("Z_Score 2 is- ", z_score)

z_score=(mean-mean_of_sample3)/st_dev
print("Z_Score 3 is- ", z_score)