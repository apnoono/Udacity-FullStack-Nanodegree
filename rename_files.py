import os
import re

def rename_files():
    file_list = os.listdir(r"C:/Users/andrew.p.noonoo/Desktop/TMP/udacity_fullstack_nano/secret")
    os.chdir(r"C:/Users/andrew.p.noonoo/Desktop/TMP/udacity_fullstack_nano/secret")

    for file_name in file_list:
        print("old: " + file_name)
        print("new: " + re.sub('\d+', '', file_name))
        #.rename() must be called twice b/c it's not a mutative method
        os.rename(file_name, re.sub('\d+', '', file_name))

rename_files()
