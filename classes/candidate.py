import bisect
from attempt import Attempt


class Candidate:
    def __init__(self, specialty_code, specialty_name, section, full_name, points, tribunal, priority):
        # This is done because there are some people who are different with the exact same full name, so we can identify
        # a candidate that might have different entries with different priorities. There can never be two candidates
        # with the same candidate_id and priority
        self.candidate_id = full_name + tribunal
        self.full_name = full_name
        self.tribunal = tribunal
        self.attempts = [Attempt(specialty_code, specialty_name, section, points, priority)]

    def __lt__(self, other):  # Sorting function that orders points by descent
        return self.currentAttempt().points > other.currentAttempt().points

    def addAttempt(self, specialty_code, specialty_name, section, points, priority):
        bisect.insort_left(self.attempts, Attempt(specialty_code, specialty_name, section, points, priority))

    def currentAttempt(self):
        return self.attempts[0]

    def removeCurrentAttempt(self):
        self.attempts.pop(0)
