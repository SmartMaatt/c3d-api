import ezc3d
import csv

def read_c3d_file(file_path):
    c3d = ezc3d.c3d(file_path)

    labels = c3d['parameters']['POINT']['LABELS']['value']
    angle_labels = c3d['parameters']['POINT']['ANGLES']['value']
    angle_indecies = []

    for angle_label in angle_labels:
        angle_indecies.append(labels.index(angle_label))

    print(angle_indecies)

    # Frame count
    header_points = c3d['header']['points']
    first_frame = header_points['first_frame'] 
    last_frame = header_points['last_frame']
    frame_count = last_frame - first_frame + 1

    data = c3d['data']['points']
    angles_data = []

    for frame in range(frame_count):
        angles_data.append([])
        for index in angle_indecies:
            angles_data[frame].append([data[0][index][frame], data[1][index][frame], data[2][index][frame]])

    with open("C:/Users/mateu/Desktop/Obrobione/dupa.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        frame_index = first_frame

        for frame in angles_data:
            angles = []
            angles.append(frame_index)

            for angle in frame:
                angles.append(angle[0])
                angles.append(angle[1])
                angles.append(angle[2])
            writer.writerow(angles)
            frame_index += 1

    


file_path = "C:/Users/mateu/Desktop/Obrobione/Test406.c3d"
read_c3d_file(file_path)