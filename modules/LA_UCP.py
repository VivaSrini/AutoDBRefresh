# Source Info:
#  {
#    "Provider": "LA_UCP",
#    "State": "LA",
#    "Name": "Louisiana UCP - LA UCP",
#    "Title": "UCP Search",
#    "ImportedFileName": "DBEList.csv"
#  }

# Field Mapping:
#
# ╔═══════════════════════════╦══════════════════╦════════════╗
# ║ DEST_COL_NAME             ║ SRC_COL_NAME     ║ SRC_COL_NO ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Sequence                  ║ Program          ║  Generated ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Company Name              ║ VENDOR_NAME      ║      2     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ DBA                       ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ DUNS Number               ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Addr Line 1               ║ MAIL_ADDR_STREET ║      5     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Addr Line 2               ║ MAIL_ADDR_AUX    ║      6     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ City                      ║ MAIL_CITY        ║      9     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ State                     ║ MAIL_STATE       ║     10     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Zip Code                  ║ MAIL_ZIP_CODE    ║     11     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Website                   ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Contact Person            ║ OWNER_NAME       ║     14     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Phone                     ║ PHONE_NUM        ║     12     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Cell Phone                ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Fax                       ║ FAX_NUM          ║     13     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Email Address             ║ EMAIL_ADDR       ║     15     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Gender                    ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Ethnicity                 ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Given Diversity           ║ MINORITY_TYPE    ║      3     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Primary Diversity         ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Other Diversities         ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Certifying Agency         ║ CERT_AGENCY      ║     16     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Certification Number      ║ VENDOR_NUM       ║      1     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Certification Start Date  ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Certification Expiry Date ║ EXPIRATION_DATE  ║      4     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Primary NAICS Code        ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Other NAICS Codes         ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Business Description      ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Additional Details 1      ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Additional Details 2      ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Additional Details 3      ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Additional Details 4      ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Additional Details 5      ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Additional Details 6      ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Additional Details 7      ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Additional Details 8      ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Additional Details 9      ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Additional Details 10     ║                  ║            ║
# ╚═══════════════════════════╩══════════════════╩════════════╝
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

    trim_file_header_rows(file_name=filename, num_lines=2)
    columns_to_be_removed = ['WORK_CODE', 'WORK_DESCRIPTION']
    dedup_csv(filename, columns_to_be_removed)

    with open(filename, encoding="utf8") as f:
        reader = csv.reader(f)
        next(reader, None)     # CSV Header

        for row_num, row in enumerate(reader):
            dict1 = empty_dict()
            dict1['source'] = provider
            dict1['sequence'] = prepare_csv_data(row_num + 1)
            dict1['company'] = prepare_csv_data(row[1])
            dict1['addr1'] = prepare_csv_data(row[4])
            dict1['addr2'] = prepare_csv_data(row[5])
            dict1['city'] = prepare_csv_data(row[8])
            dict1['state'] = prepare_csv_data(row[9])
            dict1['zipcode'] = prepare_csv_data(row[10])
            dict1['contact'] = prepare_csv_data(row[13])
            dict1['phone'] = prepare_csv_data(row[11])
            dict1['fax'] = prepare_csv_data(row[12])
            dict1['email'] = prepare_csv_data(row[14])
            dict1['ethnicity'] = prepare_csv_data(get_primary(row[6]))
            dict1['gdiverse'] = prepare_csv_data(get_primary(row[2]))
            dict1['cert_agency'] = prepare_csv_data(row[15])
            dict1['cert_num'] = prepare_csv_data(row[0])
            dict1['cert_expiry'] = prepare_csv_data(row[3])
            dict1['addl1'] = prepare_csv_data(row[7], prefix='License Number(s)')
            dict1['addl2'] = prepare_csv_data(row[16], prefix='Service Type(s)')
            records.append(dict1)

    return records
