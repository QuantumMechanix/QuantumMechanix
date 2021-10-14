#-*- coding:utf-8 -*-
Weight=float(input('Please write your weight in Kilogram'))
Height=float(input('Please write your height in Meter'))
BMI= float (Weight / (Height * Height))
if BMI < 18.5:
    print('You\'re underweight.')
if 18.5 <= BMI < 25:
    print('You\'re healthy.')
if 25 <= BMI < 30:
    print('You\'re overweight.')
if BMI >= 30:
    print('Go get some cardio, you f**king moron.')