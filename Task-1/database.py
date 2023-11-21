import csv
import pandas as pd


def data():
    fields = ['NAME',
              'PAYMENT TYPE',
              'PAYMENT MODE',
              'PAYMENT AMOUNT',
              'PAYMENT DATE',
              'REFERENCE NUMBER']

    filename = "payment_record.csv"

    with open(filename, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()


def update(list):
    with open("payment_record.csv", 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(list)


if __name__ == "__main__":
    data()
