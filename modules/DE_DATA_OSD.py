# Source Info:
#
#  {
#    "Provider": "DE_DATA_OSD",
#    "State": "DE",
#    "Name": "Delaware Open Data - Office of Supplier Diversity",
#    "Title": "Certified Vendors - Office of Supplier Diversity",
#    "ImportedFileName": "Certified_Vendors_-_Office_of_Supplier_Diversity.csv"
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
# ║ Gender                    ║ Woman           ║     44     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Ethnicity                 ║                 ║    37-43   ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Given Diversity           ║                 ║    30-36   ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Primary Diversity         ║ Disabled        ║     45     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Other Diversities         ║ Veteran         ║     46     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Certifying Agency         ║                 ║    21-29   ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Certification Number      ║ OSDCertNum      ║      2     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Certification Start Date  ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Certification Expiry Date ║                 ║            ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Primary NAICS Code        ║ NAICSCode1      ║     48     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Other NAICS Codes         ║ NAICSCode2-31   ║    49-78   ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Business Description      ║ Job Description ║     47     ║
# ╠═══════════════════════════╬═════════════════╬════════════╣
# ║ Additional Details 1      ║ Services        ║    13-20   ║
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

provider = "DE_DATA_OSD"
records = []


def processFile(filename):
    log.info(f'Processing {provider}... loading file {filename}')

    with open(filename, encoding="utf8") as f:
        reader = csv.reader(f)
        next(reader, None)

        for row_num, row in enumerate(reader):
            dict1 = empty_dict()
            dict1['sequence'] = prepare_csv_data(row_num + 1)
            dict1['company'] = prepare_csv_data(row[0])
            dict1['addr1'] = prepare_csv_data(row[3])
            dict1['addr2'] = prepare_csv_data(row[4])
            dict1['city'] = prepare_csv_data(row[5])
            dict1['state'] = prepare_csv_data(row[6])
            dict1['zipcode'] = prepare_csv_data(row[7])
            dict1['website'] = prepare_csv_data(row[10])
            dict1['contact'] = prepare_csv_data(row[2])
            dict1['phone'] = prepare_csv_data(row[8])
            dict1['fax'] = prepare_csv_data(row[9])
            dict1['email'] = prepare_csv_data(row[11])
            dict1['gender'] = 'Woman' if prepare_csv_data(row[43]).upper() == 'YES' else ''

            ethnicity = []
            if prepare_csv_data(row[36]).upper() == 'YES': ethnicity.append('African')
            if prepare_csv_data(row[37]).upper() == 'YES': ethnicity.append('Asian')
            if prepare_csv_data(row[38]).upper() == 'YES': ethnicity.append('SubAsian')
            if prepare_csv_data(row[39]).upper() == 'YES': ethnicity.append('Hispanic')
            if prepare_csv_data(row[40]).upper() == 'YES': ethnicity.append('NativeAmerican')
            if prepare_csv_data(row[41]).upper() == 'YES': ethnicity.append('White')
            if prepare_csv_data(row[42]).upper() == 'YES': ethnicity.append('Other')
            dict1['ethnicity'] = ','.join(ethnicity)

            diversity = []
            if prepare_csv_data(row[29]).upper() == 'YES': diversity.append('MBE')
            if prepare_csv_data(row[30]).upper() == 'YES': diversity.append('WBE')
            if prepare_csv_data(row[31]).upper() == 'YES': diversity.append('8(a)')
            if prepare_csv_data(row[32]).upper() == 'YES': diversity.append('Foreign State')
            if prepare_csv_data(row[33]).upper() == 'YES': diversity.append('VOBE')
            if prepare_csv_data(row[34]).upper() == 'YES': diversity.append('SDVOBE')
            if prepare_csv_data(row[35]).upper() == 'YES': diversity.append('IWDBE')
            dict1['gdiverse'] = ','.join(diversity)

            diversity2 = []
            if prepare_csv_data(row[44]).upper() == 'YES': diversity2.append('Disabled')
            if prepare_csv_data(row[45]).upper() == 'YES': diversity2.append('Veteran')
            dict1['odiverse'] = ','.join(diversity2)

            cert_agency = []
            if prepare_csv_data(row[20]).upper() == 'YES': diversity2.append('DelDOT')
            if prepare_csv_data(row[21]).upper() == 'YES': diversity2.append('MD DOT')
            if prepare_csv_data(row[22]).upper() == 'YES': diversity2.append('NMSDC')
            if prepare_csv_data(row[23]).upper() == 'YES': diversity2.append('PAUCP')
            if prepare_csv_data(row[24]).upper() == 'YES': diversity2.append('WBENC')
            if prepare_csv_data(row[25]).upper() == 'YES': diversity2.append('PAMWB')
            if prepare_csv_data(row[26]).upper() == 'YES': diversity2.append('WilmCity')
            if prepare_csv_data(row[27]).upper() == 'YES': diversity2.append('NJMWB')
            if prepare_csv_data(row[28]).upper() == 'YES': diversity2.append('SAM')
            dict1['cert_agency'] = ','.join(cert_agency)

            dict1['cert_num'] = prepare_csv_data(row[1])
            dict1['pnaics'] = prepare_csv_data(row[47])
            dict1['onaics'] = str(', '.join([x for x in row[48:78] if int(x)]))
            dict1['biz_desc'] = prepare_csv_data(get_primary(row[46]))

            services = []
            if prepare_csv_data(row[20]).upper() == 'YES': services.append('Building Trade')
            if prepare_csv_data(row[20]).upper() == 'YES': services.append('Consultant')
            if prepare_csv_data(row[20]).upper() == 'YES': services.append('General Services')
            if prepare_csv_data(row[20]).upper() == 'YES': services.append('License Professional')
            if prepare_csv_data(row[20]).upper() == 'YES': services.append('Manufacture')
            if prepare_csv_data(row[20]).upper() == 'YES': services.append('Supplier')
            if prepare_csv_data(row[20]).upper() == 'YES': services.append('Highway Construction')
            if prepare_csv_data(row[20]).upper() == 'YES': services.append('Other Services')
            dict1['addl1'] = prepare_csv_data(','.join(services), prefix='Services')

            records.append(dict1)

    return records
