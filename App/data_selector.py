import glob
import re
import pandas as pd

def extract_rows(file_name, start_row, end_row, output_file):
    # Wczytanie pliku csv
    data = pd.read_csv(file_name)

    # Pobranie wierszy z danego zakresu
    data_subset = data.iloc[start_row:end_row]

    # Zapisanie wybranych wierszy do nowego pliku csv
    data_subset.to_csv(output_file, header=False, index=False)

FILE_PATH = r"C:\Repos\Mgr\data\long\410_long.csv"
SAVE_PATH = r"C:\Repos\Mgr\data\hundred_frames\csv\410"

starting_rows = [85, 197, 308, 424, 535, 644, 754, 862, 981, 1091]
row_numbers = 100
correction_offset = 2

alphabet = "abcdefghijklmnopqrstuwxyz"

regex = re.compile(r'\d+')
regex.findall(FILE_PATH)
label = [int(x) for x in regex.findall(FILE_PATH)]
i = 0
for row in starting_rows:
    save_path = f"{SAVE_PATH}/{label[0]}{alphabet[i]}.csv"
    i+=1
    star_row = row - correction_offset
    end_row = row - correction_offset + row_numbers
    extract_rows(FILE_PATH, star_row, end_row, save_path)


# 415 starting_rows = [27, 166, 307, 451, 586, 724, 864, 995, 1138, 1278]
# 414 starting_rows = [51, 171, 288, 415, 538, 659, 776, 889, 1003, 1118] 
# 413 starting_rows = [33, 154, 274, 394, 513, 635, 755, 877, 995, 1114]
# 412 starting_rows = [44, 171, 295, 417, 550, 672, 797, 920, 1045, 1164]
# 411 starting_rows = [51, 183, 313, 449, 585, 718, 846, 974, 1113, 1241]
# 410 starting_rows = [85, 197, 308, 424, 535, 644, 754, 862, 981, 1091]
# 409 starting_rows = [66, 179, 291, 397, 509, 617, 722, 828, 937, 1046]
# 408 starting_rows = [111, 237, 367, 488, 611, 730, 848, 967, 1080, 1205]
# 407 starting_rows = [50, 190, 328, 469, 605, 750, 885, 1019, 1156, 1290]
# 406 starting_rows = [23, 144, 254, 366, 474, 584, 695, 809, 929, 1044]