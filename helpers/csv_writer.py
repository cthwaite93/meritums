import os
import csv


def __writeCSVRow(writer, data):
    # Fix for catalan locale where decimal point is a comma
    attempt = data.currentAttempt()
    formatted_float = "{:.4f}".format(attempt.points).replace(".", ",")
    writer.writerow([data.fullName, formatted_float, data.tribunal, attempt.priority])


def __writeCSVRows(csv_file, specialty, reject):
    writer = csv.writer(csv_file)
    writer.writerow(["Nom", "Barem", "Tribunal", "Prioritat"])
    if reject:
        for reject in specialty.rejects:
            __writeCSVRow(writer, reject)
    else:
        for member in specialty.members:
            __writeCSVRow(writer, member)


def writeCSV(dictionary):
    for key in dictionary:
        base_folder = "lists/"
        folder_name = dictionary[key].specialtyCode + "_" + str(dictionary[key].specialtyName)
        folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../" + base_folder + folder_name))
        os.makedirs(folder_path)
        with open(folder_path + "/accepted.csv", "w", newline="") as csv_file:
            __writeCSVRows(csv_file, dictionary[key], False)
        with open(folder_path + "/rejected.csv", "w", newline="") as csv_file:
            __writeCSVRows(csv_file, dictionary[key], True)