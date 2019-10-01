#This file literally just takes up space
import os 

def dosomething():
    siz =  os.path.getsize("b.py")/1024
    print(f'Size of the file is: {siz} Kilobytes')


dosomething()
