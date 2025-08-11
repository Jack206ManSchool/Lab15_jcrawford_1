import matplotlib.pyplot as plt
from pathlib import Path
import csv
import datetime

file_path = Path('OHUR.csv')
file = open('OHUR.csv', 'r')
csv_file = csv.reader(file)

header = next(csv_file)

for i, h in enumerate(header):
    print(f'{i}. {h}')

ohur_list = []
date_list = []

for entry in csv_file:
    date_list.append(entry[0])
    ohur_list.append(entry[1])

plt.style.use("dark_background")
figure, graph = plt.subplots()
plt.title("Ohio Unemployment")
plt.xlabel("Date")
plt.ylabel("Unemp Rate")
graph.plot(date_list, ohur_list, "darkred")
figure.autofmt_xdate()

plt.show()