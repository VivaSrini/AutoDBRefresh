# Source Info:
#   {
#     "Provider": "OH_COLUMBUS",
#     "State": "OH",
#     "Name": "City of Columbus, OH",
#     "Website": "https://cleveland.diversitycompliance.com/FrontEnd/searchcertifieddirectory.asp",
#     "Title": "City of Columbus Certified Vendor Directory",
#     "Download": "Manual",
#     "FileName": "OH_COLUMBUS.csv",
#   }
#

import csv
import logging

from src import custom_logger, prepare_csv_data, empty_dict
from src import trim_file_header_rows, get_pnaics_onaics

log = custom_logger.LogGen.logGen()
log.setLevel(level=logging.DEBUG)

provider = "OH_COLUMBUS"
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
            dict1['addr1'] = prepare_csv_data(row[2])
            dict1['city'] = prepare_csv_data(row[3])
            dict1['state'] = prepare_csv_data(row[4])
            dict1['zipcode'] = prepare_csv_data(row[5])
            dict1['website'] = prepare_csv_data(row[11])
            dict1['email'] = prepare_csv_data(row[10])
            dict1['gdiverse'] = prepare_csv_data(row[13])
            dict1['cert_agency'] = prepare_csv_data(row[12])
            (pnaics, onaics) = get_pnaics_onaics(row[30])
            dict1['pnaics'] = pnaics
            dict1['onaics'] = prepare_csv_data(onaics)
            dict1['biz_desc'] = prepare_csv_data(row[24])
            dict1['addl1'] = prepare_csv_data(row[6], prefix='Mailing Address')
            dict1['addl2'] = prepare_csv_data(row[9], prefix='Mail Addr Zip')
            dict1['addl3'] = prepare_csv_data(row[14], prefix='Capabilities')
            dict1['addl4'] = prepare_csv_data(row[15], prefix='County')
            dict1['addl5'] = prepare_csv_data(row[16], prefix='Bonding Capacity')
            dict1['addl6'] = prepare_csv_data(row[17], prefix='Eligible for Goals')
            dict1['addl7'] = prepare_csv_data(row[18], prefix='Eligible for Incentive Credits and Bid Discounts')
            dict1['addl8'] = prepare_csv_data(row[19], prefix='Number of Employees')
            dict1['addl9'] = prepare_csv_data(row[26], prefix='Facebook')
            dict1['addl10'] = prepare_csv_data(row[27], prefix='LinkedIn')

            records.append(dict1)

    return records