import serial, time, csv, os
from datetime import date
from datetime import datetime
#ngay hien tai
day = date.today()
filenow = str(day) +'.csv' # filenow là file hiện tại

new_code_path = os.path.join(os.getcwd(),'csv', filenow)
fp = os.path.exists(new_code_path)
if(fp == True):
    #append value
    print("yes")
else:
    # cread write
    file = open('csv/value.csv', 'w', newline='')
    writer = csv.writer(file)
    

# f = os.listdir('csv')
# print(f[-1])
# new_code_path = os.path.join(os.getcwd(),'csv', 'abc.csv')
# t = os.path.exists(new_code_path)
# if(t==True):
#     print()
# print(t)

