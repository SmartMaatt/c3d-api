from file_manager import FileManager
from generators import generate_training_data, generate_validation_data
from out_of_range_error import OutOfRangeError
import glob


# Public parameters
DIR_PATH = r"C:\Users\Szkolenie\Desktop\Obrobione\quaternions"
TRAINING_LABELS = ["LHipAngles"]
DATA_WINDOW = 100
IS_QUATERNION = True
TRAINING_DATA_PROCENTAGE = 0.8


def main():
    if TRAINING_DATA_PROCENTAGE > 1 or TRAINING_DATA_PROCENTAGE < 0:
        print(f"ERROR: Training data procentage needs to be in range <0,1>")
        return

    csv_paths = glob.glob(DIR_PATH + "\*.csv")
    output_data = []

    try:
        for csv_path in csv_paths:
            print(f"Reading {csv_path}")
            output_data.append(generate_training_data(csv_path, TRAINING_LABELS, DATA_WINDOW, IS_QUATERNION))
        
        print("Splitting data set for training and validation")
        training_data_unsorted, validation_data_unsorted = generate_validation_data(output_data, TRAINING_DATA_PROCENTAGE)
        
        print("Sorting training set")
        training_data = []
        for training_file in training_data_unsorted:
            training_data.extend(training_file)

        print("Sorting validation set")
        validation_data = []
        for validation_file in validation_data_unsorted:
            validation_data.extend(validation_file)

        print("Saving sets to csv")
        FileManager.write_csv(training_data, f"{DIR_PATH}/training_data.csv")
        FileManager.write_csv(validation_data, f"{DIR_PATH}/validation.data.csv")
    except OutOfRangeError as err:
        print(f"ERROR: {err}")
    except ValueError as err:
        print(f"ERROR: {err}")


if __name__ == "__main__":
    main()