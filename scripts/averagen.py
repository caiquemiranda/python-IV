#!/usr/bin/env python3

N, sum, cont = 10, 0, 0
while cont < N:
    number = float(input(''))
    sum = sum + number
    cont += 1
    average = float(sum) / N
    print(f'N = {N}, Sum = {sum}')
    print(f'Average = {average}')
    