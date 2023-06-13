# Source Info:
#   {
#     "Provider": "FL_PENSACOLA",
#     "State": "FL",
#     "Name": "City of Pensacola, FL",
#     "Website": "https://pensacola.mwdbe.com/FrontEnd/searchcertifieddirectory.asp",
#     "Title": "City of Pensacola Certified Firm Directory",
#     "Download": "Manual",
#     "FileName": "FL_PENSACOLA.csv",
#   }
#

import csv
import logging

from src import custom_logger, prepare_csv_data, empty_dict
from src import trim_file_header_rows, get_pnaics_onaics

log = custom_logger.LogGen.logGen()
log.setLevel(level=logging.DEBUG)

provider = "FL_PENSACOLA"
records = []


def processFile(filename):
    log.info(f'Loaded module {provider}...')

    trim_file_header_rows(file_name=filename, num_lines=5)
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader, None)     # CSV Header

        for row_num, row in enumerate(reader):
            if not row: break
            dict1 = empty_dict()
            dict1['source'] = provider
            dict1['sequence'] = prepare_csv_data(row_num + 1)
            dict1['company'] = prepare_csv_data(row[0])
            dict1['dba'] = prepare_csv_data(row[1])
            dict1['gdiverse'] = prepare_csv_data(row[4])
            dict1['cert_agency'] = prepare_csv_data(row[3])
            (pnaics, onaics) = get_pnaics_onaics(row[6])
            dict1['pnaics'] = pnaics
            dict1['onaics'] = prepare_csv_data(onaics)
            dict1['addl1'] = prepare_csv_data(row[2], prefix='Location')
            records.append(dict1)

    return records
