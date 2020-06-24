# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total = 0
    with open(filename, 'rt') as file:
        next(file)
        rows = csv.reader(file)
        for row in rows:
            total += int(row[1]) * float(row[2])
        return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'


cost = portfolio_cost(filename)
print(f"Total cost {cost:0.2f}")