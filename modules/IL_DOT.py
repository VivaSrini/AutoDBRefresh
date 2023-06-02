# Source Info:
#
#  {
#    "Provider": "IL_DOT",
#    "State": "IL",
#    "Name": "Illinois DOT - IDOT",
#    "Title": "UCP Search",
#    "ImportedFileName": "Contrators.csv"
#  }

# Field Mapping:
#
# ╔═══════════════════════════╦══════════════════╦════════════╗
# ║ DEST_COL_NAME             ║ SRC_COL_NAME     ║ SRC_COL_NO ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Sequence                  ║ Program          ║  Generated ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Company Name              ║ Firm             ║      1     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ DBA                       ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ DUNS Number               ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Addr Line 1               ║ Address 1        ║      2     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Addr Line 2               ║ Address 2        ║      3     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ City                      ║ City             ║      4     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ State                     ║ State            ║      5     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Zip Code                  ║ Zip Code         ║      6     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Website                   ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Contact Person            ║ Contact Name     ║      7     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Phone                     ║ Tel              ║      9     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Cell Phone                ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Fax                       ║ Fax              ║      8     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Email Address             ║ EMail            ║     10     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Gender                    ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Ethnicity                 ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Given Diversity           ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Primary Diversity         ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Other Diversities         ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Certifying Agency         ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Certification Number      ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Certification Start Date  ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Certification Expiry Date ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Primary NAICS Code        ║ Specialty, NAICS ║    21-22   ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Other NAICS Codes         ║ Specialty, NAICS ║    21-22   ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Business Description      ║                  ║            ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Additional Details 1      ║ ACDBE?           ║     13     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Additional Details 2      ║ Services         ║    14-20   ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Additional Details 3      ║ County           ║     11     ║
# ╠═══════════════════════════╬══════════════════╬════════════╣
# ║ Additional Details 4      ║ District         ║     12     ║
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

from src import custom_logger, prepare_csv_data, empty_dict, get_primary, get_other

log = custom_logger.LogGen.logGen()
log.setLevel(level=logging.DEBUG)

provider = "IL_DOT"
records = []


def processFile(filename):
    log.info(f'Loaded module {provider}...')

    with open(filename, encoding="utf8") as f:
        reader = csv.reader(f)
        for i in range(2):
            next(reader, None)

        for row_num, row in enumerate(reader):
            dict1 = empty_dict()
            dict1['source'] = provider
            dict1['sequence'] = prepare_csv_data(row_num + 1)
            dict1['company'] = prepare_csv_data(row[0])
            dict1['addr1'] = prepare_csv_data(row[1])
            dict1['addr2'] = prepare_csv_data(row[2])
            dict1['city'] = prepare_csv_data(row[3])
            dict1['state'] = prepare_csv_data(row[4])
            dict1['zipcode'] = prepare_csv_data(row[5])
            dict1['contact'] = prepare_csv_data(row[6])
            dict1['phone'] = prepare_csv_data(row[8])
            dict1['fax'] = prepare_csv_data(row[7])
            dict1['email'] = prepare_csv_data(row[9])
            dict1['pdiverse'] = 'SBE' if prepare_csv_data(row[18]).upper() == 'YES' else ''
            dict1['cert_num'] = prepare_csv_data(row[1])

            spl_naics = ', '.join([row[20] or '', row[21] or ''])
            dict1['pnaics'] = prepare_csv_data(get_primary(spl_naics, pattern=r'[0-9]{6}'))
            dict1['onaics'] = prepare_csv_data(get_other(spl_naics, pattern=r'[0-9]{6}'))

            dict1['addl1'] = prepare_csv_data(get_primary(row[12]), prefix='ACDBE?')

            services = []
            if prepare_csv_data(row[13]).upper() == 'YES': services.append('Retail')
            if prepare_csv_data(row[14]).upper() == 'YES': services.append('Manufacturing')
            if prepare_csv_data(row[15]).upper() == 'YES': services.append('Service')
            if prepare_csv_data(row[16]).upper() == 'YES': services.append('Construction')
            if prepare_csv_data(row[17]).upper() == 'YES': services.append('Construction')
            if prepare_csv_data(row[18]).upper() == 'YES': services.append('Wholesale')
            if prepare_csv_data(row[19]).upper() == 'YES': services.append('Wholesale')
            dict1['addl2'] = prepare_csv_data(','.join(services), prefix='Services')

            dict1['addl3'] = prepare_csv_data(get_primary(row[10]), prefix='County')
            dict1['addl4'] = prepare_csv_data(get_primary(row[11]), prefix='District')

            records.append(dict1)

    return records
