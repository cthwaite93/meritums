class Attempt:
    def __init__(self, specialty_code, points, priority):
        self._specialty_code = specialty_code
        self._points = points
        self._priority = priority

    @property
    def specialtyCode(self):
        return self._specialty_code

    @property
    def priority(self):
        return self._priority

    @property
    def points(self):
        return self._points

    def __lt__(self, other):
        return self.priority < other.priority
