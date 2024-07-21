#!/usr/bin/env python
# coding: utf-8

#BMI = (weight in pounds x 703) / (height in inches x height in inches)


name = input("enter your name: ")

weight = int(input("enter weight in pounds: "))

height = int(input("enter height in inches: "))

BMI = (weight * 703) / (height * height)

print(BMI)

if BMI>0:
    if(BMI<18.5):
        print("	Underweight")
    elif(BMI<=24.9):
        print("	Normal weight")
    elif(BMI<=29.9):
        print("	overweight")
    elif(BMI<=34.9):
        print("	Obese")
    elif(BMI<=39.9):
        print("	Severely Obese")
    elif(BMI>=40):
        print("	Morbidly Obese")
    else:
        print("enter valid input")
        






