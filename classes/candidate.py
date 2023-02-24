import bisect
from attempt import Attempt


class Candidate:
    def __init__(self, specialty_code, full_name, points, tribunal, priority):
        # This is done because there are some people who are different with the exact same full name, so we can identify
        # a candidate that might have different entries with different priorities. There can never be two candidates
        # with the same candidate_id and priority
        self._candidate_id = full_name + tribunal
        self._full_name = full_name
        self._tribunal = tribunal
        self._attempts = [Attempt(specialty_code, points, priority)]

    @property
    def candidateId(self):
        return self._candidate_id

    @property
    def fullName(self):
        return self._full_name

    @property
    def tribunal(self):
        return self._tribunal

    @property
    def __attempts(self):
        return self._attempts

    def addAttempt(self, specialty_code, points, priority):
        bisect.insort_left(self.__attempts, Attempt(specialty_code, points, priority))

    def currentAttempt(self):
        return self.__attempts[0]

    def removeCurrentAttempt(self):
        self.__attempts.pop(0)

    def __lt__(self, other):  # Sorting function that orders points by descent
        return self.currentAttempt().points > other.currentAttempt().points
