# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import logging

import requests
import json
import csv
import logging


def generate_most_volatile_stock():
    companies = ['GOOGL', 'NFLX', 'AAPL', 'NFLX', 'FB']

    print("start fetching stocks...")
    stocks = [json.loads(requests.get(get_url(i)).text.replace('}', ',"stock_symbol":"' + i + '"}'))
              for i in companies]
    print("stock list", stocks)
    print("end fetching stocks..")

    # get percentage change list
    dp = [abs(x['dp']) for x in stocks]

    # get most volatile json obj
    filtered_stock = [x for x in stocks if abs(x['dp']) == max(dp)][0]

    filtered_stock_dict = get_most_volatile_stock_dict(filtered_stock)

    generate_csv_file(filtered_stock, filtered_stock_dict)


def get_most_volatile_stock_dict(filtered_stock):
    return {'stock_symbol': filtered_stock['stock_symbol'], 'percentage_change': filtered_stock['dp'],
            'current_price': filtered_stock['c'], 'last_close_price': filtered_stock['pc']}


def generate_csv_file(filtered_stock, filtered_stock_dict):
    with open('most_volatile_stock.csv', 'w') as data_file:
        csv_writer = csv.writer(data_file)
        header = dict(filtered_stock_dict).keys()
        print("start cvs creation")
        csv_writer.writerow(header)
        csv_writer.writerow(dict(filtered_stock_dict).values())
        print(filtered_stock)
        data_file.close()
        print("end cvs creation")


def get_url(symbol):
    # add your key
    api_key = 'sandbox_c9i39taad3i9bpe2219g'
    return f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate_most_volatile_stock()
