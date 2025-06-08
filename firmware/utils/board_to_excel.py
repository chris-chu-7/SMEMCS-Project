import time 
import serial 

#configuration
COM_PORT = 'COM5'
BAUD_RATE = 9600
CSV_PATH = r'C:\Users\chris\Documents\SMEMCS\sensor_test\sensor_log.csv'

#Open serial port, write to the csv file (this is listened to in python after the code is uploaded in arduino )
open_serial = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
time.sleep(2) # wait for the arduino reset action 
print("Logging data to the .csv file.")

with open(CSV_PATH, 'w') as file: 
    while True: 
        try: 
            line = open_serial.readline().decode('utf-8').strip()
            if line: 
                print(line)
                file.write(line + '\n')
        except Exception as e:
            print(f"Error: {e}")
            break
        
open_serial.close()