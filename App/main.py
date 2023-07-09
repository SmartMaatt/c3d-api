from data_type import DataType
from scraper import Scraper

def main():
    try:
        scraper = Scraper("C:/Users/mateu/Desktop/Obrobione/Test406.c3d")
        scraper.report_data_to_csv(DataType.POWERS)
    except OSError as err:
        print(f"{err}")
        return

if __name__ == '__main__':
    main()