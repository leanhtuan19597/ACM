import serial, time, csv,os
from datetime import date
from datetime import datetime

#khai báo cổng serial
port = 'COM6'
ser = serial.Serial(port, 9600)
time.sleep(1)
while True:
    # ngày giờ hiện tại
    current_day = date.today()
    current_time = datetime.now().strftime("%H:%M:%S")

    # filenow là file hiện tại
    file_now = str(current_day) +'.csv' 

    new_code_path = os.path.join(os.getcwd(),'csv', file_now)
    fp = os.path.exists(new_code_path)
    path = 'csv/'+file_now
    print(fp)
    if(fp == True):
        #append value
        # filenow là file hiện tại
        file_csv = open(path, 'a+', newline='') 
        wr = csv.writer(file_csv)

        values = ser.readline()
        valueString = str(values)
        val =  valueString[2:6]
        print(val)
        wr.writerow([current_day, current_time, val])
        file_csv.close()
        time.sleep(1)
    else:
        # cread write
        file_csv = open(path, 'a+', newline='') 
        wr = csv.writer(file_csv)

        values = ser.readline()
        valueString = str(values)
        val =  valueString[2:6]
        print(val)
        wr.writerow([current_day, current_time, val])
        file_csv.close()
        time.sleep(1)


