# Source Info:
#  {
#    "Provider": "CA_DOT",
#    "State": "CA",
#    "Name": "California DOT",
#    "Title": "UCP Web Application - Main Page",
#    "ImportedFileName": "UCPReport.xls"
#  }

# ╔═══════════════════════════╦═════════════════╦════════════╗
# ║ DEST_COL_NAME             ║ SRC_COL_NAME    ║ SRC_COL_NO ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Sequence                  ║ Program         ║  Generated ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Company Name              ║ Firm Name       ║      5     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ DBA                       ║ DBA Name        ║      4     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ DUNS Number               ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Addr Line 1               ║ Address 1       ║      6     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Addr Line 2               ║ Address 2       ║      7     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ City                      ║ City            ║      8     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ State                     ║ State           ║      9     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Zip Code                  ║ Zip Code        ║    10,11   ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Website                   ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Contact Person            ║ Contact Name    ║     19     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Phone                     ║ Tel             ║    20-25   ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Cell Phone                ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Fax                       ║ Fax             ║    26,27   ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Email Address             ║ EMail           ║     18     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Gender                    ║ Gender          ║     36     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Ethnicity                 ║ Ethnicity       ║     37     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Given Diversity           ║ Firm Type       ║     38     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Primary Diversity         ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Other Diversities         ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Certifying Agency         ║ Agency Name     ║     28     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Certification Number      ║ Firm Id         ║      1     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Certification Start Date  ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Certification Expiry Date ║ Suspended Date  ║      3     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Primary NAICS Code        ║ DBE/ACDBE NAICS ║    31,32   ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Other NAICS Codes         ║ DBE/ACDBE NAICS ║    31,32   ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Business Description      ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Additional Details 1      ║ Counties        ║     29     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Additional Details 2      ║ Districts       ║     30     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Additional Details 3      ║ Work Codes      ║     33     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Additional Details 4      ║ Licenses        ║     34     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Additional Details 5      ║ Trucks          ║     35     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Additional Details 6      ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Additional Details 7      ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Additional Details 8      ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Additional Details 9      ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Additional Details 10     ║                 ║            ║
# ╚═══════════════════════════╩═════════════════╩════════════╝

import csv
import logging

from src import custom_logger, empty_dict, prepare_csv_data, get_primary, get_other, format_phone

log = custom_logger.LogGen.logGen()
log.setLevel(level=logging.DEBUG)

provider = "CA_DOT"
records = []


def processFile(filename):
    log.info(f'Loaded module {provider}...')

    with open(filename, encoding="utf8") as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader, None)

        for row_num, row in enumerate(reader):
            dict1 = empty_dict()
            dict1['source'] = provider
            dict1['sequence'] = prepare_csv_data(row_num + 1)
            dict1['company'] = prepare_csv_data(row[4])
            dict1['dba'] = prepare_csv_data(row[3])
            dict1['addr1'] = prepare_csv_data(row[5])
            dict1['addr2'] = prepare_csv_data(row[6])
            dict1['city'] = prepare_csv_data(row[7])
            dict1['state'] = prepare_csv_data(row[8])
            dict1['zipcode'] = prepare_csv_data(row[9] + ('-'+row[10] if row[10] else ''))
            dict1['contact'] = prepare_csv_data(row[18])
            dict1['phone'] = prepare_csv_data(format_phone(area_code=row[19], number=row[20], ext=row[21]))
            dict1['fax'] = prepare_csv_data(format_phone(area_code=row[25], number=row[26]) if row[25] else '')
            dict1['email'] = prepare_csv_data(row[17])
            dict1['gender'] = prepare_csv_data(row[35])
            dict1['ethnicity'] = prepare_csv_data(row[36])
            dict1['gdiverse'] = prepare_csv_data(row[37])
            dict1['cert_agency'] = prepare_csv_data(row[27])
            dict1['cert_num'] = prepare_csv_data(row[0])
            dict1['pnaics'] = prepare_csv_data(get_primary((row[30]+'; ' if row[30] else '') + row[31], separator=';'))
            dict1['onaics'] = prepare_csv_data(get_other((row[30]+'; ' if row[30] else '') + row[31], separator=';'))
            dict1['addl1'] = prepare_csv_data(row[28], prefix='Counties')
            dict1['addl2'] = prepare_csv_data(row[29], prefix='Districts')
            dict1['addl3'] = prepare_csv_data(row[32], prefix='Work Codes')
            dict1['addl4'] = prepare_csv_data(row[33], prefix='Licenses')
            dict1['addl5'] = prepare_csv_data(row[34], prefix='Trucks')
            records.append(dict1)
            row_num += 1

        return records
