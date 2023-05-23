# Source Info:
#  {
#    "Provider": "WA_WEBS",
#    "State": "WA",
#    "Name": "Washington Electronic Business Solution",
#    "Title": "Washington Electronic Business Solution",
#    "ImportedFileName": "VendorListMM_DD_YYYY HH_MM_SS.csv"
#  }

# Field Mapping:
#

# ╔═══════════════════════════╦══════════════╦════════════╗
# ║ DEST_COL_NAME             ║ SRC_COL_NAME ║ SRC_COL_NO ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Sequence                  ║ Program      ║  Generated ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Company Name              ║ CompanyName  ║      1     ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ DBA                       ║ DBAName      ║      2     ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ DUNS Number               ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Addr Line 1               ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Addr Line 2               ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ City                      ║ City         ║      4     ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ State                     ║ State        ║      5     ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Zip Code                  ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Website                   ║ WebAddress   ║      6     ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Contact Person            ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Phone                     ║ Phone        ║      8     ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Cell Phone                ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Fax                       ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Email Address             ║ EmailAddress ║      3     ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Gender                    ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Ethnicity                 ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Given Diversity           ║ Status       ║      7     ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Primary Diversity         ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Other Diversities         ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Certifying Agency         ║ "WA_WEBS"    ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Certification Number      ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Certification Start Date  ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Certification Expiry Date ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Primary NAICS Code        ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Other NAICS Codes         ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Business Description      ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Additional Details 1      ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Additional Details 2      ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Additional Details 3      ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Additional Details 4      ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Additional Details 5      ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Additional Details 6      ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Additional Details 7      ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Additional Details 8      ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Additional Details 9      ║              ║            ║
# ╠═══════════════════════════╬══════════════╬════════════╣
# ║ Additional Details 10     ║              ║            ║
# ╚═══════════════════════════╩══════════════╩════════════╝
#
import csv
import logging

from src import custom_logger, prepare_csv_data, empty_dict

log = custom_logger.LogGen.logGen()
log.setLevel(level=logging.DEBUG)

provider = "WA_WEBS"
records = []


def processFile(filename):
    log.info(f'Processing {provider}... loading file {filename}')

    with open(filename, encoding="utf8") as f:
        reader = csv.reader(f)
        # Skip first 13 rows
        for _i in range(13):
            next(reader, None)

        for row_num, row in enumerate(reader):
            dict1 = empty_dict()
            dict1['sequence'] = prepare_csv_data(row_num + 1)
            dict1['company'] = prepare_csv_data(row[0])
            dict1['dba'] = prepare_csv_data(row[1])
            dict1['city'] = prepare_csv_data(row[3])
            dict1['state'] = prepare_csv_data(row[4])
            dict1['website'] = prepare_csv_data(row[5])
            dict1['phone'] = prepare_csv_data(row[7])
            dict1['email'] = prepare_csv_data(row[2])
            dict1['gdiverse'] = prepare_csv_data(row[6])
            dict1['cert_agency'] = 'Washington Electronic Business Solution (WEBS)'
            dict1['cert_num'] = prepare_csv_data(row[0])
            records.append(dict1)

    return records
