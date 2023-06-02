# Source Info:
#
#  {
#    "Provider": "DE_DATA_SBE",
#    "State": "DE",
#    "Name": "Delaware Open Data - Small Business",
#    "Title": "Certified Vendors - Small Business Focus Program",
#    "ImportedFileName": "Certified_Vendors_-_Small_Business_Focus_Program.csv"
#  }

# Field Mapping:
#
# ╔═══════════════════════════╦═════════════════╦════════════╗
# ║ DEST_COL_NAME             ║ SRC_COL_NAME    ║ SRC_COL_NO ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Sequence                  ║ Program         ║  Generated ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Company Name              ║ Company Name    ║      1     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ DBA                       ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ DUNS Number               ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Addr Line 1               ║ Address 1       ║      4     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Addr Line 2               ║ Address 2       ║      5     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ City                      ║ City            ║      6     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ State                     ║ State           ║      7     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Zip Code                  ║ Zip Code        ║      8     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Website                   ║ WebSite         ║     11     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Contact Person            ║ Contact Name    ║      3     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Phone                     ║ Tel             ║      9     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Cell Phone                ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Fax                       ║ Fax             ║     10     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Email Address             ║ EMail           ║     12     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Gender                    ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Ethnicity                 ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Given Diversity           ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Primary Diversity         ║ Small Business  ║     19     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Other Diversities         ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Certifying Agency         ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Certification Number      ║ SBFCertNum      ║      2     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Certification Start Date  ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Certification Expiry Date ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Primary NAICS Code        ║ NAICSCode1      ║     21     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Other NAICS Codes         ║ NAICSCode2-31   ║    22-60   ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Business Description      ║ Job Description ║     20     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Additional Details 1      ║ Services        ║    13-18   ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Additional Details 2      ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Additional Details 3      ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Additional Details 4      ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Additional Details 5      ║                 ║            ║
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
#
import csv
import logging

from src import custom_logger, prepare_csv_data, empty_dict, get_primary

log = custom_logger.LogGen.logGen()
log.setLevel(level=logging.DEBUG)

provider = "DE_DATA_SBE"
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
            dict1['company'] = prepare_csv_data(row[0])
            dict1['addr1'] = prepare_csv_data(row[3])
            dict1['addr2'] = prepare_csv_data(row[4])
            dict1['city'] = prepare_csv_data(row[5])
            dict1['state'] = prepare_csv_data(row[6])
            dict1['zipcode'] = prepare_csv_data(row[7])
            dict1['website'] = prepare_csv_data(row[10])
            dict1['contact'] = prepare_csv_data(row[2])
            dict1['phone'] = prepare_csv_data(row[8]).replace(',', '')
            dict1['fax'] = prepare_csv_data(row[9]).replace(',', '')
            dict1['email'] = prepare_csv_data(row[11])
            dict1['pdiverse'] = 'SBE' if prepare_csv_data(row[18]).upper() == 'YES' else ''
            dict1['cert_num'] = prepare_csv_data(row[1])
            dict1['pnaics'] = prepare_csv_data(row[20])
            dict1['onaics'] = str(', '.join([x for x in row[21:59] if int(x)]))
            dict1['biz_desc'] = prepare_csv_data(get_primary(row[19]))

            services = []
            if prepare_csv_data(row[12]).upper() == 'YES': services.append('Wholesale')
            if prepare_csv_data(row[13]).upper() == 'YES': services.append('Retail')
            if prepare_csv_data(row[14]).upper() == 'YES': services.append('Manufacturing')
            if prepare_csv_data(row[15]).upper() == 'YES': services.append('Service')
            if prepare_csv_data(row[16]).upper() == 'YES': services.append('Construction')
            if prepare_csv_data(row[17]).upper() == 'YES': services.append('Architecture and Engg. Services')
            dict1['addl1'] = prepare_csv_data(','.join(services), prefix='Services')

            records.append(dict1)

    return records
