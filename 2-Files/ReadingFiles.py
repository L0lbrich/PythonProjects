import time
import os
import pandas


while True:
    if os.path.exists('Data.csv'):
        data = pandas.read_csv("Data.csv")
        print(data.mean()['st1'])
    else:
        print('file does not exit')
    time.sleep(10) 