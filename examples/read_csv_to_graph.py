
#ruk.shan@outlook.com <roboy labs>
#read modbus registors
#25-02-2021 
#tested with URsim 5.6.4 and python 3.8.5
#To Do File path 


import pandas as pd
import datetime
import pytz
import csv
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np


#get date and time
def get_timestamp():
    global time_stamp
    time_stamp = datetime.datetime.now(tz=pytz.UTC)

#read csv
def read_csv():
    global df
    df = pd.read_csv("/home/shan/MyWork/UR_graphs/CSV/file1.csv")    
    print (df)


#graph
def draw_graph():
    y = df.joint_1
    x = df.timestamp
    plt.plot(x, y)
    plt.show()

read_csv()
draw_graph()
