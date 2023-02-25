import tabula
import os

tribunal_pages = [
    '1-242', '243-276', '277-386', '387-485', '486-563', '564-621', '622-693', '694-798', '799-847', '848-924',
    '925-998', '999-1197', '1198-1351', '1-91', '92-238', '239-270', '271-304', '305-484', '485-771', '772-898',
    '899-990', '991-1059', '1060-1396'
]

specialty_pages = {
    '501': '1-14', '502': '15-19', '503': '20-21', '504': '22-24', '505': '25-45', '506': '46-49', '507': '50-60',
    '508': '61-76', '509': '77', '510': '78-87', '511': '88-91', '512': '92-95', '513': '96-98', '514': '99',
    '515': '100-102', '516': '103-105', '517': '106-109', '518': '110-116', '519': '117-119', '520': '120',
    '522': '121', '523': '122', '524': '123-125', '525': '126-130', 'AL': '131-134', 'AN': '135-174', 'AR': '175',
    'CN': '176-207', 'DI': '208-224', 'ECO': '225-239', 'EF': '240-260', 'FI': '261-271', 'FQ': '272-296',
    'FR': '297-307', 'GE': '308-344', 'GR': '345-348', 'IT': '349', 'LA': '350-354', 'LC': '355-387', 'LE': '388-417',
    'MA': '418-466', 'MU': '467-478', 'PSI': '479-525', 'TEC': '526-562', '601': '563-565', '602': '566-567',
    '603': '568-569', '604': '570', '605': '571-572', '606': '573-576', '607': '577', '608': '578-580',
    '609': '581-584', '610': '585', '611': '586-589', '612': '590-591', '614': '592', '615': '593-594',
    '616': '595-596', '617': '597', '618': '598-599', '619': '600-604', '620': '605-613', '621': '614-621',
    '622': '622-632', '623': '633', '625': '634-644', '626': '645-646', '627': '647-654', '628': '655',
    '629': '656-657', '133': '658-659', '134': '660', '135': '661', '137': '662', '138': '663', '139': '664',
    '190': '665-667', '192': '668-670', '193': '671-678', '195': '679-680', '197': '681', '198': '682', '199': '683',
    '703': '684', '707': '685-688', '708': '689-690', '709': '691-692', '710': '693', '711': '694', '712': '695-696',
    '715': '697-698', '716': '699-701', '719': '702', '720': '703', '721': '704-705', '722': '706', '723': '707-708',
    '725': '709-710', '806': '711', '809': '712', '812': '713', '813': '714', '817': '715', 'ALL': '716-730',
    'EES': '731-785', 'INF': '786-888', 'PAN': '889-933', 'PEF': '934-969', 'PFR': '970-972', 'PMU': '973-994',
    'PRI': '995-1163'
}

specialty_pages_codes = [
    '501', '502', '503', '504', '505', '506', '507', '508', '509', '510', '511', '512', '513', '514', '515', '516',
    '517', '518', '519', '520', '522', '523', '524', '525', 'AL', 'AN', 'AR', 'CN', 'DI', 'ECO', 'EF', 'FI', 'FQ', 'FR',
    'GE', 'GR', 'IT', 'LA', 'LC', 'LE', 'MA', 'MU', 'PSI', 'TEC', '601', '602', '603', '604', '605', '606', '607',
    '608', '609', '610', '611', '612', '614', '615', '616', '617', '618', '619', '620', '621', '622', '623', '625',
    '626', '627', '628', '629', '133', '134', '135', '137', '138', '139', '190', '192', '193', '195', '197', '198',
    '199', '703', '707', '708', '709', '710', '711', '712', '715', '716', '719', '720', '721', '722', '723', '725',
    '806', '809', '812', '813', '817', 'ALL', 'EES', 'INF', 'PAN', 'PEF', 'PFR', 'PMU', 'PRI'
]


def __tribunal_pdf():
    for i, pages in enumerate(tribunal_pages):
        if i < 13:
            pdf_path = os.path.abspath(os.path.join(
                os.path.dirname(__file__), "../data/llista-provisional-merits-tribunal-1-13.pdf")
            )
        else:
            pdf_path = os.path.abspath(os.path.join(
                os.path.dirname(__file__), "../data/llista-provisional-merits-tribunal-14-23.pdf")
            )
        if i < 9:
            csv_path = os.path.abspath(os.path.join(
                os.path.dirname(__file__), "../data/llista-provisional-merits-tribunal-0" + str(i + 1) + ".csv")
            )
        else:
            csv_path = os.path.abspath(os.path.join(
                os.path.dirname(__file__), "../data/llista-provisional-merits-tribunal-" + str(i + 1) + ".csv")
            )
        tabula.convert_into(pdf_path, csv_path, output_format="csv", pages=tribunal_pages[i])


def __specialty_pdf():
    pdf_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "../data/llista-provisional-merits-cos-especialitat.pdf")
    )
    for code in specialty_pages_codes:
        csv_path = os.path.abspath(os.path.join(
            os.path.dirname(__file__), "../data/llista-provisional-merits-cos-" + code + ".csv")
        )
        tabula.convert_into(pdf_path, csv_path, output_format="csv", pages=specialty_pages[code])


def __pdf2csv():
    __tribunal_pdf()
    __specialty_pdf()


if __name__ == "__main__":
    __pdf2csv()
