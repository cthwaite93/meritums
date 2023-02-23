class Candidate:
    def __init__(self, specialty_code, specialty_name, section, full_name, points, tribunal, priority):
        self.specialty_code = specialty_code
        self.specialty_name = specialty_name
        self.section = section
        self.full_name = full_name
        self.points = points
        self.tribunal = tribunal
        self.priority = priority
        # This is done because there are some people who are different with the exact same full name, so we can identify
        # a candidate that might have different entries with different priorities. There can never be two candidates
        # with the same candidate_id and priority
        self.candidate_id = self.full_name + self.tribunal

    def __lt__(self, other):  # Sorting function that orders priority by ascent and points by descent
        if self.priority < other.priority:
            return True
        elif self.priority == other.priority:
            return self.points > other.points
        return False
