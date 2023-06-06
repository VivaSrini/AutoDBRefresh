# Source Info:
#   {
#     "Provider": "MO_DOT_DBE",
#     "State": "MO",
#     "Name": "Missouri DOT - MODOT",
#     "Title": "MRCC Directory",
#     "ImportedFileName": "MRCC_DBE.csv",
#   }
#
# Field Mapping:
#
# ╔═══════════════════════════╦════════════════╦════════════╗
# ║ DEST_COL_NAME             ║ SRC_COL_NAME   ║ SRC_COL_NO ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Sequence                  ║ Program        ║  Generated ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Company Name              ║ DBE Name       ║      1     ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ DBA                       ║                ║            ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ DUNS Number               ║                ║            ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Addr Line 1               ║ Address        ║      2     ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Addr Line 2               ║                ║            ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ City                      ║ City           ║      3     ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ State                     ║ State          ║      4     ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Zip Code                  ║ Zip            ║      5     ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Website                   ║                ║            ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Contact Person            ║ Owner          ║      8     ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Phone                     ║ Telephone      ║      9     ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Cell Phone                ║                ║            ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Fax                       ║ Fax            ║     10     ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Email Address             ║ Email          ║     11     ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Gender                    ║ Gender         ║     14     ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Ethnicity                 ║ Ethnicity      ║     15     ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Given Diversity           ║                ║            ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Primary Diversity         ║                ║            ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Other Diversities         ║                ║            ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Certifying Agency         ║ Agency         ║     12     ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Certification Number      ║                ║            ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Certification Start Date  ║                ║            ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Certification Expiry Date ║                ║            ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Primary NAICS Code        ║ NAICS          ║     17     ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Other NAICS Codes         ║                ║    19-43   ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Business Description      ║                ║            ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Additional Details 1      ║ County         ║      6     ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Additional Details 2      ║ District       ║      7     ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Additional Details 3      ║ DBE Certified? ║     16     ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Additional Details 4      ║                ║            ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Additional Details 5      ║                ║            ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Additional Details 6      ║                ║            ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Additional Details 7      ║                ║            ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Additional Details 8      ║                ║            ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Additional Details 9      ║                ║            ║
# ╠═══════════════════════════╬════════════════╬════════════╣
# ║ Additional Details 10     ║                ║            ║
# ╚═══════════════════════════╩════════════════╩════════════╝
#

import csv
import logging

from src import custom_logger, prepare_csv_data, empty_dict

log = custom_logger.LogGen.logGen()
log.setLevel(level=logging.DEBUG)

provider = "MO_DOT_ACDBE"
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
            dict1['city'] = prepare_csv_data(row[2])
            dict1['state'] = prepare_csv_data(row[3])
            dict1['zipcode'] = prepare_csv_data(row[4])
            dict1['contact'] = prepare_csv_data(row[7])
            dict1['phone'] = prepare_csv_data(row[8])
            dict1['fax'] = prepare_csv_data(row[9])
            dict1['email'] = prepare_csv_data(row[10])
            dict1['gender'] = prepare_csv_data(row[13])
            dict1['ethnicity'] = prepare_csv_data(row[14])
            dict1['cert_agency'] = prepare_csv_data(row[11])
            dict1['pnaics'] = prepare_csv_data(row[16])
            onaics = []
            try:
                for i in range(18, 44, 2):
                    onaics.append(prepare_csv_data(row[i]))
            except IndexError as _e:
                pass
            dict1['onaics'] = ', '.join(onaics)
            dict1['addl1'] = prepare_csv_data(row[5], prefix='County')
            dict1['addl2'] = prepare_csv_data(row[6], prefix='District')
            dict1['addl3'] = prepare_csv_data(row[15], prefix='DBE Certified?')
            if dict1['addl3'] == 'DBE Certified?: Certified':
                dict1['gdiverse'] = 'DBE'
            records.append(dict1)

    return records
