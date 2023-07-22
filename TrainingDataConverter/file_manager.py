import os
import csv


class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.directory = os.path.dirname(file_path)
        self.file_full = os.path.basename(file_path)
        self.file_name, self.file_ext = os.path.splitext(self.file_full)
        self.file_name = self.file_name[:self.file_name.find('_')]
        self._validate_file_path()

    def _validate_file_path(self):
        if self.file_ext != ".csv":
            raise OSError(
                f"Required file must have the extension .csv not {self.file_ext}"
            )

    @staticmethod
    def read_csv(file_path: str) -> list:
        result_array = []
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                result_array.append(row)

        return result_array

    @staticmethod
    def write_csv(data, file_path):
        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerow(row)
        print(f"Succesfully saved data to {file_path}")
