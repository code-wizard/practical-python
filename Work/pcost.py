# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row_no, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                n_shares = int(record['shares'])
                price = float(record['price'])
                total_cost += n_shares * price
            except ValueError:
                print(f'Row {row_no}: Bad row: {row}')

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

cost = portfolio_cost(filename)
print('Total cost:', cost)