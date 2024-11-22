""" 
Created By SORENSHAMLOU

Create At : 2023/2/16

Version : 0.0.1

"""
__version__ = "1.5.0"
__author__ = "SorenShamlou"
__date__ = "2023/2/16"
__copyright__ = "Copyright 2023, SorenShamlou"
__credits__ = ["SorenShamlou"]
__license__ = "GPL"

from os import system
from time import sleep
from sys import stdout
from string import (
    ascii_letters,
    digits
)

chars = list(" " + ascii_letters + digits + "!@#$%^&*()_-=+`~")

def show_text(text, index=0, temp="",sleep_value=0.04):
    if index == len(text):
        print(text)
        return 0
    for char in chars:
        stdout.write(f"{temp}{char}")
        stdout.flush()
        sleep(sleep_value)
        system("cls")
        if text[index] == char: break
    return show_text(text,index+1,temp+char)


show_text("Soren Shamlou")