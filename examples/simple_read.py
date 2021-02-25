#ruk.shan@outlook.com <roboy labs>
#read modbus registors
#25-02-2021 
#tested with URsim 5.6.4 and python 3.8.5

#!/usr/bin/python

from pyModbusTCP.client import ModbusClient

#connect to UR
def connect_to_UR():
    global modbus_conn
    modbus_conn = ModbusClient(host="192.168.153.136", port=502, auto_open=True) #host ip is ROBOT's ip
    print ("connected to UR modbus")

#read UR joints
def read_reg_UR():
    reg = modbus_conn.read_holding_registers(206,1)
    return reg

def main():
    connect_to_UR()
    print (read_reg_UR())

if __name__ == "__main__":
    main()
