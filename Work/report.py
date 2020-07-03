# report.py
#
# Exercise 2.4
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

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as file:
        next(file)
        rows = csv.reader(file)
        for row in rows:
            t = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(t)
    return portfolio

def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        for r in rows:
            if len(r) == 2:
                prices[r[0]] = float(r[1])
    return prices

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'


cost = portfolio_cost(filename)
print(f"Total cost {cost:0.2f}")