# Source Info:
#   {
#     "Provider": "MN_DOA",
#     "State": "MN",
#     "Name": "Minnesota DOA",
#     "Title": "Equity in Procurement (TG/ED/VO) Directory / Minnesota Office of State Procurement",
#     "ImportedFileName": "vmpvendors.csv",
#   }
#
# Field Mapping:
#
# ╔═══════════════════════════╦══════════════════════════╦════════════╗
# ║ DEST_COL_NAME             ║ SRC_COL_NAME             ║ SRC_COL_NO ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Sequence                  ║ Program                  ║  Generated ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Company Name              ║ Vendor                   ║      1     ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ DBA                       ║                          ║            ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ DUNS Number               ║                          ║            ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Addr Line 1               ║ Address                  ║      2     ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Addr Line 2               ║                          ║            ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ City                      ║ City                     ║      3     ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ State                     ║ State                    ║      4     ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Zip Code                  ║ Zip                      ║      5     ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Website                   ║                          ║            ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Contact Person            ║ Owner                    ║     11     ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Phone                     ║ Telephone                ║      6     ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Cell Phone                ║                          ║            ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Fax                       ║ Fax                      ║      8     ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Email Address             ║ Email                    ║      7     ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Gender                    ║                          ║            ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Ethnicity                 ║                          ║            ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Given Diversity           ║                          ║            ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Primary Diversity         ║                          ║            ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Other Diversities         ║                          ║            ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Certifying Agency         ║ 'State of Minnesota DOA' ║            ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Certification Number      ║ SWIFT                    ║     12     ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Certification Start Date  ║ CertDate                 ║     13     ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Certification Expiry Date ║                          ║            ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Primary NAICS Code        ║ NAICS                    ║     14     ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Other NAICS Codes         ║                          ║            ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Business Description      ║ Description              ║     15     ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Additional Details 1      ║ County                   ║      9     ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Additional Details 2      ║ Category                 ║     10     ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Additional Details 3      ║                          ║            ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Additional Details 4      ║                          ║            ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Additional Details 5      ║                          ║            ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Additional Details 6      ║                          ║            ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Additional Details 7      ║                          ║            ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Additional Details 8      ║                          ║            ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Additional Details 9      ║                          ║            ║
# ╠═══════════════════════════╬══════════════════════════╬════════════╣
# ║ Additional Details 10     ║                          ║            ║
# ╚═══════════════════════════╩══════════════════════════╩════════════╝
#

import csv
import logging

from src import custom_logger, prepare_csv_data, dedup_csv, empty_dict
from src import get_primary, trim_file_header_rows

log = custom_logger.LogGen.logGen()
log.setLevel(level=logging.DEBUG)

provider = "LA_UCP"
records = []


def processFile(filename):
    log.info(f'Loaded module {provider}...')

    with open(filename, encoding="utf8") as f:
        reader = csv.reader(f)
        next(reader, None)     # CSV Header

        for row_num, row in enumerate(reader):
            dict1 = empty_dict()
            dict1['source'] = provider
            dict1['sequence'] = prepare_csv_data(row_num + 1)
            dict1['company'] = prepare_csv_data(row[0])
            dict1['addr1'] = prepare_csv_data(row[1])
            dict1['city'] = prepare_csv_data(row[2], pattern='(^[^,]*)')
            dict1['state'] = prepare_csv_data(row[3])
            dict1['zipcode'] = prepare_csv_data(row[4])
            dict1['contact'] = prepare_csv_data(row[10])
            dict1['phone'] = prepare_csv_data(row[5])
            dict1['fax'] = prepare_csv_data(row[7])
            dict1['email'] = prepare_csv_data(row[6])
            dict1['cert_agency'] = 'State of Minnesota DOA'
            dict1['cert_num'] = prepare_csv_data(row[11])
            dict1['cert_start'] = prepare_csv_data(row[12])
            dict1['pnaics'] = prepare_csv_data(row[13])
            dict1['biz_desc'] = prepare_csv_data(row[14])
            dict1['addl1'] = prepare_csv_data(row[8], prefix='County')
            dict1['addl2'] = prepare_csv_data(row[9], prefix='Category')
            records.append(dict1)

    return records
