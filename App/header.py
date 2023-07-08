import ezc3d


class HeaderC3D:
    def __init__(self, c3d: ezc3d.c3d):
        self.c3d = c3d

        self.header = c3d["header"]
        self.points = self.header["points"]
        self.analogs = self.header["analogs"]
        self.events = self.header["events"]

        self.points_size = self.points["size"]
        self.points_frame_rate = self.points["frame_rate"]
        self.points_first_frame = self.points["first_frame"]
        self.points_last_frame = self.points["last_frame"]
        self.points_frame_count = self.points_last_frame - self.points_first_frame + 1
