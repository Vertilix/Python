from ast import Sub
from re import sub
import random

temp = {
    "0":[0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    "1": [0, 1, 2, 2, 1, 1, 0, 0, 0, 1, 0, 2, 0, 1, 0, 2, 1, 1, 1, 0],
    "2": [0, 1, 0, 2, 1, 1, 0, 3, 0, 1, 3, 0, 0, 1, 0, 3, 1, 1, 1, 0],
    "3": [2, 1, 2, 2, 1, 1, 0, 0, 0, 1, 0, 2, 0, 1, 2, 2, 1, 1, 1, 0],
    "4": [0, 1, 2, 2, 1, 1, 0, 2, 0, 1, 10, 2, 0, 2, 2, 0, 1, 1, 1, 0],
    "5": [4, 2, 2, 2, 1, 1, 0, 0, 0, 1, 0, 0, 0, 2, 2, 0, 1, 1, 1, 0]}

print(sum(temp[("0","1", "2", "3", "4", "5")[random.randint(0,5)]]))    

#Program picks a random array and sums them together