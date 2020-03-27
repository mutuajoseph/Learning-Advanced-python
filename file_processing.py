import time
import os

while True:
    if os.path.exists("veges.txt"):
        with open("veges.txt") as veges:
            print(veges.read())
    else:
        print("FIle not found")

    time.sleep(10) 


