import bisect


class Specialty:
    def __init__(self, specialty_code, specialty_name, section, capacity):
        self._specialty_code = specialty_code
        self._specialty_name = specialty_name
        self._section = section
        self._capacity = capacity
        self.members = []

    @property
    def specialtyCode(self):
        return self._specialty_code

    @property
    def specialtyName(self):
        return self._section

    @property
    def section(self):
        return self._section

    @property
    def capacity(self):
        return self._capacity

    def addCandidate(self, candidate):
        if len(self.members) < self.capacity:
            bisect.insort_left(self.members, candidate)  # If capacity of specialty is not full, just add the candidate
            return True, ""
        else:
            last_member = self.members.pop()  # Get last member of list and remove him of it

            # If candidate has more points than the one of the list
            if last_member.currentAttempt().points < candidate.currentAttempt().points:
                bisect.insort_left(self.members, candidate)
                last_member.removeCurrentAttempt()
                return True, last_member.candidateId

            # If last member of list has more points
            elif last_member.currentAttempt().points > candidate.currentAttempt().points:
                self.members.append(last_member)  # Put last member back in the list
                candidate.removeCurrentAttempt()
                return False

            # If they have equal points I sort by priority
            elif last_member.priority < candidate.priority:
                self.members.append(last_member)  # Don't have the info to sort it in another way
                candidate.removeCurrentAttempt()
                return False

            else:
                self.members.append(candidate)
                last_member.removeCurrentAttempt()
                return True, last_member.candidateId
