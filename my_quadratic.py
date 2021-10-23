# -*- coding: utf-8 -*-

import math
import time

def my_quadratic(a,b,c):
    bigx = (-b + math.sqrt(b*b-4*a*c))/(2*a)
    smallx = (-b - math.sqrt(b*b-4*a*c))/(2*a)
    return smallx, bigx

print (my_quadratic(2,3,1))

time.sleep(30)