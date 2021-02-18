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
        # cout = 0
        # print(valSensor)
        return(valSensor)
    except:
        # bật function báo lỗi mất kết nối thiết bị
        warning = '-'
        # sendWarning()
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
        # time.sleep(0.5)
        
    else:
        # cread write
        file_csv = open(path, 'a+', newline='') 
        wr = csv.writer(file_csv)
        wr.writerow([current_day, current_time, value])
        file_csv.close()
        # time.sleep(0.5)

      
# def sendWarning():
#     # đặt biến đếm 
#     global cout
#     flat = 20
#     cout += 1
    
#     if(cout == 1):
#         skypeWarning()
#     if(cout == flat):
#         skypeWarning()

#     print('gửi cảnh báo thông qua skype')

# def skypeWarning():
#     # gửi cảnh báo đến bảo trì
#     print('connect skype ....')
#     sk = Skype(userSkype,passSkype) # đăng nhập skype
#     contact = sk.contacts[idChat] # ip người nhận msg         
#     contentMess ='Test send warning'
#     contact.chat.sendMsg(contentMess) # gửi msg thông báo




if __name__ == "__main__":
    while True:
        writaData()
        

# while True:


