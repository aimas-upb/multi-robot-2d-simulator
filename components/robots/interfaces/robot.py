from components.robots.models.pose import Pose

class Robot:

    def __init__(self, geometry, kinematics, sensors):
        self.geometry = geometry
        self.kinematics = kinematics
        self.sensors = sensors
        self.pose = None

    def get_pose(self):
        return self.pose

    def move(self):
        pass

    def update(self, unit_time):
        pass