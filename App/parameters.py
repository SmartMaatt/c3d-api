import ezc3d

class ParametersC3D:
    def __init__(self, c3d: ezc3d.c3d, markers_count: int, virtual_markers_count: int):
        self.c3d = c3d

        self.parameters = c3d["parameters"]
        self.trial = self.parameters["TRIAL"]
        self.subjects = self.parameters["SUBJECTS"]
        self.point = self.parameters["POINT"]
        self.analog = self.parameters["ANALOG"]
        self.force_platform = self.parameters["FORCE_PLATFORM"]
        self.event_context = self.parameters["EVENT_CONTEXT"]
        self.event = self.parameters["EVENT"]
        self.manufacturer = self.parameters["MANUFACTURER"]
        self.analysis = self.parameters["ANALYSIS"]
        self.processing = self.parameters["PROCESSING"]

        self.point_info = PointInfoC3D(self.point, markers_count, virtual_markers_count)

class PointInfoC3D:

    # >>> Constructor <<<
    def __init__(self, point_info, markers_count: int, virtual_markers_count: int):
        self.point_info = point_info
        self.markers_count = markers_count
        self.virtual_markers_count = virtual_markers_count

        self.used = point_info["USED"]["value"]
        self.frames = point_info["FRAMES"]["value"]
        self.scale = point_info["SCALE"]["value"]
        self.rate = point_info["RATE"]["value"]
        self.movie_delay = point_info["MOVIE_DELAY"]["value"]
        self.movie_id = point_info["MOVIE_ID"]["value"]
        self.x_screen = point_info["X_SCREEN"]["value"]
        self.y_screen = point_info["Y_SCREEN"]["value"]
        self.units = point_info["UNITS"]["value"]
        self.angle_units = point_info["ANGLE_UNITS"]["value"]
        self.force_units = point_info["FORCE_UNITS"]["value"]
        self.moment_units = point_info["MOMENT_UNITS"]["value"]
        self.power_units = point_info["POWER_UNITS"]["value"]
        self.modeled_marker_units = point_info["MODELED_MARKER_UNITS"]["value"]
        self.labels = point_info["LABELS"]["value"]
        self.descriptions = point_info["DESCRIPTIONS"]["value"]
        self.angles = point_info["ANGLES"]["value"]
        self.forces = point_info["FORCES"]["value"]
        self.moments = point_info["MOMENTS"]["value"]
        self.powers = point_info["POWERS"]["value"]
        self.modeled_markers = point_info["MODELED_MARKERS"]["value"]
        self.type_groups = point_info["TYPE_GROUPS"]["value"]
        self.data_start = point_info["DATA_START"]["value"]

        self.markers = []
        for index in range(self.markers_count):
            self.markers.append(self.labels[index])

        self.virtual_markers = []
        for index in range(self.virtual_markers_count):
            self.virtual_markers.append(self.labels[index + self.markers_count])


    # >>> Indices methods <<<
    def get_indices_by_labels(self, labels: list) -> list:
        indices = []
        for label in labels:
            indices.append(self.labels.index(label))
        return indices

    def get_markers_indices(self) -> list:
        indices = []
        for index in range(self.markers_count):
            indices.append(index)
        return indices
    
    def get_virtual_markers_indices(self) -> list:
        indices = []
        for index in range(self.virtual_markers_count):
            indices.append(index + self.markers_count)
        return indices

    def get_modeled_markers_indices(self) -> list:
        return self.get_indices_by_labels(self.modeled_markers)

    def get_angles_indices(self) -> list:
        return self.get_indices_by_labels(self.angles)
    
    def get_forces_indices(self) -> list:
        return self.get_indices_by_labels(self.forces)
    
    def get_moments_indices(self) -> list:
        return self.get_indices_by_labels(self.moments)
    
    def get_powers_indices(self) -> list:
        return self.get_indices_by_labels(self.powers)
