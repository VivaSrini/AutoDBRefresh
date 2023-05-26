# Source Info:
#  {
#    "Provider": "NV_GOED",
#    "State": "NV",
#    "Name": "Nevada Governor's Office of Economic Development",
#    "Title": "Emerging Small Business Directory - Nevada Governor's Office of Economic Development",
#    "ImportedFileName": "esb-download-MM-DD-YYYY-07-0404.csv"
#  }

# Field Mapping:
#
# ╔═══════════════════════════╦═════════════════════════╦════════════╗
# ║ DEST_COL_NAME             ║ SRC_COL_NAME            ║ SRC_COL_NO ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Sequence                  ║ Program                 ║  Generated ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Company Name              ║ LEGAL NAME OF BUSINESS  ║      7     ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ DBA                       ║ DOING BUSINESS AS       ║      8     ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ DUNS Number               ║                         ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Addr Line 1               ║ BUSINESS STREET ADDRESS ║      9     ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Addr Line 2               ║                         ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ City                      ║ BUSINESS CITY           ║     10     ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ State                     ║ BUSINESS STATE          ║     11     ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Zip Code                  ║ BUSINESS ZIP            ║     12     ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Website                   ║ WEBSITE                 ║     21     ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Contact Person            ║ NAME                    ║     17     ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Phone                     ║ PHONE                   ║     20     ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Cell Phone                ║                         ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Fax                       ║                         ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Email Address             ║ EMAIL                   ║     19     ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Gender                    ║                         ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Ethnicity                 ║                         ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Given Diversity           ║                         ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Primary Diversity         ║                         ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Other Diversities         ║                         ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Certifying Agency         ║ "NV-GOED"               ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Certification Number      ║                         ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Certification Start Date  ║                         ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Certification Expiry Date ║                         ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Primary NAICS Code        ║                         ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Other NAICS Codes         ║                         ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Business Description      ║                         ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Additional Details 1      ║                         ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Additional Details 2      ║                         ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Additional Details 3      ║                         ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Additional Details 4      ║                         ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Additional Details 5      ║                         ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Additional Details 6      ║                         ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Additional Details 7      ║                         ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Additional Details 8      ║                         ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Additional Details 9      ║                         ║            ║
# ╠═══════════════════════════╬═════════════════════════╬════════════╣
# ║ Additional Details 10     ║                         ║            ║
# ╚═══════════════════════════╩═════════════════════════╩════════════╝

import csv
import logging

from src import custom_logger, prepare_csv_data, empty_dict

log = custom_logger.LogGen.logGen()
log.setLevel(level=logging.DEBUG)

provider = "NV_GOED"
records = []


def processFile(filename):
    log.info(f'Processing {provider}... loading file {filename}')

    with open(filename, encoding="utf8") as f:
        reader = csv.reader(f)
        next(reader, None)

        csv_row_num = 0
        for row in reader:
            if row[0][:2] == '<b':
                continue
            csv_row_num += 1
            dict1 = empty_dict()
            dict1['source'] = provider
            dict1['sequence'] = prepare_csv_data(csv_row_num)
            dict1['company'] = prepare_csv_data(row[6])
            dict1['dba'] = prepare_csv_data(row[7])
            dict1['addr1'] = prepare_csv_data(row[8])
            dict1['city'] = prepare_csv_data(row[9])
            dict1['state'] = prepare_csv_data(row[10])
            dict1['zipcode'] = prepare_csv_data(row[11])
            dict1['website'] = prepare_csv_data(row[20])
            dict1['contact'] = prepare_csv_data(row[16])
            dict1['phone'] = prepare_csv_data(row[19])
            dict1['email'] = prepare_csv_data(row[18])
            dict1['cert_agency'] = 'Nevada Governers Office of Economic Development'
            records.append(dict1)

    return records
