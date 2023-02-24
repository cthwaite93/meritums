class Attempt:
    def __init__(self, specialty_code, specialty_name, section, priority, points):
        self.specialty_code = specialty_code
        self.specialty_name = specialty_name
        self.section = section
        self.priority = priority
        self.points = points

    def __lt__(self, other):
        return self.priority < other.priority
