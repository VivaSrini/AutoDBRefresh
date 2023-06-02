import re
import pandas as pd


# ssq = Strip Single Quotes. Sometimes HTML tables are prefixed with single quote
# to force excel conversion to string. We are converting everything into string
# due to the pandas import bug workaround
def prepare_csv_data(data, prefix=None, pattern=None, ssq=None):
    data = str(data or '').strip()
    if not data or data == 'nan':
        return ''
    data = data[:len(data) - 1] if data[len(data) - 1] == ',' else data
    if ssq and ssq.lower() == 'y':
        data = data[1:] if data[0] == '\'' else data
        data = data[:len(data) - 1] if data and data[len(data) - 1] == '\'' else data
    if pattern:
        data = re.search(pattern, data)
        data = data.group(0) if data else ''
    if prefix:
        data = prefix + ': ' + data
    return data.replace('"', '""')


def get_csv_header():
    return \
        f'"Source",' \
        f'"Sequence",' \
        f'"Company_Name",' \
        f'"DBA",' \
        f'"DUNS_Number",' \
        f'"Addr_Line_1",' \
        f'"Addr_Line_2",' \
        f'"City",' \
        f'"State",' \
        f'"Zip_Code",' \
        f'"Website_URL",' \
        f'"Contact_Person",' \
        f'"Phone",' \
        f'"Cell_Phone",' \
        f'"Fax",' \
        f'"Email_Address",' \
        f'"Gender",' \
        f'"Ethnicity",' \
        f'"Given_Diversity",' \
        f'"Primary_Diversity",' \
        f'"Other_Diversities",' \
        f'"Certifying_Agency",' \
        f'"Certification_Number",' \
        f'"Certification_Start_Date",' \
        f'"Certification_Expiry_Date",' \
        f'"Primary_NAICS_Code",' \
        f'"Other_NAICS_Codes",' \
        f'"Business_Description",' \
        f'"Additional_Details_1",' \
        f'"Additional_Details_2",' \
        f'"Additional_Details_3",' \
        f'"Additional_Details_4",' \
        f'"Additional_Details_5",' \
        f'"Additional_Details_6",' \
        f'"Additional_Details_7",' \
        f'"Additional_Details_8",' \
        f'"Additional_Details_9",' \
        f'"Additional_Details_10"\n'


def empty_dict():
    dict1: dict = {key: value for key, value in []}
    dict1['source'] = ''
    dict1['sequence'] = ''
    dict1['company'] = ''
    dict1['dba'] = ''
    dict1['duns'] = ''
    dict1['addr1'] = ''
    dict1['addr2'] = ''
    dict1['city'] = ''
    dict1['state'] = ''
    dict1['zipcode'] = ''
    dict1['website'] = ''
    dict1['contact'] = ''
    dict1['phone'] = ''
    dict1['cellphone'] = ''
    dict1['fax'] = ''
    dict1['email'] = ''
    dict1['gender'] = ''
    dict1['ethnicity'] = ''
    dict1['gdiverse'] = ''
    dict1['pdiverse'] = ''
    dict1['odiverse'] = ''
    dict1['cert_agency'] = ''
    dict1['cert_num'] = ''
    dict1['cert_start'] = ''
    dict1['cert_expiry'] = ''
    dict1['pnaics'] = ''
    dict1['onaics'] = ''
    dict1['biz_desc'] = ''
    dict1['addl1'] = ''
    dict1['addl2'] = ''
    dict1['addl3'] = ''
    dict1['addl4'] = ''
    dict1['addl5'] = ''
    dict1['addl6'] = ''
    dict1['addl7'] = ''
    dict1['addl8'] = ''
    dict1['addl9'] = ''
    dict1['addl10'] = ''
    return dict1


def dict_to_csv(data_rec):
    csv_rec = ''

    # Column #0 - Provider
    csv_rec += '"' + data_rec['source'] + '",'

    # Column #1 - Sequence Number
    csv_rec += '"' + data_rec['sequence'] + '",'

    # Column #2 - Company Name
    csv_rec += '"' + data_rec['company'] + '",'

    # Column #4 - DBA
    csv_rec += '"' + data_rec['dba'] + '",'

    # Column #5 - DUNS Number
    csv_rec += '"' + data_rec['duns'] + '",'

    # Column #6 - Address Line 1
    csv_rec += '"' + data_rec['addr1'] + '",'

    # Column #7 - Address Line 2
    csv_rec += '"' + data_rec['addr2'] + '",'

    # Column #8 - City
    csv_rec += '"' + data_rec['city'] + '",'

    # Column #9 - State
    csv_rec += '"' + data_rec['state'] + '",'

    # Column #10 - Zip Code
    csv_rec += '"' + data_rec['zipcode'] + '",'

    # Column #11 - Website URL
    csv_rec += '"' + data_rec['website'] + '",'

    # Column #12 - Contact Person
    csv_rec += '"' + data_rec['contact'] + '",'

    # Column #13 - Phone
    csv_rec += '"' + data_rec['phone'] + '",'

    # Column #14 - Cell Phone
    csv_rec += '"' + data_rec['cellphone'] + '",'

    # Column #15 - Fax
    csv_rec += '"' + data_rec['fax'] + '",'

    # Column #16 - Email Address
    csv_rec += '"' + data_rec['email'] + '",'

    # Column #17 - Gender
    csv_rec += '"' + data_rec['gender'] + '",'

    # Column #18 - Ethnicity
    csv_rec += '"' + data_rec['ethnicity'] + '",'

    # Column #19 - Given Diversity
    csv_rec += '"' + data_rec['gdiverse'] + '",'

    # Column #20 - Primary Diversity
    csv_rec += '"' + data_rec['pdiverse'] + '",'

    # Column #21 - Other Diversities
    csv_rec += '"' + data_rec['odiverse'] + '",'

    # Column #22 - Certifying Agency
    csv_rec += '"' + data_rec['cert_agency'] + '",'

    # Column #23 - Certification Number
    csv_rec += '"' + data_rec['cert_num'] + '",'

    # Column #24 - Certification Start Date
    csv_rec += '"' + data_rec['cert_start'] + '",'

    # Column #25 - Certification Expiry Date
    csv_rec += '"' + data_rec['cert_expiry'] + '",'

    # Column #26 - Primary NAICS Code
    csv_rec += '"' + data_rec['pnaics'] + '",'

    # Column #27 - Other NAICS Codes
    csv_rec += '"' + data_rec['onaics'] + '",'

    # Column #28 - Business Description
    csv_rec += '"' + data_rec['biz_desc'] + '",'

    # Column #29 - Additional Details 1
    csv_rec += '"' + data_rec['addl1'] + '",'

    # Column #30 - Additional Details 2
    csv_rec += '"' + data_rec['addl2'] + '",'

    # Column #31 - Additional Details 3
    csv_rec += '"' + data_rec['addl3'] + '",'

    # Column #32 - Additional Details 4
    csv_rec += '"' + data_rec['addl4'] + '",'

    # Column #33 - Additional Details 5
    csv_rec += '"' + data_rec['addl5'] + '",'

    # Column #34 - Additional Details 6
    csv_rec += '"' + data_rec['addl6'] + '",'

    # Column #35 - Additional Details 7
    csv_rec += '"' + data_rec['addl7'] + '",'

    # Column #36 - Additional Details 8
    csv_rec += '"' + data_rec['addl8'] + '",'

    # Column #37 - Additional Details 9
    csv_rec += '"' + data_rec['addl9'] + '",'

    # Column #38 - Additional Details 10
    csv_rec += '"' + data_rec['addl10'] + '"\n'

    return csv_rec


def dedup_csv(filename, col_array):
    df = pd.read_csv(filename)
    for col in col_array:
        df.pop(col)
    df.drop_duplicates(inplace=True)
    df.to_csv(filename, index=False)


def get_primary(data_list, separator=',', pattern=None):
    list1 = list([item for item in str(data_list or '').split(separator) if item])
    primary = list1[0] if list1 else ''

    if pattern:
        primary = re.search(pattern, primary)
        return primary.group(0) if primary else ''
    return primary


def get_other(data_list, separator=',', pattern=None):
    return_array = []
    list1 = list([item for item in str(data_list or '').split(separator) if item])
    other_array = list1[1:] if list1 else ''

    if pattern:
        for item in other_array:
            item = re.search(pattern, item)
            if item:
                return_array.append(item.group(0))
        return ','.join(return_array)
    return ','.join(other_array)


# Just Q&D, no controls yet...
def format_phone(country_code='', area_code='', number='', ext='', fmt='2'):
    ret_str = ''
    match fmt:
        case '1':
            ret_str = f'+{country_code} ({area_code}) {number[:3]}-{number[-4:]} x{ext}' if ext \
                else f'+{country_code} ({area_code}) {number[:3]}-{number[-4:]}'
        case '2':
            ret_str = f'({area_code}) {number[:3]}-{number[-4:]} x{ext}' if ext \
                else f'({area_code}) {number[:3]}-{number[-4:]}'

    return ret_str


def trim_file_header_rows(file_name, num_lines):
    with open(file_name, encoding='utf-8') as f:
        lines = f.readlines()

    with open(file_name, encoding='utf-8', mode='w') as f:
        f.writelines(lines[num_lines:])
