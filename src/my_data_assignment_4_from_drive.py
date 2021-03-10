#!/bin/python

# Import the libraries we are using. It is good practice to import all necessary
# libraries in the first lines of a file.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def read_data():
    # Create an array (a multi-dimensional table) out of our data file, full of text
    all_data = np.genfromtxt("data/Data_umbos.csv", delimiter=',')
    print(all_data)

    # Select the data range we are interested in, convert it into a new array, full of numbers
    umbo_data = np.array(all_data[2:,1:3], dtype=float)
    print(umbo_data)
    return umbo_data

umbo_data = read_data()

#Processing Data adding a random column of made up umbos
random_umbos = (umbo_data[:,1:None]- 0)*0 + 1000

processed_umbo_data = np.append(umbo_data, random_umbos,1)

print(processed_umbo_data)
# Create a figure of the processed data (I took out the random umbos)
umbo_figure = plt.figure
umbo_plot = plt.bar (umbo_data[:,1],umbo_data[:,0])
plt.show(block=True)

all_data = pd.read_csv("data/Data_umbos.csv", index_col='Taxon', header =1)
all_data.info()
all_data.to_json("results/data_output.json")

json_data = pd.read_json("results/data_output.json")
json_data.info()
print(json_data)

#all_data = pd.read_csv("110-tavg-12-12-1950-2020.csv", index_col='Date', header=4)
#all_data.info()
#all_data.to_json("data_output.json")

#json_data = pd.read_json("data_output.json")
#json_data.info()
#print(json_data.loc['195012':'197512','Value'])