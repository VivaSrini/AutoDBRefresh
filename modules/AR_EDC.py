# Source Info:
#  {
#    "Provider": "AR_EDC",
#    "State": "AR",
#    "Name": "Arkansas Economic Development Commission - AEDC",
#    "Title": "Directory",
#    "ImportedFileName": "women-minority-owned-business.csv"
#  }

# ╔════════════════════════════╦═════════════════════╦════════════╗
# ║ DEST_COL_NAME              ║ SRC_COL_NAME        ║ SRC_COL_NO ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Sequence                   ║ Program             ║  Generated ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Company Name               ║ CompanyName         ║      1     ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ DBA                        ║                     ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ DUNS Number                ║                     ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Addr Line 1                ║ Street              ║      4     ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Addr Line 2                ║                     ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ City                       ║ City                ║      5     ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ State                      ║ StateCode           ║      6     ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Zip Code                   ║ Zip                 ║      7     ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Website                    ║ Website             ║     19     ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Contact Person             ║ ContactFirstName    ║     12     ║
# ║                            ║ ContactLastName     ║     13     ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Phone                      ║ Phone               ║      3     ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Cell Phone                 ║                     ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Fax                        ║                     ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Email Address              ║ ContactEmail        ║     16     ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Gender                     ║                     ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Ethnicity                  ║                     ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Given Diversity            ║ VendorCategory      ║      8     ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Primary Diversity          ║ BusinessDesignation ║     18     ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Other Diversities          ║ BusinessDesignation ║     18     ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Certifying Agency          ║ "AEDC"              ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Certification Number       ║ CertificationNumber ║      9     ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Certification Start Date   ║                     ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Certification Expiry Date  ║                     ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Primary NAICS Code         ║ NAICS               ║     10     ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Other NAICS Codes          ║ NAICS               ║     10     ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Business Description       ║ BusinessDecsription ║      2     ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Additional Details 1       ║ AasisVendorNumber   ║     11     ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Additional Details 2       ║ ContactTitle        ║     14     ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Additional Details 3       ║ County              ║     17     ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Additional Details 4       ║                     ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Additional Details 5       ║                     ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Additional Details 6       ║                     ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Additional Details 7       ║                     ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Additional Details 8       ║                     ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Additional Details 9       ║                     ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Additional Details 10      ║                     ║            ║
# ╚════════════════════════════╩═════════════════════╩════════════╝

import csv
import logging

from src import custom_logger, empty_dict, prepare_csv_data, get_primary, get_other

log = custom_logger.LogGen.logGen()
log.setLevel(level=logging.DEBUG)

provider = "AR_EDC"
records = []


def processFile(filename):
    log.info(f'Loaded module {provider}...')

    with open(filename, encoding="utf8") as f:
        reader = csv.reader(f)
        next(reader, None)

        for row_num, row in enumerate(reader):
            dict1 = empty_dict()
            dict1['source'] = provider
            dict1['sequence'] = prepare_csv_data(row_num + 1)
            dict1['company'] = prepare_csv_data(row[1])
            dict1['addr1'] = prepare_csv_data(row[4])
            dict1['city'] = prepare_csv_data(row[5])
            dict1['state'] = prepare_csv_data(row[6])
            dict1['zipcode'] = prepare_csv_data(row[7])
            dict1['website'] = prepare_csv_data(row[19])
            dict1['contact'] = prepare_csv_data(row[12]) + ' ' + prepare_csv_data(row[13])
            dict1['phone'] = prepare_csv_data(row[3])
            dict1['email'] = prepare_csv_data(row[16])
            dict1['gdiverse'] = prepare_csv_data(row[8])
            dict1['pdiverse'] = prepare_csv_data(get_primary(row[18]))
            dict1['odiverse'] = prepare_csv_data(get_other(row[18]))
            dict1['cert_agency'] = 'Arkansas Economic Development Commission'
            dict1['cert_num'] = prepare_csv_data(row[9])
            dict1['pnaics'] = prepare_csv_data(get_primary(row[10]))
            dict1['onaics'] = prepare_csv_data(get_other(row[10]))
            dict1['biz_desc'] = prepare_csv_data(row[9])
            dict1['addl1'] = prepare_csv_data(row[11], prefix='Aasis Vendor Number')
            dict1['addl2'] = prepare_csv_data(row[14], prefix='Job Title')
            dict1['addl3'] = prepare_csv_data(row[17], prefix='County')
            records.append(dict1)
            row_num += 1
    
        return records
