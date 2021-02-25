#ruk.shan@outlook.com <roboy labs>
#read modbus registors
#25-02-2021 
#tested with URsim 5.6.4 and python 3.8.5

#!/usr/bin/python


from pyModbusTCP.client import ModbusClient
import sqlite3
from datetime import datetime
import time
from time import sleep
import math 

delay_mills = 0.05
#sleep
def sleep_delay():
    sleep(delay_mills)

def connect_to_UR():
    global modbus_conn
    modbus_conn = ModbusClient(host="192.168.153.136", port=502, auto_open=True)
    print ("connected to UR modbus")

#read UR joints
def read_joints_UR():
    global joints
    joints = modbus_conn.read_holding_registers(270,6)

#get time stamp
def get_time_stamp():
    global time_stamp
    # local_time = datetime.now(timezone.utc).astimezone()
    # time_stamp = local_time.isoformat()
    time_stamp = int(time.time())
    print(time_stamp)

#connect to sqlite database and create table
def sqlite_db_init():
    global db_conn, db_cursor
    db_conn =sqlite3.connect ('UR_robot_data.db')
    print ("Connected to the database")
    db_cursor = db_conn.cursor()
    
    #sCreate table
    try:
	    db_cursor.execute('''CREATE TABLE joints(
            time TEXT,
		    joint_1 INTEGER,
		    joint_2 INTEGER,
		    joint_3 INTEGER,
		    joint_4 INTEGER,
		    joint_5 INTEGER,
		    joint_6 INTEGER)''')
	    print ("Table created")
    except:
	    print ("Table exists")

#write data to database
def write_db():
    db_cursor.execute(
            "INSERT INTO joints (time,joint_1, joint_2, joint_3, joint_4, joint_5 , joint_6) VALUES (?, ?, ?, ?, ?, ?,?)"
            ,(time_stamp,joints[0],joints[1],joints[2],joints[3],joints[4],joints[5] ))
    db_conn.commit()
    print ("db updated")

connect_to_UR()
sqlite_db_init()
# read_joints_UR()
# write_db()

while True:
    sleep_delay()
    read_joints_UR()
    get_time_stamp()
    write_db()



