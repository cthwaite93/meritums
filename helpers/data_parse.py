import csv
import json
import os
import helpers.data_loader


def __data_parse():
    specialties = helpers.data_loader.loadSpecialties()
    candidates = dict()
    for key in specialties:
        csv_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../data/llista-provisional-merits-cos-" + key + ".csv")
        )
        try:
            with open(csv_path, 'r', newline='') as csv_file:
                reader = csv.reader(csv_file)

                for row in reader:
                    if not row[0].startswith('***'):
                        continue

                    specialty_code = key
                    partial_id = row[0]
                    full_name = row[1]
                    points = float(row[2].replace(',', '.'))
                    tribunal = row[3]
                    priority = int(row[4])
                    candidate_id = partial_id + full_name + tribunal
                    candidate_id = candidate_id.replace(' ', '')

                    # Check if candidate is already in with one attempt or more
                    if candidate_id in candidates:
                        candidates[candidate_id]["attempts"][specialty_code] = {"points": points, "priority": priority}
                    else:
                        candidates[candidate_id] = {
                            "full_name": full_name,
                            "tribunal": tribunal,
                            "attempts": {specialty_code: {"points": points, "priority": priority}}
                        }
        except FileNotFoundError:
            continue

    parsed_barem = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/parsed_llista_provisional.json"))
    with open(parsed_barem, 'w') as f:
        json.dump(candidates, f)


if __name__ == "__main__":
    __data_parse()
