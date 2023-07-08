import ezc3d
import csv
from header import HeaderC3D
from parameters import ParametersC3D
from data import DataC3D

MARKERS_COUNT = 39
VIRTUAL_MARKERS_COUNT = 76

def read_c3d_file(file_path):
    # Containers initialization
    c3d = ezc3d.c3d(file_path)
    header = HeaderC3D(c3d)
    parameters = ParametersC3D(c3d, MARKERS_COUNT, VIRTUAL_MARKERS_COUNT)
    point_info = parameters.point_info
    data = DataC3D(c3d)
    point_data = data.point_data

    # Angle indices
    angle_indices = point_info.get_angles_indices()
    print(angle_indices)

    # Frame count
    first_frame = header.points_first_frame
    frame_count = header.points_frame_count

    # Angle data
    angles_data = point_data.get_data_by_indices(angle_indices, frame_count)
    
    with open("C:/Users/mateu/Desktop/Obrobione/dupa.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        frame_index = first_frame

        # Header
        header = ['Index']
        for label in point_info.angles:
            header.append(f'{label} [X]')
            header.append(f'{label} [Y]')
            header.append(f'{label} [Z]')
        writer.writerow(header)

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