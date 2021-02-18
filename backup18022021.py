import serial, time, csv, os
from datetime import date
from datetime import datetime
from skpy import Skype

# đăng nhập Skype
userSkype = 'asuzac-it.iot@outlook.com'# user, password skype
passSkype = 'iot@123987'
idChat = 'live:a697b99abc2b9460'

#khai báo cổng serial
port = 'COM6'

# biến đếm đọc lỗi
cout = 0

def connectSerial():
    # kết nối serial đọc dữ liệu
    try:
        global cout
        ser = serial.Serial(port, 9600)
        values = ser.readline()
        valueString = str(values)
        valSensor =  valueString[2:6]
        return(valSensor)
    except:
        # bật function báo lỗi mất kết nối thiết bị
        warning = '-'
        time.sleep(1)
        return (warning)

def writaData():
    value = connectSerial()
    # ngày giờ hiện tại
    current_day = date.today()
    current_time = datetime.now().strftime("%H:%M:%S")

    # filenow là file hiện tại
    file_now = str(current_day) +'.csv' 
    new_code_path = os.path.join(os.getcwd(),'csv', file_now)
    fp = os.path.exists(new_code_path)
    # đường dẫn đến các file csv
    path = 'csv/'+file_now
    #kiểm tra file hiện tại
    if(fp == True):
        file_csv = open(path, 'a+', newline='') 
        wr = csv.writer(file_csv)
        wr.writerow([current_day, current_time, value])
        file_csv.close()
        
        
    else:
        # cread write
        file_csv = open(path, 'a+', newline='') 
        wr = csv.writer(file_csv)
        wr.writerow([current_day, current_time, value])
        file_csv.close()

if __name__ == "__main__":
    while True:
        writaData()
        


