# Source Info:
#
#   {
#     "Provider": "CA_DGS",
#     "State": "CA",
#     "Name": "California eProcure",
#     "Title": "The State of California Certifications",
#     "ImportedFileName": "Certification_Information_YYYY-MM-DD-HH.MM.SS.000000.xls"
#   }

# Summary of process:
#   - use Pandas read_html to import .xls file (file content is a html table!) into a dataframe


# Field Mapping:
#
# ╔════════════════════════════╦═════════════════════╦════════════╗
# ║ DEST_COL_NAME              ║ SRC_COL_NAME        ║ SRC_COL_NO ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Sequence                   ║ Program Generated   ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Company Name               ║ Legal Business Name ║ 2          ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ DBA                        ║ Doing Business As 1 ║ 3,4        ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ DUNS Number                ║                     ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Addr Line 1                ║ Address Line 1      ║ 14         ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Addr Line 2                ║ Address Line 2      ║ 15         ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ City                       ║ City                ║ 17         ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ State                      ║ State               ║ 18         ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Zip Code                   ║ Postal Code         ║ 19         ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Website                    ║ URLID               ║ 11         ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Contact Person             ║ DBE Contact         ║ 9,10       ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Phone                      ║ Telephone           ║ 12         ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Cell Phone                 ║                     ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Fax                        ║ Fax Number          ║ 13         ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Email Address              ║ Email ID            ║ 8          ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Gender                     ║                     ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Ethnicity                  ║                     ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Given Diversity            ║                     ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Primary Diversity          ║ Certification Type  ║ 5          ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Other Diversities          ║ Certification Type  ║ 5          ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Certifying Agency          ║ "Cal eProcure"      ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Certification Number       ║ Certification ID    ║ 1          ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Certification Start Date   ║ Start Date          ║ 6          ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Certification Expiry Date ║ End Date            ║ 7          ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Primary NAICS Code         ║ NAICS               ║ 23         ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Other NAICS Codes          ║ NAICS               ║ 23         ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Business Description       ║                     ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Additional Details 1       ║ Address Line 3      ║ 16         ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Additional Details 2       ║ Country             ║ 20         ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Additional Details 3       ║ UNSPSC              ║ 21         ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Additional Details 4       ║ Keywords            ║ 22         ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Additional Details 5       ║ Service Areas       ║ 24         ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Additional Details 6       ║ License             ║ 25         ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Additional Details 7       ║ Industry Type       ║ 26         ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Additional Details 8       ║                     ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Additional Details 9       ║                     ║            ║
# ╠════════════════════════════╬═════════════════════╬════════════╣
# ║ Additional Details 10      ║                     ║            ║
# ╚════════════════════════════╩═════════════════════╩════════════╝
#

import re
import logging
import pandas as pd
from src import custom_logger, prepare_csv_data, empty_dict

log = custom_logger.LogGen.logGen()
log.setLevel(level=logging.DEBUG)

provider = "CA_DGS"
records = []


def prepare_array_str(array_str):
    if not array_str:
        return ''
    ret_arr = []
    for item in str(array_str).split(','):
        ret_arr.append(prepare_csv_data(item, ssq='Y'))
    return ','.join(ret_arr)


def processFile(filename):
    log.info(f'Processing {provider}... loading file {filename}')

    with open(filename, encoding="utf8") as f:
        html_str = f.read()

    # The following line is to prevent a bug in Pandas
    # https://github.com/pandas-dev/pandas/issues/52619
    # We are forcing all table data to be treated as string by prefixing '

    html_str = re.sub(r'<td>(?=[0-9])', "<td>'", html_str)
    df1 = pd.read_html(html_str)[0]

    idx = 0
    for _idx, row in df1.iterrows():
        dict1 = empty_dict()
        idx += 1
        dict1['source'] = provider
        dict1['sequence'] = prepare_csv_data(idx)
        dict1['company'] = prepare_csv_data(row['Legal Business Name'])
        dict1['dba'] = prepare_csv_data(row['Doing Business As 1'])
        dict1['addr1'] = prepare_csv_data(row['Address Line 1'])
        dict1['addr2'] = prepare_csv_data(row['Address Line 2'])
        dict1['city'] = prepare_csv_data(row['City'])
        dict1['state'] = prepare_csv_data(row['State'])
        dict1['zipcode'] = prepare_csv_data(row['Postal Code'], ssq='Y')
        dict1['website'] = prepare_csv_data(row['URLID'])
        dict1['contact'] = prepare_csv_data(row['First Name']) + ' ' + prepare_csv_data(row['Last Name'])
        dict1['phone'] = prepare_csv_data(row['Telephone'], ssq='Y')
        dict1['fax'] = prepare_csv_data(row['Fax Number'])
        dict1['email'] = prepare_csv_data(row['Email ID'])
        dict1['pdiverse'] = prepare_csv_data(row['Certification Type'], pattern=r'^([^,]+)')
        dict1['odiverse'] = prepare_csv_data(row['Certification Type'], pattern=r'(?<=,).*$')
        dict1['cert_agency'] = 'CA eProcure'
        dict1['cert_num'] = prepare_csv_data(row['Certification ID'], ssq='Y')
        dict1['cert_start'] = prepare_csv_data(row['Start Date'], ssq='Y')
        dict1['cert_expiry'] = prepare_csv_data(row['End Date'], ssq='Y')
        dict1['pnaics'] = prepare_csv_data(prepare_array_str(row['NAICS']), pattern=r'^([^,]+)')
        dict1['onaics'] = prepare_csv_data(prepare_array_str(row['NAICS']), pattern=r'(?<=,).*$')
        dict1['addl1'] = prepare_csv_data(row['Address Line 3'], prefix='Addr_Line_3')
        dict1['addl2'] = prepare_csv_data(row['Country'], prefix='"Country')
        dict1['addl3'] = prepare_csv_data(prepare_array_str(row['UNSPSC']), prefix='"UNSPSC Codes')
        dict1['addl4'] = prepare_csv_data(row['Keywords'], prefix='"Keywords')
        dict1['addl5'] = prepare_csv_data(prepare_array_str(row['Service Areas']), prefix='Service Area(s)')
        dict1['addl6'] = prepare_csv_data(prepare_array_str(row['License']), prefix='"License(s)')
        dict1['addl7'] = prepare_csv_data(prepare_array_str(row['Industry Type']), prefix='"Industry Type')
        records.append(dict1)

    return records
