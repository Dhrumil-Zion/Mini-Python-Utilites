import filecmp
import os

files = os.listdir()
filename = '2.pdf'
for val in files:
    if val != filename:
        if filecmp.cmp(filename, val):
            os.remove(val)
            print("removed")
        else:
            print("no needed")
