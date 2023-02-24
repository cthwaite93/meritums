import csv
import bisect
import json
from classes.specialty import Specialty
from classes.candidate import Candidate


def loadSpecialties():
    return {
        "ALL": Specialty("ALL", "Audició i llenguatge", "Cos de mestres", 101),
        "EES": Specialty("EES", "Pedagogia terapèutica", "Cos de mestres", 857),
        "INF": Specialty("INF", "Educació infantil", "Cos de mestres", 1312),
        "PAN": Specialty("PAN", "Llengua estrangera - anglès", "Cos de mestres", 482),
        "PEF": Specialty("PEF", "Educació física", "Cos de mestres", 402),
        "PFR": Specialty("PFR", "Llengua estrangera - francès", "Cos de mestres", 8),
        "PMU": Specialty("PMU", "Música", "Cos de mestres", 298),
        "PRI": Specialty("PRI", "Educació primària", "Cos de mestres", 2223),
        "501": Specialty("501", "Administració d'empreses", "Cos de professors d'ensenyament secundari", 80),
        "502": Specialty("502", "Anàlisi i química industrial", "Cos de professors d'ensenyament secundari", 25),
        "503": Specialty("503", "Assessoria i processos d'imatge personal",
                         "Cos de professors d'ensenyament secundari", 24),
        "504": Specialty("504", "Construccions civils i edificacions", "Cos de professors d'ensenyament secundari", 5),
        "505": Specialty("505", "Formació i orientació laboral", "Cos de professors d'ensenyament secundari", 113),
        "506": Specialty("506", "Hoteleria i turisme", "Cos de professors d'ensenyament secundari", 27),
        "507": Specialty("507", "Informàtica", "Cos de professors d'ensenyament secundari", 129),
        "508": Specialty("508", "Intervenció sociocomunitària", "Cos de professors d'ensenyament secundari", 91),
        "509": Specialty("509", "Navegació i instal·lacions marines", "Cos de professors d'ensenyament secundari", 5),
        "510": Specialty("510", "Organització i gestió comercial", "Cos de professors d'ensenyament secundari", 55),
        "511": Specialty("511", "Organització i processos de manteniment vehicles",
                         "Cos de professors d'ensenyament secundari", 26),
        "512": Specialty("512", "Organització i projectes de fabricació mecànica",
                         "Cos de professors d'ensenyament secundari", 28),
        "513": Specialty("513", "Organització i projectes de sistemes energètics",
                         "Cos de professors d'ensenyament secundari", 8),
        "514": Specialty("514", "Processos de cultiu aqüícola", "Cos de professors d'ensenyament secundari", 1),
        "515": Specialty("515", "Processos de producció agrària", "Cos de professors d'ensenyament secundari", 10),
        "516": Specialty("516", "Processos en la indústria alimentària",
                         "Cos de professors d'ensenyament secundari", 8),
        "517": Specialty("517", "Processos diagnòstics clínics i productes ortoprotètics",
                         "Cos de professors d'ensenyament secundari", 20),
        "518": Specialty("518", "Processos sanitaris", "Cos de professors d'ensenyament secundari", 46),
        "519": Specialty("519", "Processos i mitjans de comunicació", "Cos de professors d'ensenyament secundari", 12),
        "520": Specialty("520", "Processos i productes de tèxtil, confecció i pell",
                         "Cos de professors d'ensenyament secundari", 4),
        "522": Specialty("522", "Processos i productes d'arts gràfiques",
                         "Cos de professors d'ensenyament secundari", 5),
        "523": Specialty("523", "Processos i productes de fusta i moble",
                         "Cos de professors d'ensenyament secundari", 4),
        "524": Specialty("524", "Sistemes electrònics", "Cos de professors d'ensenyament secundari", 12),
        "525": Specialty("525", "Sistemes electrotècnics i automàtics",
                         "Cos de professors d'ensenyament secundari", 24),
        "AL": Specialty("AL", "Alemany", "Cos de professors d'ensenyament secundari", 14),
        "AN": Specialty("AN", "Anglès", "Cos de professors d'ensenyament secundari", 621),
        "AR": Specialty("AR", "Aranès", "Cos de professors d'ensenyament secundari", 1),
        "CN": Specialty("CN", "Biologia i geologia", "Cos de professors d'ensenyament secundari", 368),
        "DI": Specialty("DI", "Dibuix", "Cos de professors d'ensenyament secundari", 278),
        "ECO": Specialty("ECO", "Economia", "Cos de professors d'ensenyament secundari", 96),
        "EF": Specialty("EF", "Educació física", "Cos de professors d'ensenyament secundari", 326),
        "FI": Specialty("FI", "Filosofia", "Cos de professors d'ensenyament secundari", 130),
        "FQ": Specialty("FQ", "Física i química", "Cos de professors d'ensenyament secundari", 270),
        "FR": Specialty("FR", "Francès", "Cos de professors d'ensenyament secundari", 103),
        "GE": Specialty("GE", "Geografia i història", "Cos de professors d'ensenyament secundari", 604),
        "GR": Specialty("GR", "Grec", "Cos de professors d'ensenyament secundari", 20),
        "IT": Specialty("IT", "Italià", "Cos de professors d'ensenyament secundari", 1),
        "LA": Specialty("LA", "Llatí", "Cos de professors d'ensenyament secundari", 64),
        "LC": Specialty("LC", "Llengua catalana i literatura", "Cos de professors d'ensenyament secundari", 520),
        "LE": Specialty("LE", "Llengua castellana i literatura", "Cos de professors d'ensenyament secundari", 528),
        "MA": Specialty("MA", "Matemàtiques", "Cos de professors d'ensenyament secundari", 554),
        "MU": Specialty("MU", "Música", "Cos de professors d'ensenyament secundari", 166),
        "PSI": Specialty("PSI", "Orientació educativa", "Cos de professors d'ensenyament secundari", 523),
        "TEC": Specialty("TEC", "Tecnologia", "Cos de professors d'ensenyament secundari", 336),
        "601": Specialty("601", "Cuina i pastisseria", "Cos de professors tècnics de formació professional", 37),
        "602": Specialty("602", "Equips electrònics", "Cos de professors tècnics de formació professional", 7),
        "603": Specialty("603", "Estètica", "Cos de professors tècnics de formació professional", 24),
        "604": Specialty("604", "Fabricació i instal·lació de fusteria i mobles",
                         "Cos de professors tècnics de formació professional", 4),
        "605": Specialty("605", "Instal·lació i manteniment d’equips tèrmics i fluids",
                         "Cos de professors tècnics de formació professional", 4),
        "606": Specialty("606", "Instal·lacions electrotècniques",
                         "Cos de professors tècnics de formació professional", 26),
        "607": Specialty("607", "Instal·lació i equips de criança i cultiu",
                         "Cos de professors tècnics de formació professional", 1),
        "608": Specialty("608", "Laboratori", "Cos de professors tècnics de formació professional", 7),
        "609": Specialty("609", "Manteniment de vehicles", "Cos de professors tècnics de formació professional", 51),
        "610": Specialty("610", "Màquines, serveis i producció",
                         "Cos de professors tècnics de formació professional", 6),
        "611": Specialty("611", "Mecanització i manteniment de màquines",
                         "Cos de professors tècnics de formació professional", 41),
        "612": Specialty("612", "Oficina de projectes de construcció",
                         "Cos de professors tècnics de formació professional", 3),
        "614": Specialty("614", "Operacions d’equips d’elaboració de productes alimentaris",
                         "Cos de professors tècnics de formació professional", 3),
        "615": Specialty("615", "Operacions de processos", "Cos de professors tècnics de formació professional", 7),
        "616": Specialty("616", "Operacions i equips de producció agrària",
                         "Cos de professors tècnics de formació professional", 4),
        "617": Specialty("617", "Patronatge i confecció", "Cos de professors tècnics de formació professional", 6),
        "618": Specialty("618", "Perruqueria", "Cos de professors tècnics de formació professional", 30),
        "619": Specialty("619", "Procediments de diagnòstic clínic i ortoprotètics",
                         "Cos de professors tècnics de formació professional", 38),
        "620": Specialty("620", "Procediments sanitaris i assistencials",
                         "Cos de professors tècnics de formació professional", 89),
        "621": Specialty("621", "Processos comercials", "Cos de professors tècnics de formació professional", 36),
        "622": Specialty("622", "Processos de gestió administrativa",
                         "Cos de professors tècnics de formació professional", 58),
        "623": Specialty("623", "Producció en arts gràfiques", "Cos de professors tècnics de formació professional", 6),
        "625": Specialty("625", "Serveis a la comunitat", "Cos de professors tècnics de formació professional", 75),
        "626": Specialty("626", "Serveis de restauració", "Cos de professors tècnics de formació professional", 9),
        "627": Specialty("627", "Sistemes i aplicacions informàtiques",
                         "Cos de professors tècnics de formació professional", 81),
        "628": Specialty("628", "Soldadures", "Cos de professors tècnics de formació professional", 10),
        "629": Specialty("629", "Màquines, serveis i producció",
                         "Cos de professors tècnics de formació professional", 5),
        "133": Specialty("133", "Alemany", "Cos de professors d'escoles oficials d'idiomes", 20),
        "134": Specialty("134", "Àrab", "Cos de professors d'escoles oficials d'idiomes", 3),
        "135": Specialty("135", "Italià", "Cos de professors d'escoles oficials d'idiomes", 4),
        "136": Specialty("136", "Japonès", "Cos de professors d'escoles oficials d'idiomes", 1),
        "137": Specialty("137", "Portuguès", "Cos de professors d'escoles oficials d'idiomes", 1),
        "138": Specialty("138", "Rus", "Cos de professors d'escoles oficials d'idiomes", 4),
        "139": Specialty("139", "Xinès", "Cos de professors d'escoles oficials d'idiomes", 3),
        "190": Specialty("190", "Espanyol", "Cos de professors d'escoles oficials d'idiomes", 6),
        "192": Specialty("192", "Francès", "Cos de professors d'escoles oficials d'idiomes", 26),
        "193": Specialty("193", "Anglès", "Cos de professors d'escoles oficials d'idiomes", 58),
        "195": Specialty("195", "Català", "Cos de professors d'escoles oficials d'idiomes", 4),
        "197": Specialty("197", "Neerlandès", "Cos de professors d'escoles oficials d'idiomes", 1),
        "198": Specialty("198", "Èuscar", "Cos de professors d'escoles oficials d'idiomes", 1),
        "199": Specialty("199", "Coreà", "Cos de professors d'escoles oficials d'idiomes", 1),
        "703": Specialty("703", "Construcció i restauració d’obres escultòriques",
                         "Cos de professors d'arts plàstiques i disseny", 1),
        "707": Specialty("707", "Dibuix artístic i color", "Cos de professors d'arts plàstiques i disseny", 14),
        "708": Specialty("708", "Dibuix tècnic", "Cos de professors d'arts plàstiques i disseny", 5),
        "709": Specialty("709", "Disseny d'interiors", "Cos de professors d'arts plàstiques i disseny", 9),
        "710": Specialty("710", "Disseny de moda", "Cos de professors d'arts plàstiques i disseny", 1),
        "711": Specialty("711", "Disseny de producte", "Cos de professors d'arts plàstiques i disseny", 1),
        "712": Specialty("712", "Disseny gràfic", "Cos de professors d'arts plàstiques i disseny", 15),
        "715": Specialty("715", "Fotografia", "Cos de professors d'arts plàstiques i disseny", 6),
        "716": Specialty("716", "Història de l'art", "Cos de professors d'arts plàstiques i disseny", 5),
        "719": Specialty("719", "Materials i tecnologia - conservació i restauració",
                         "Cos de professors d'arts plàstiques i disseny", 1),
        "720": Specialty("720", "Materials i tecnologia - disseny", "Cos de professors d'arts plàstiques i disseny", 3),
        "721": Specialty("721", "Mitjans audiovisuals", "Cos de professors d'arts plàstiques i disseny", 6),
        "722": Specialty("722", "Mitjans informàtics", "Cos de professors d'arts plàstiques i disseny", 2),
        "723": Specialty("723", "Organització industrial i legislació",
                         "Cos de professors d'arts plàstiques i disseny", 6),
        "725": Specialty("725", "Volum", "Cos de professors d'arts plàstiques i disseny", 7),
        "806": Specialty("806", "Enquadernació artística", "Cos de mestres de tallers d'arts plàstiques i disseny", 1),
        "809": Specialty("809", "Modelisme i maquetisme", "Cos de mestres de tallers d'arts plàstiques i disseny", 1),
        "812": Specialty("812", "Talla en pedra i fusta", "Cos de mestres de tallers d'arts plàstiques i disseny", 2),
        "813": Specialty("813", "Tècniques ceràmiques", "Cos de mestres de tallers d'arts plàstiques i disseny", 3),
        "817": Specialty("817", "Tècniques de patronatge i confecció",
                         "Cos de mestres de tallers d'arts plàstiques i disseny", 1)
    }


def loadCandidates():
    list_of_candidates = []
    with open('data/parsed_barem_provisional.json') as f:
        data = json.load(f)
        for obj in data:
            new_candidate = Candidate(obj["full_name"], obj["tribunal"])
            for attempt in obj["attempts"]:
                new_candidate.addAttempt(attempt["code"], attempt["points"], attempt["priority"])
            bisect.insort(list_of_candidates, new_candidate)
    return list_of_candidates


def writeCSV(dictionary):
    for key in dictionary:
        with open("testLists/" + dictionary[key].specialtyCode + " " + str(dictionary[key].specialtyName) + ".csv", "w",
                  newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Nom", "Barem", "Tribunal", "Prioritat"])
            for member in specialties[key].members:
                # Fix for catalan locale where decimal point is a comma
                attempt = member.currentAttempt()
                formatted_float = "{:.4f}".format(attempt.points).replace(".", ",")
                writer.writerow([member.fullName, formatted_float, member.tribunal, attempt.priority])


if __name__ == '__main__':
    specialties = loadSpecialties()
    candidates = loadCandidates()

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

    writeCSV(specialties)
