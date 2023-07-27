import os
import shutil
import random

DIR_PATH = r"C:\Repos\Mgr\data\hundred_frames\csv_one_line\407"
MOVE_PATH = r"C:\Repos\Mgr\data\hundred_frames\csv_one_line\test"

def move_files_randomly(src_folder, dst_folder, num_files):
    # Wczytanie listy plików
    files = os.listdir(src_folder)

    # Sprawdzenie, czy są co najmniej 4 pliki do przeniesienia
    if len(files) < num_files:
        print(f"Znaleziono tylko {len(files)} plików. Zmniejsz liczbę plików do przeniesienia.")
        return

    # Losowe wybranie plików do przeniesienia
    selected_files = random.sample(files, num_files)

    # Przeniesienie plików
    for file_name in selected_files:
        src_file_path = os.path.join(src_folder, file_name)
        dst_file_path = os.path.join(dst_folder, file_name)
        shutil.move(src_file_path, dst_file_path)

    print(f"Przeniesiono {num_files} plików.")

# Użycie funkcji
move_files_randomly(DIR_PATH, MOVE_PATH, 4)