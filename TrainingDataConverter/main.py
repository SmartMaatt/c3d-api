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
    output_labels = []

    try:
        for csv_path in csv_paths:
            print(f"Reading {csv_path}")
            data, labels = generate_training_data(csv_path, TRAINING_LABELS, DATA_WINDOW, IS_QUATERNION)
            output_data.append(data)
            output_labels.append(labels)
        
        print("Sorting training set")
        training_data = []
        for training_file in output_data:
            training_data.extend(training_file)

        print("Sorting labels data")
        labels_data = []
        for label_file in output_labels:
            labels_data.extend(label_file)

        print("Saving sets to csv")
        FileManager.write_csv(training_data, f"{DIR_PATH}/training_data.csv")
        FileManager.write_csv(labels_data, f"{DIR_PATH}/labels_data.csv")
    except OutOfRangeError as err:
        print(f"ERROR: {err}")
    except ValueError as err:
        print(f"ERROR: {err}")


if __name__ == "__main__":
    main()