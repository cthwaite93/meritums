import json


def data_parse():
    output_list = []
    candidates = dict()
    with open('../data/barem_provisional.json') as f:
        data = json.load(f)
        for obj in data["data"]:

            # Fix for shitty data inconsistency where EC and ECO codes are the same specialty
            if obj["0"] == "EC":
                obj["0"] = "ECO"

            specialty_code = obj["0"]
            full_name = obj["3"]
            points = obj["4"]
            priority = obj["5"]
            tribunal = obj["6"]
            candidate_id = full_name + tribunal

            # Check if candidate is already in with one attempt or more
            if candidate_id in candidates:
                candidates[candidate_id]["attempts"].append(
                    {"code": specialty_code, "points": points, "priority": priority}
                )
            else:
                candidates[candidate_id] = {
                    "full_name": full_name,
                    "tribunal": tribunal,
                    "attempts": [{"code": specialty_code, "points": points, "priority": priority}]
                }

    for key in candidates:
        output_list.append(candidates[key])

    with open('../data/parsed_barem_provisional.json', 'w') as f:
        json.dump(output_list, f)


if __name__ == '__main__':
    data_parse()
