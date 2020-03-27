import time
import os
import pandas

while True:
    if os.path.exists("files/temps_today.csv"):
        with open("files/temps_today.csv") as temps:

            data = pandas.read_csv("files/temps_today.csv")
            data2 = data.mean()
            print(data2["st1"])
    else:
        print("File does not exist")
    time.sleep(10)    


