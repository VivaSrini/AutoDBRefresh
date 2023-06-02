# Source Info:

#  {
#    "Provider": "CA_PORTOAK",
#    "State": "CA",
#    "Name": "Port of Oakland, CA",
#    "Title": "Port's Social Responsibility database of certified businesses",
#    "ImportedFileName": "SRD-Output.csv"
#  }

# Summary of process:
#   1. Remove last 4 columns creating duplicates
#   2. Remove duplicate lines

# Field Mapping:
#
# ╔════════════════════════════╦══════════════════════════╦════════════╗
# ║ DEST_COL_NAME              ║ SRC_COL_NAME             ║ SRC_COL_NO ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Sequence                   ║ Program Generated        ║            ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Company Name               ║ CompanyName              ║ 1          ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ DBA                        ║                          ║            ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ DUNS Number                ║                          ║            ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Addr Line 1                ║ StreetAddress1           ║ 4          ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Addr Line 2                ║                          ║            ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ City                       ║ City                     ║ 5          ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ State                      ║ "CA"                     ║            ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Zip Code                   ║ ZipCode                  ║ 6          ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Website                    ║ WebAddress               ║ 14         ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Contact Person             ║ FirstName, LastName      ║ 2, 3       ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Phone                      ║ Company Phone            ║ 8          ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Cell Phone                 ║                          ║            ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Fax                        ║ Fax                      ║ 9          ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Email Address              ║ eMailAddress             ║ 10         ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Gender                     ║                          ║            ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Ethnicity                  ║                          ║            ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Given Diversity            ║                          ║            ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Primary Diversity          ║ CertType                 ║ 12         ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Other Diversities          ║ CertType                 ║ 12         ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Certifying Agency          ║ "Port of Oakland"        ║            ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Certification Number       ║ CertNumber               ║ 13         ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Certification Start Date   ║                          ║            ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Certification Expiry Date ║ ExpirationDate           ║ 11         ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Primary NAICS Code         ║ NAICS                    ║ 19         ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Other NAICS Codes          ║ NAICS                    ║ 19         ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Business Description       ║                          ║            ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Additional Details 1       ║ PrimaryService           ║ 15         ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Additional Details 2       ║ SpecialtyService         ║ 16         ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Additional Details 3       ║ ConsumerAffairs_Category ║ 17         ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Additional Details 4       ║                          ║            ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Additional Details 5       ║                          ║            ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Additional Details 6       ║                          ║            ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Additional Details 7       ║                          ║            ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Additional Details 8       ║                          ║            ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Additional Details 9       ║                          ║            ║
# ╠════════════════════════════╬══════════════════════════╬════════════╣
# ║ Additional Details 10      ║                          ║            ║
# ╚════════════════════════════╩══════════════════════════╩════════════╝
#

import csv
import logging

from src import custom_logger, prepare_csv_data, dedup_csv, empty_dict
from src import get_primary, get_other

log = custom_logger.LogGen.logGen()
log.setLevel(level=logging.DEBUG)

provider = "CA_PORTOAK"
records = []


def processFile(filename):
    log.info(f'Loaded module {provider}...')
    columns_to_be_removed = ['PContact First Name', 'PContact Last Name', 'PContact Email Address', 'PContact Phone']
    dedup_csv(filename, columns_to_be_removed)

    with open(filename, encoding="utf8") as f:
        reader = csv.reader(f)
        next(reader, None)

        for row_num, row in enumerate(reader):
            dict1 = empty_dict()
            dict1['source'] = provider
            dict1['sequence'] = prepare_csv_data(row_num + 1)
            dict1['company'] = prepare_csv_data(row[0])
            dict1['addr1'] = prepare_csv_data(row[3])
            dict1['city'] = prepare_csv_data(row[4])
            dict1['state'] = 'CA'
            dict1['zipcode'] = prepare_csv_data(row[5])
            dict1['website'] = prepare_csv_data(row[13])
            dict1['contact'] = prepare_csv_data(row[1]) + ' ' + prepare_csv_data(row[2])
            dict1['phone'] = prepare_csv_data(row[7])
            dict1['fax'] = prepare_csv_data(row[8])
            dict1['email'] = prepare_csv_data(row[9])
            dict1['pdiverse'] = prepare_csv_data(get_primary(row[11]))
            dict1['odiverse'] = prepare_csv_data(get_other(row[11]))
            dict1['cert_agency'] = 'Port of Oakland'
            dict1['cert_num'] = prepare_csv_data(row[12])
            dict1['pnaics'] = prepare_csv_data(get_primary(row[18], pattern=r'[0-9]{6}'))
            dict1['onaics'] = prepare_csv_data(get_other(row[18], pattern=r'[0-9]{6}'))
            dict1['addl1'] = prepare_csv_data(row[14], prefix='Primary Service')
            dict1['addl2'] = prepare_csv_data(row[15], prefix='Specialty Service')
            dict1['addl3'] = prepare_csv_data(row[16], prefix='Consumer Affairs Category')
            records.append(dict1)

    return records
