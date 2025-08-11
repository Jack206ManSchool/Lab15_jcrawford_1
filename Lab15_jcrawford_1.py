'''
Program Name: Lab15_jackcrawford_1
Author Name: Jack Crawford
Purpose: A program that displays unemployment numbers.
Date: 8/11/25
'''

# Imports
import matplotlib.pyplot as plt
from pathlib import Path
import csv
import datetime

# Get File
file_path = Path('OHUR.csv')
file = open('OHUR.csv', 'r')
csv_file = csv.reader(file)

# Get and Print header
header = next(csv_file)
for i, h in enumerate(header):
    print(f'{i}. {h}')

# Create Lists
ohur_list = []
date_list = []
for entry in csv_file:
    date_list.append(datetime.datetime.strptime(entry[0], "%Y-%m-%d"))
    ohur_list.append(float(entry[1]))

# Create graph, apply titles, print lists onto it
plt.style.use("dark_background")
figure, graph = plt.subplots()
plt.title("Ohio Unemployment", fontsize=24)
plt.xlabel("Date", fontsize=16)
plt.ylabel("Unemp Rate", fontsize=16)
graph.plot(date_list, ohur_list, "darkred")
figure.autofmt_xdate()
plt.gca().xaxis.set_remove_overlapping_locs(True)
plt.show()