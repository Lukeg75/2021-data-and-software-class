#!/bin/python

# Import the libraries we are using. It is good practice to import all necessary
# libraries in the first lines of a file.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "data"))
print(data_directory)

results_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..", "results"))
print(results_directory)

input_file= "data_umbos.csv" 
print(input_file)

output_file = "data_output.json"
print (output_file)

input_filename = os.path.join(data_directory, input_file)
print(input_filename)

output_filename = os.path.join(results_directory, output_file)
print(output_filename)

# Create a function to read the data 
def read_data(filename):
    """This function reads data from a specified filename. The specified filename should point to .csv file. """
    # Create an array (a multi-dimensional table) out of our data file, full of text
    all_data = np.genfromtxt(filename, delimiter=',')
    print(all_data)

    # Select the data range we are interested in, convert it into a new array, full of numbers
    umbo_data = np.array(all_data[2:,1:3], dtype=float)
    print(umbo_data)
    return umbo_data

umbo_data = read_data(input_filename)

#1st function I figured out^
#Create a function to process the data
def processing_data(filename):
    """This function processes the data by appending a random column made up of 1000 umbos for each species """
    #Processing Data adding a random column of made up umbos
    random_umbos = (filename[:,1:None]- 0)*0 + 1000

    processed_umbo_data = np.append(filename, random_umbos,1)

    print(processed_umbo_data)
    return processed_umbo_data

processed_umbo_data = processing_data(umbo_data)
#2nd function I figured out^

# Create a figure of the processed data (I took out the random umbos)
# Create a function to plot the processed data

def create_plot(filename):
    "This function creates a plot of specified umbo data as bar graph. It must use a csv file that contains umbo counts. The csv file should be arranged so that the specified rows and columns are plotted"
    umbo_plot = plt.bar (umbo_data[:,1],umbo_data[:,0])
    plt.show(block=True)
    return umbo_plot

create_plot = plt.bar(umbo_data[:,1],umbo_data[:,0])
umbo_plot =create_plot
plt.show(block=True)

#4th function I figured out^

#Create a function to convert csv_to_json
def csv_to_json(filename):
    """This function reads an umbo csv list into a json file that is stored in the results folder. Taxon must be the name for the index column with a header of =1 """
    all_data = pd.read_csv(filename, index_col='Taxon', header =1)
    all_data.info()
    all_data.to_json(output_filename)
    return all_data
    
json_data = pd.read_json(output_filename)
#3rd function I figured out^

json_data.info()
print(json_data)
#no function for printing json_data, just a sanity check


#all_data = pd.read_csv("110-tavg-12-12-1950-2020.csv", index_col='Date', header=4)
#all_data.info()
#all_data.to_json("data_output.json")

#json_data = pd.read_json("data_output.json")
#json_data.info()
#print(json_data.loc['195012':'197512','Value']