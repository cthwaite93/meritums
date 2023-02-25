import bisect
import helpers.csv_writer
import helpers.data_loader


if __name__ == '__main__':
    specialties = helpers.data_loader.loadSpecialties()
    candidates = helpers.data_loader.loadCandidates()
    print(len(candidates))

    # While there's candidates to try and insert in a specialty
    while len(candidates) != 0:
        # Get the candidate on the top of the list and remove them from it
        candidate = candidates.pop(0)

        # Get the candidate's top priority attempt
        current_attempt = candidate.currentAttempt()

        # Try and add candidate to the attempt's chosen specialty
        accepted, rejected = specialties[current_attempt.specialtyCode].addCandidate(candidate)

        # Candidate has been accepted as member of the speciality they attempted to enter
        if accepted:
            # If adding the new candidate has unassigned another one and that reject still has attempts left
            if bool(rejected) and rejected.hasAttempts():
                bisect.insort_left(candidates, rejected)

        # If candidate has been rejected and still has attempts put them back in the list
        elif candidate.hasAttempts():
            bisect.insort_left(candidates, candidate)

    helpers.csv_writer.writeCSV(specialties)
