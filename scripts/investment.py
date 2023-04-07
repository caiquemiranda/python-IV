#!/usr/bin/env python3

amount = float(input('Enter amount: '))
inrate = float(input('Enter interest rate: '))
period = int(input('Enter period: '))

value = 0
year = 1

while year <= period:
    value = amount + (inrate * amount)
    print(f'Year {year} Rs. {value}%.2f')
    amount = value
    year = year + 1
    