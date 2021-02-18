import serial, time, csv
from datetime import date
from datetime import datetime
#khai báo cổng serial
ser = serial.Serial('COM6', 9600)
time.sleep(1)

# ngày giờ hiện tại
day = date.today()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
filenow = 'paintFactory' + '_' + day +'.csv'

# def readValue():
#     v = ser.readline()
#     valueString = str(v)
#     valu =  valueString[2:6] 
#     return valu
def createFile():
    new_code_path = os.path.join(os.getcwd(),'csv', 'abc.csv')
    t = os.path.exists(new_code_path)
    if(t == True):
        #ghi vào file

    
with open('csv/value.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Data", "Time", "Value"])
    while True:
        day = date.today()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        values = ser.readline()
        print(values)
        valueString = str(values)
        v =  valueString[2:6]   
        writer.writerow([day, current_time, v])
        time.sleep(1)
    