class Attempt:
    def __init__(self, specialty_code, priority, points):
        self.specialty_code = specialty_code
        self.priority = priority
        self.points = points
        self.attempted = False

    def __lt__(self, other):
        return self.priority < other.priority

    def hasBeenAttempted(self):
        return self.attempted

    def tried(self):
        self.attempted = True
