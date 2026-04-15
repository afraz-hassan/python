import os
import time

timeNow = time.time()
filePath = r"D://Recordings"
days = 30 

for fileName in os.listdir(filePath):
    
    file = os.path.join(filePath, fileName)

    if os.path.isfile(file):
        creationTime = os.path.getctime(file)

        if (timeNow - creationTime) > (30 * 86400):
            os.remove (file)
