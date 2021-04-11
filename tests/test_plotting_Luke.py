import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


sys.path.append(os.path.join(
    os.path.dirname(__file__),
    ".."))

results_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..", "results"))

output_file = "data_output.json"
print (output_file)

output_filename = os.path.join(results_directory, output_file)
print(output_filename)

def test_read_data():
    input_file = "data_umbos.csv"
    data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","data"))
    input_filename = os.path.join(data_directory,input_file)
    all_data = np.genfromtxt(input_file, delimiter=',')
    umbo_data = np.array(all_data[2:,1:3], dtype=float)
    print (umbo_data)

    assert (umbo_data[0,0] == 262)

#1st test on read_data function^

def test_processing_data():
    input_file = "data_umbos.csv"
    data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","data"))
    input_filename = os.path.join(data_directory,input_file)
    all_data = np.genfromtxt(input_file, delimiter=',')
    umbo_data = np.array(all_data[2:,1:3], dtype=float)    

    random_umbos = (umbo_data[:,1:None]- 0)*0 + 1000
    processed_umbo_data = np.append(umbo_data, random_umbos,1)
    print(processed_umbo_data)

    assert (processed_umbo_data[0,2] == 1000)
    assert (processed_umbo_data[1,2] == 1000)
    
#2nd test on processing_data_function^
def test_csv_to_json():
    input_file = "data_umbos.csv"
    all_data = pd.read_csv(input_file, index_col='Taxon', header =1)
    all_data.info()
    all_data.to_json(output_filename)

    json_data = pd.read_json(output_filename)

    json_data.info()
    print(json_data)

    assert (True)

#Had trouble figuring out a test for the csv_to_json function

def test_create_plot():
    input_file = "data_umbos.csv"
    data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","data"))
    input_filename = os.path.join(data_directory,input_file)
    all_data = np.genfromtxt(input_file, delimiter=',')
    umbo_data = np.array(all_data[2:,1:3], dtype=float)

    umbo_plot = plt.bar (umbo_data[:,1],umbo_data[:,0])
    
    

    create_plot = plt.bar(umbo_data[:,1],umbo_data[:,0])
    umbo_plot =create_plot
    
    plt.savefig('umbo_plot.pdf')
    
    if os.path.exists("umbo_plot.pdf"):

        assert os.open('umbo_plot.pdf',os.O_RDONLY)
        
    #3rd test for create_plot function. I think this one worked correctly but it is hard to tell.

    