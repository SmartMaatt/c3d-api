import ezc3d
import sys
from file_management import FileManager
from header import HeaderC3D
from parameters import ParametersC3D
from data import DataC3D

MARKERS_COUNT = 39
VIRTUAL_MARKERS_COUNT = 76

file_path = "C:/Users/mateu/Desktop/Obrobione/Test406.c3d"

# Containers initialization
try:
    file_manager = FileManager(file_path)
    c3d = ezc3d.c3d(file_path)
except OSError as err:
    print(f"{err}")
    sys.exit()

header = HeaderC3D(c3d)
parameters = ParametersC3D(c3d, MARKERS_COUNT, VIRTUAL_MARKERS_COUNT)
point_info = parameters.point_info
data = DataC3D(c3d)
point_data = data.point_data

# Angle indices
angle_labels = point_info.markers
angle_indices = point_info.get_markers_indices()
print(angle_indices)

# Frame count
first_frame = header.points_first_frame
frame_count = header.points_frame_count

# Angle data
angles_data = point_data.get_data_by_indices(angle_indices, frame_count)

# Writing to csv
file_manager.write_csv_with_header(angles_data, angle_labels, first_frame)
