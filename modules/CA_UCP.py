# Source Info:
#   {
#     "Provider": "CA_UCP",
#     "State": "CA",
#     "Name": "California UCP",
#     "Website": "https://californiaucp.dbesystem.com/FrontEnd/searchcertifieddirectory.asp",
#     "Title": "Certified Vendor Directory",
#     "Download": "Manual",
#     "FileName": "CA_UCP.csv",
#   }
#

import csv
import logging

from src import custom_logger, prepare_csv_data, empty_dict
from src import trim_file_header_rows, get_pnaics_onaics

log = custom_logger.LogGen.logGen()
log.setLevel(level=logging.DEBUG)

provider = "CA_UCP"
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
            dict1['addr1'] = prepare_csv_data(row[4])
            dict1['city'] = prepare_csv_data(row[5])
            dict1['state'] = prepare_csv_data(row[6])
            dict1['zipcode'] = prepare_csv_data(row[7])
            dict1['website'] = prepare_csv_data(row[15])
            dict1['contact'] = f'{prepare_csv_data(row[2])} {prepare_csv_data(row[3])}'
            dict1['phone'] = prepare_csv_data(row[12])
            dict1['fax'] = prepare_csv_data(row[13])
            dict1['email'] = prepare_csv_data(row[14])
            dict1['gdiverse'] = prepare_csv_data(row[17])
            dict1['gender'] = prepare_csv_data(row[19])
            dict1['ethnicity'] = prepare_csv_data(row[18])
            dict1['cert_agency'] = prepare_csv_data(row[16])
            dict1['cert_num'] = prepare_csv_data(row[22])
            (pnaics, onaics) = get_pnaics_onaics(row[23])
            dict1['pnaics'] = pnaics
            dict1['onaics'] = prepare_csv_data(onaics)
            dict1['addl1'] = prepare_csv_data(row[8], prefix='Mailing Address')
            dict1['addl2'] = prepare_csv_data(row[9], prefix='Mail Addr City')
            dict1['addl3'] = prepare_csv_data(row[10], prefix='Mail Addr State')
            dict1['addl4'] = prepare_csv_data(row[11], prefix='Mail Addr Zip')
            dict1['addl5'] = prepare_csv_data(row[20], prefix='Capabilities')
            dict1['addl6'] = prepare_csv_data(row[21], prefix='County')
            records.append(dict1)

    return records
