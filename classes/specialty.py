class Specialty:
    def __init__(self, specialty_code, specialty_name, section, capacity):
        self.specialty_code = specialty_code
        self.specialty_name = specialty_name
        self.section = section
        self.capacity = capacity
        self.members = []
        self.wait_list = []

    def addCandidate(self, candidate):
        if len(self.members) < self.capacity:
            self.members.append(candidate)  # If capacity of specialty is not full, just add the candidate
            return True, ""
        else:
            last_member = self.members.pop()  # Get last member of list and remove him of it
            if last_member.points < candidate.points:  # If candidate has more points than the one of the list
                self.members.append(candidate)
                # In the specialty list, the order is by points in descent
                self.members = sorted(self.members, key=lambda x: -x.points)
                return True, last_member.candidate_id
            elif last_member.points > candidate.points:  # If last member of list has more points
                self.members.append(last_member)  # Put last member back in the list
                return False, ""
            elif last_member.priority < candidate.priority:  # If they have equal points I sort by priority
                self.members.append(last_member)  # Don't have the info to sort it in another way
                return False, ""
            else:
                self.members.append(candidate)
                return True, last_member.candidate_id
