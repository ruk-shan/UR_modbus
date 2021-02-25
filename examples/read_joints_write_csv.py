
#ruk.shan@outlook.com <roboy labs>
#read modbus registors
#25-02-2021 
#tested with URsim 5.6.4 and python 3.8.5

#To DO > CSV filepath

import pandas as pd
from pyModbusTCP.client import ModbusClient
import datetime
import time
import pytz
import csv

#get date and time
time_now = time.time()
def get_timestamp():
    global time_stamp
    # time_stamp = datetime.datetime.now(tz=pytz.UTC)
    time_stamp  = time.time() - time_now

#connect to UR
def connect_to_UR():
    global modbus_conn
    modbus_conn = ModbusClient(host="192.168.153.136", port=502, auto_open=True)
    # modbus_conn = ModbusClient(host="192.168.1.19", port=502, auto_open=True)
    print ("connected to UR modbus")
    # print (modbus_conn)

#read UR joints
def read_joints_UR():
    global json_joints
    joints = modbus_conn.read_holding_registers(270,6)
    if joints == None:
        print ("No data recieved..!!")
    else:
        # print (joints)
        json_joints = [
                    {
            "timestamp": time_stamp,
            "joint_1": joints[0],
            "joint_2": joints[1],
            "joint_3": joints[2],
            "joint_4": joints[3],
            "joint_5": joints[4],
            "joint_6": joints[5]
                    }
                ]

#create to CSV
def crate_csv():
    col_names = ["timestamp","joint_1","joint_2", "joint_3","joint_4","Joint_5","joint_6"]
    df = pd.DataFrame([
                    {
            "timestamp": 0,
            "joint_1": 0,
            "joint_2": 0,
            "joint_3": 0,
            "joint_4": 0,
            "joint_5": 0,
            "joint_6": 0
                    }
                ])
    df.to_csv("/home/shan/MyWork/UR_graphs/CSV/file1.csv", header=col_names)

#write to CSV
def write_to_csv():
    df = pd.DataFrame(json_joints)
    df.to_csv("/home/shan/MyWork/UR_graphs/CSV/file1.csv", mode='a', header=False)
    print ("data written to the file")


connect_to_UR()
crate_csv()

while True:
    get_timestamp()
    read_joints_UR()
    write_to_csv()
