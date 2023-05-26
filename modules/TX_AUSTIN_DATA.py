# Source Info:
#  {
#    "Provider": "TX_AUSTIN_DATA",
#    "State": "PATX",
#    "Name": "Open Data - City of Austin, Texas",
#    "Title": "City of Austin's Open Data Portal",
#    "ImportedFileName": "Current_Small_Business_Enterprise__SBE__Certfied_Vendors.csv"
#  }

# Field Mapping:
#
# ╔═══════════════════════════╦═══════════════════╦════════════╗
# ║ DEST_COL_NAME             ║ SRC_COL_NAME      ║ SRC_COL_NO ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Sequence                  ║ Program           ║  Generated ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Company Name              ║ LEGAL_NAME        ║      2     ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ DBA                       ║ ALIAS             ║      3     ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ DUNS Number               ║                   ║            ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Addr Line 1               ║ STREET_1          ║     10     ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Addr Line 2               ║ STREET_2          ║     11     ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ City                      ║ CITY              ║     12     ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ State                     ║ STATE             ║     13     ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Zip Code                  ║ ZIP               ║     14     ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Website                   ║                   ║            ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Contact Person            ║ PRINCIPLE_CONTACT ║      4     ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Phone                     ║ PHONE             ║      6     ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Cell Phone                ║                   ║            ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Fax                       ║ FAX               ║      8     ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Email Address             ║ EMAIL             ║      5     ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Gender                    ║                   ║            ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Ethnicity                 ║                   ║            ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Given Diversity           ║ "SBE"             ║            ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Primary Diversity         ║                   ║            ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Other Diversities         ║                   ║            ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Certifying Agency         ║ "TX_AUSTIN_DATA"  ║            ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Certification Number      ║ VENDOR_CODE       ║      1     ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Certification Start Date  ║                   ║            ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Certification Expiry Date ║                   ║            ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Primary NAICS Code        ║                   ║            ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Other NAICS Codes         ║                   ║            ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Business Description      ║                   ║            ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Additional Details 1      ║                   ║            ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Additional Details 2      ║                   ║            ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Additional Details 3      ║                   ║            ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Additional Details 4      ║                   ║            ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Additional Details 5      ║                   ║            ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Additional Details 6      ║                   ║            ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Additional Details 7      ║                   ║            ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Additional Details 8      ║                   ║            ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Additional Details 9      ║                   ║            ║
# ╠═══════════════════════════╬═══════════════════╬════════════╣
# ║ Additional Details 10     ║                   ║            ║
# ╚═══════════════════════════╩═══════════════════╩════════════╝
#
import csv
import logging

from src import custom_logger, prepare_csv_data, empty_dict

log = custom_logger.LogGen.logGen()
log.setLevel(level=logging.DEBUG)

provider = "PA_DOT"
records = []


def processFile(filename):
    log.info(f'Processing {provider}... loading file {filename}')

    with open(filename, encoding="utf8") as f:
        reader = csv.reader(f)
        next(reader, None)

        for row_num, row in enumerate(reader):
            dict1 = empty_dict()
            dict1['source'] = provider
            dict1['sequence'] = prepare_csv_data(row_num + 1)
            dict1['company'] = prepare_csv_data(row[1])
            dict1['addr1'] = prepare_csv_data(row[9])
            dict1['addr2'] = prepare_csv_data(row[10])
            dict1['city'] = prepare_csv_data(row[11])
            dict1['state'] = prepare_csv_data(row[12])
            dict1['zipcode'] = prepare_csv_data(row[13])
            dict1['contact'] = prepare_csv_data(row[3])
            dict1['phone'] = prepare_csv_data(row[5])
            dict1['fax'] = prepare_csv_data(row[7])
            dict1['email'] = prepare_csv_data(row[4])
            dict1['gdiverse'] = 'SBE'
            dict1['cert_agency'] = 'Small Business Construction Program (SBCP)'
            dict1['cert_num'] = prepare_csv_data(row[0])
            records.append(dict1)

    return records
