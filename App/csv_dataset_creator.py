import glob
import csv
import pandas as pd

DIR_PATH = r"C:\Repos\Mgr\data\hundred_frames\csv_test"
SAVE_PATH = r"C:\Repos\Mgr\data\hundred_frames\csv_test.csv"

csv_data = glob.glob(DIR_PATH + "\*.csv")

# Lista na pierwsze wiersze każdego pliku
first_rows = []

for csv_path in csv_data:
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        first_row = next(reader)  # Odczytuje pierwszy wiersz pliku
        first_rows.append(first_row)

# Zapisuje pierwsze wiersze do nowego pliku csv
with open(SAVE_PATH, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(first_rows)  # Zapisuje listę wierszy do pliku