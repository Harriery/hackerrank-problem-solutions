"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.

Input Format

A single line of input containing the full name, .

Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, .
chris alan => Chris Alan
https://www.hackerrank.com/challenges/capitalize/problem
"""
def solve(user_name):
    return user_name.title()
    
user_name = "chris alan"
result = solve(user_name)

print(result)