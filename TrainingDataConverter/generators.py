from file_manager import FileManager
from out_of_range_error import OutOfRangeError

def generate_training_data(file_path, training_labels, data_window, is_quaternion):
    # Read file data
    file_manager = FileManager(file_path)
    csv_data = FileManager.read_csv(file_path)
    header = csv_data[0]
    just_data = csv_data[1:]
    frames_count = len(just_data)
    number_of_params = len(training_labels)

    # Validation
    if data_window < 1:
        raise OutOfRangeError(f"Data window can't be lower then one")

    if data_window > frames_count:
        raise OutOfRangeError(f"Data window ({data_window}) can't be higher then frames count ({frames_count})")
    
    if number_of_params == 0:
        raise OutOfRangeError(f"Training labels are empty")

    # Set data step
    data_step = 3
    if is_quaternion:
        data_step = 4

    # Read labels
    labels = []
    for i in range(int(len(header[1:]) / data_step)):
        labels.append(header[i * data_step + 1][:-data_step])

    # Search for indices of labels
    labels_indices = []
    for traning_label in training_labels:
        try:
            labels_indices.append(labels.index(traning_label))
        except ValueError:
            raise ValueError(f'Label "{traning_label}" is not in file {file_path}"')

    # Extract training data
    training_data = []
    for i in range(data_step):
        training_data.append([])

    for label_index in labels_indices:
        for i in range(data_step):
            row = []
            row.append(header[label_index * data_step + i + 1])
            for j in range(frames_count):
                row.append(just_data[j][label_index * data_step + i + 1])
            training_data[i].append(row)

    # Slice training data
    sliced_data = []
    for i in range(number_of_params):
        start_index = 0
        end_index = data_window - 1

        while end_index != frames_count:
            for j in range(data_step):
                row = []
                header = training_data[j][i][0]
                sample = training_data[j][i][1:]

                row.append(f"{header} ({start_index},{end_index})")
                row.extend(sample[start_index : end_index + 1])
                sliced_data.append(row)
            start_index += 1
            end_index += 1
    
    # Add file name to header
    for slice in sliced_data:
        slice[0] = f"{file_manager.file_name} - {slice[0]}"

    return sliced_data


def generate_validation_data(training_data, training_procentage):
    data_len = len(training_data)
    training_len = round(data_len * training_procentage)

    return [training_data[:training_len], training_data[training_len:]]