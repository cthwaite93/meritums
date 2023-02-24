import bisect
import helpers.helpers as helper


if __name__ == '__main__':
    specialties = helper.loadSpecialties()
    candidates = helper.loadCandidates()

    # Candidates that are assigned to a specialty
    assigned = set()

    # While there's candidates to try and insert in a specialty
    while len(candidates) != 0:
        candidate = candidates.pop(0)
        if candidate.candidateId not in assigned:
            if candidate.hasAttempts():
                current_attempt = candidate.currentAttempt()
                accepted, rejected = specialties[current_attempt.specialtyCode].addCandidate(candidate)
                if accepted:
                    assigned.add(candidate)  # Add candidate to the set of assigned candidates
                    # If adding the new candidate has unassigned another one
                    if bool(rejected):
                        # Remove that candidate from assigned candidates
                        assigned.remove(rejected)
                        # Reinstate candidate with left attempts
                        if rejected.hasAttempts():
                            bisect.insort_left(candidates, rejected)
                elif candidate.hasAttempts():
                    bisect.insort_left(candidates, candidate)

    helper.writeCSV(specialties)
