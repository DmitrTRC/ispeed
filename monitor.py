import speedtest
import datetime
import time


MB_Converter = 1048576

s = speedtest.Speedtest()
while True:
    time_now = datetime.datetime.now().strftime('%H:%M:%S')
    down_speed =  round ( s.download() / MB_Converter , 2 )
    up_speed = round ( s.upload()  / MB_Converter , 2 )

    print(f' Download : {down_speed} , Upload: {up_speed}')



