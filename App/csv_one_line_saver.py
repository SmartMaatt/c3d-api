import csv
import re
import glob
import pandas as pd
from pathlib import Path

DIR_PATH = r"C:\Repos\Mgr\data\hundred_frames\csv\415"
#FILE_PATH = r"C:\Repos\Mgr\data\hundred_frames\csv\407a.csv"
SAVE_PATH = r"C:\Repos\Mgr\data\hundred_frames\csv_one_line\415"

csv_data = glob.glob(DIR_PATH + "\*.csv")
    
for csv_path in csv_data:
    try:
        #csv_path = FILE_PATH
        # Pobranie etykiety z nazwy pliku
        regex = re.compile(r'\d+')
        regex.findall(csv_path)
        label = [int(x) for x in regex.findall(csv_path)]

        # Odczytanie danych z pliku csv
        with open(csv_path, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)

        # Sklejenie wszystkich wierszy
        flattened_data = [item for sublist in data for item in sublist]
        flattened_data.insert(0, label[0])

        # Zapisanie sklejonych danych do nowego pliku csv
        #print(Path(csv_path).stem)
        save_path = f"{SAVE_PATH}/{Path(csv_path).stem}_one_line.csv"
        with open(save_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(flattened_data)

    except OSError as err:
        print(f"{csv_path}: {err}")