import random
import os

myFile = open("inputdata", "w+")

for i in range(0,10):
    num= random.randint(0,1000)
    myFile.write(f"{i}, {num}\n")
myFile.close()
