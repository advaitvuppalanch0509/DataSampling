import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["data"].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 10], mode="lines", name="MEAN"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(64)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    
mean = statistics.mean(data)
print(mean)
median = statistics.median(data)
print(median)
mode = statistics.mode(data)
print(mode)
stddev=statistics.stdev(data)
print(stddev)

setup()
population_mean = statistics.mean(data)
print("population mean:- ", population_mean)

def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)

    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution:- ", std_deviation)

standard_deviation()

first_stddev_start = mean - stddev
first_stddev_end = mean + stddev


fig = ff.create_distplot([data], ["temp"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 2], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_stddev_start, first_stddev_start], y=[0, 2], mode="lines", name="STANDARD DEVIATION"))
fig.add_trace(go.Scatter(x=[first_stddev_end, first_stddev_end], y=[0, 2], mode="lines", name="STANDARD DEVIATION"))
fig.show()


