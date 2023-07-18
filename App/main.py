import glob
from c3d_exception import C3DError
from data_type import DataType
from scraper import Scraper


DIR_PATH = r"C:\Users\Szkolenie\Desktop\Obrobione"
DATA_TYPE = DataType.ANGLES
INCLUDE_HEADER = True


def main():
    c3d_data = glob.glob(DIR_PATH + "\*.c3d")
    
    for c3d_path in c3d_data:
        try:
            scraper = Scraper(c3d_path)
            scraper.report_data_to_csv(DATA_TYPE, INCLUDE_HEADER)
        except OSError as err:
            print(f"{c3d_path}: {err}")
        except C3DError as err:
            print(f"{c3d_path}: {err}")

if __name__ == '__main__':
    main()