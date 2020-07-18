# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    portfolio = list()
    with open(filename, 'rt') as f:
        rows = csv.reader(filename)
        headers = next(rows)
        for row in rows:
            portfolio.append(dict(name=row[0], shares=int(row[1]), price=float(row[2])))
        return portfolio


def read_prices(filename):
    prices = dict()
    with open(filename, 'r') as f:
        rows = csv.reader(filename)
        headers = rows.next()
        for row in rows:
            try:
                prices[row[0]] = row[1]
            except:
                print("Bad rows")
        return prices


def make_report(stock, prices):
    reports = []
    for s in stock:
        reports.append((s["name"], s["shares"], s["price"], prices[s["name"]]-s["price"]))
    return reports


portfolio = read_portfolio('Work/Data/portfolio.csv')
prices = read_prices('Work/Data/prices.csv')

# Generate the report data

report = make_report(portfolio, prices)
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)
