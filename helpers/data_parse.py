import json
import os


def __data_parse():
    barem_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/barem_provisional.json"))
    output_list = []
    candidates = dict()
    with open(barem_path, 'r') as f:
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

    parsed_barem = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/parsed_barem_provisional.json"))
    with open(parsed_barem, 'w') as f:
        json.dump(output_list, f)


if __name__ == "__main__":
    __data_parse()
