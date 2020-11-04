import speedtest
import datetime
import time
import csv 


MB_Converter = 1048576

s = speedtest.Speedtest()

with open('i_speed.csv', 'w') as fs:

    csv_writer = csv.DictWriter(fs, fieldnames=['time', 'downspeed', 'upspeed'])
    csv_writer.writeheader()

    while True:
        time_now = datetime.datetime.now().strftime('%H:%M:%S')
        down_speed =  round ( s.download() / MB_Converter , 2 )
        up_speed = round ( s.upload()  / MB_Converter , 2 )
        csv_writer.writerow({
            'time': time_now,
            'downspeed': down_speed,
            'upspeed': up_speed
        })
        print(f'Time : {time_now},  Download : {down_speed} Mb/s , Upload: {up_speed} Mb/s')
        time.sleep(60)



