import sys
import imppkg.harmony_mean import harmoic_mean
from termcolor import cprint

def main():
    result =0.0
    try:
        nums =[float(num) for num in sys.argv[1:]]
    except ValueError:
        nums = []

    try:
        result = harmoic_mean(nums)
    except ZeroDivisionError:
        pass

    cprint(result,"red","on_cyan",attrs=["bold"])