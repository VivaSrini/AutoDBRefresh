# Source Info:
#   {
#     "Provider": "FL_ORANGE",
#     "State": "FL",
#     "Name": "Orange County, Florida",
#     "Website": "https://ocfl.diversitycompliance.com/FrontEnd/searchcertifieddirectory.asp",
#     "Title": "Certified Vendor Directory",
#     "Download": "Manual",
#     "FileName": "FL_ORANGE.csv",
#   }
#
# ╔═══════════════════════════╦════════════════════╦════════════╗
# ║ DEST_COL_NAME             ║ SRC_COL_NAME       ║ SRC_COL_NO ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Sequence                  ║ Program            ║  Generated ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Company Name              ║ Company Name       ║      1     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ DBA                       ║ DBA Name           ║      2     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ DUNS Number               ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Addr Line 1               ║ Address            ║      5     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Addr Line 2               ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ City                      ║ City               ║      6     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ State                     ║ State              ║      7     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Zip Code                  ║ Zip                ║      8     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Website                   ║ Website            ║     14     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Contact Person            ║ Owner First,       ║     3,     ║
# ║                           ║ Owner Last         ║      4     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Phone                     ║ Telephone          ║     13     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Cell Phone                ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Fax                       ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Email Address             ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Gender                    ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Ethnicity                 ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Given Diversity           ║ Certification Type ║     16     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Primary Diversity         ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Other Diversities         ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Certifying Agency         ║ Agency             ║     15     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Certification Number      ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Certification Start Date  ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Certification Expiry Date ║ Expiration         ║     17     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Primary NAICS Code        ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Other NAICS Codes         ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Business Description      ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Additional Details 1      ║ Mailing Address    ║      9     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Additional Details 2      ║ Mail Addr City     ║     10     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Additional Details 3      ║ Mail Addr State    ║     11     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Additional Details 4      ║ Mail ADdr Zip      ║     12     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Additional Details 5      ║ Capability         ║     18     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Additional Details 6      ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Additional Details 7      ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Additional Details 8      ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Additional Details 9      ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Additional Details 10     ║                    ║            ║
# ╚═══════════════════════════╩════════════════════╩════════════╝
#
import csv
import logging

from src import custom_logger, prepare_csv_data, empty_dict
from src import trim_file_header_rows, get_pnaics_onaics

log = custom_logger.LogGen.logGen()
log.setLevel(level=logging.DEBUG)

provider = "FL_ORANGE"
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
            dict1['website'] = prepare_csv_data(row[13])
            dict1['contact'] = f'{prepare_csv_data(row[2])} {prepare_csv_data(row[3])}'
            dict1['phone'] = prepare_csv_data(row[12])
            dict1['gdiverse'] = prepare_csv_data(row[15])
            dict1['cert_agency'] = prepare_csv_data(row[14])
            dict1['cert_expiry'] = prepare_csv_data(row[16])
            dict1['addl1'] = prepare_csv_data(row[8], prefix='Mailing Address')
            dict1['addl2'] = prepare_csv_data(row[9], prefix='Mail Addr City')
            dict1['addl3'] = prepare_csv_data(row[10], prefix='Mail Addr State')
            dict1['addl4'] = prepare_csv_data(row[11], prefix='Mail Addr Zip')
            dict1['addl5'] = prepare_csv_data(row[17], prefix='Capabilities')
            records.append(dict1)

    return records
