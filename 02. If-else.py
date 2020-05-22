#!/bin/python3

N = int(input())

if N % 2 == 0:
    if (2 <= N< 6):
        print("Not Weird")
    elif (6<= N <=20):
        print("Weird")
    elif (20<N):
        print("Not Weird")

else:
    print("Weird")

