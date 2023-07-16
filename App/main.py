import glob
from c3d_exception import C3DError
from data_type import DataType
from scraper import Scraper

def main():
    dir_path = r"C:\Users\Szkolenie\Desktop\Obrobione"
    c3d_data = glob.glob(dir_path + "\*.c3d")
    
    for c3d_path in c3d_data:
        try:
            scraper = Scraper(c3d_path)
            scraper.report_data_to_csv(DataType.ANGLES)
        except OSError as err:
            print(f"{c3d_path}: {err}")
        except C3DError as err:
            print(f"{c3d_path}: {err}")

if __name__ == '__main__':
    main()