# Source Info:
#  {
#    "Provider": "PennDOT",
#    "State": "PA",
#    "Name": "Pennsylvania Department of Transportation",
#    "Title": "Small Business Enterprise",
#    "ImportedFileName": "Data.csv"
#  }

# Field Mapping:
#
# ╔═══════════════════════════╦════════════════════╦════════════╗
# ║ DEST_COL_NAME             ║ SRC_COL_NAME       ║ SRC_COL_NO ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Sequence                  ║ Program            ║  Generated ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Company Name              ║ Firm Name          ║      2     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ DBA                       ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ DUNS Number               ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Addr Line 1               ║ Physical Address   ║      6     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Addr Line 2               ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ City                      ║ Physical Address   ║      6     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ State                     ║ Physical Address   ║      6     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Zip Code                  ║ Physical Address   ║      6     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Website                   ║ Website            ║     11     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Contact Person            ║ Owners             ║      3     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Phone                     ║ Phone Number       ║      8     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Cell Phone                ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Fax                       ║ Fax Number         ║      9     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Email Address             ║ Email Address      ║     10     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Gender                    ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Ethnicity                 ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Given Diversity           ║ Certification Type ║      1     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Primary Diversity         ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Other Diversities         ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Certifying Agency         ║ "PA_DOT"           ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Certification Number      ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Certification Start Date  ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Certification Expiry Date ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Primary NAICS Code        ║ NAICS Codes        ║      5     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Other NAICS Codes         ║ NAICS Codes        ║      5     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Business Description      ║ Work Description   ║      4     ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Additional Details 1      ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Additional Details 2      ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Additional Details 3      ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Additional Details 4      ║                    ║            ║
# ╠═══════════════════════════╬════════════════════╬════════════╣
# ║ Additional Details 5      ║                    ║            ║
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

from src import custom_logger, prepare_csv_data, empty_dict, get_primary, get_other

log = custom_logger.LogGen.logGen()
log.setLevel(level=logging.DEBUG)

provider = "PA_DOT"
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
            addr = prepare_csv_data(row[5])
            addr_array = addr.split('\n')
            len_addr_array = len(addr_array)
            dict1['addr1'] = addr_array[0] if len_addr_array == 2 else addr_array[0] + ' ' + addr_array[1]
            dict1['city'] = prepare_csv_data(addr_array[len_addr_array-1], pattern='(^[^,]*)')
            dict1['state'] = prepare_csv_data(addr_array[len_addr_array-1], pattern='(.{2}) [0-9-]*$')
            dict1['zipcode'] = prepare_csv_data(addr_array[len_addr_array-1], pattern='([0-9-]*)$')
            dict1['website'] = prepare_csv_data(row[10])
            dict1['contact'] = prepare_csv_data(row[3])
            dict1['phone'] = prepare_csv_data(row[7])
            dict1['fax'] = prepare_csv_data(row[8])
            dict1['email'] = prepare_csv_data(row[9])
            dict1['gdiverse'] = prepare_csv_data(row[0])
            dict1['gdiverse'] = prepare_csv_data(row[0])
            dict1['cert_agency'] = 'PA DOT Small Business Enterprise (SBE)'
            dict1['pnaics'] = prepare_csv_data(get_primary(row[4]))
            dict1['onaics'] = prepare_csv_data(get_other(row[4]))
            dict1['biz_desc'] = prepare_csv_data(get_primary(row[3]))
            records.append(dict1)

    return records
