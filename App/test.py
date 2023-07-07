import numpy as np
import ezc3d

def read_c3d_file(file_path):
    # Otwórz plik C3D
    c3d = ezc3d.c3d(file_path)

    # Wczytaj etykiety kątów
    angle_labels = c3d['parameters']['POINT']['ANGLES']['value']

    # Dla każdej etykiety, wypisz odpowiadające jej dane
    for label in angle_labels:
        angle_data = c3d['data']['points'][label]
        print(f'Dane dla kąta {label}: {angle_data}')

    # # Pobierz listę nazw kanałów danych analogowych
    # analog_labels = c3d['parameters']['POINT']['ANGLES']['value']

    # # Sprawdź, czy istnieją jakiekolwiek dane analogowe
    # if not analog_labels:
    #     print(f"Brak danych analogowych w pliku {file_path}")
    #     return None

    # # Pobierz dane analogowe
    # analog_data = c3d['data']['analogs']

    # # Zwróć dane analogowe jako słownik, gdzie klucze to nazwy kanałów, a wartości to dane z tych kanałów
    # return {label: analog_data[i] for i, label in enumerate(analog_labels)}


file_path = "C:/Users/mateu/Desktop/Obrobione/Test406.c3d"
read_c3d_file(file_path)

# if data is not None:
#     for label, values in data.items():
#         print(f"Kanał: {label}, wartości: {values}")