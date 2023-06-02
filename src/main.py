import datetime
import glob
import json
import logging
import shutil
import os
import time
import xlsxwriter
import importlib

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import custom_logger
from utilities import dict_to_csv, get_csv_header


# Create a custom Error to drop out of loop
class NextItem(Exception):
    def __init__(self, message):
        self.message = message


# Initialize logging
log = custom_logger.LogGen.logGen()
log.setLevel(level=logging.DEBUG)
log.info('Starting AutoDBRefresh Process...')
shutil.copyfile(custom_logger.BASE_INPUT_JSON, custom_logger.RUN_INPUT_JSON)

# Setup Excel Output
wb = xlsxwriter.Workbook(custom_logger.XL_FILE)
ws = wb.add_worksheet(custom_logger.XL_SHEET)
header_format = wb.add_format({'bold': True, 'bg_color': '#AAAAAA'})
success_format = wb.add_format({'font_color': '#006100', 'bg_color': '#C6EFCE'})
failed_format = wb.add_format({'font_color': '#9C0006', 'bg_color': '#FFC7CE'})
skipped_format = wb.add_format({'font_color': '#9C6500', 'bg_color': '#FFEB9C'})
ws.write('A1', "SNo", header_format)
ws.write('B1', "Provider", header_format)
ws.write('C1', "Download", header_format)
ws.write('D1', "Convert", header_format)
ws.write('E1', "Extn", header_format)
ws.write('F1', "Downloaded file", header_format)
ws.set_column('A:A', 4)
ws.set_column('B:B', 16)
ws.set_column('C:C', 11)
ws.set_column('D:D', 11)
ws.set_column('E:E', 4)
ws.set_column('F:F', 105)
ws.set_column('G:XFD', None, None, {'hidden': 1})

# Setup Browser options
options = Options()
options.add_argument("--headless=new")
options.add_argument("--force-device-scale-factor=0.5")
options.add_argument("--high-dpi-support=1")
options.add_argument("--disable-notifications")
options.add_argument("--start-fullscreen")
# log.info(f'Starting chrome with option < --profile-directory=\"{custom_logger.PROFILE}\" >')
# options.add_argument(f"--profile-directory=\"{custom_logger.PROFILE}\"")
# user_data_dir = r"C:\Users\srinivasg\AppData\Local\Google\Chrome\User Data\Profile 5"
# options.add_argument(f"--user-data-dir={user_data_dir}")

prefs = {
    'profile.default_content_setting_values.automatic_downloads': 1,
    'download.prompt_for_download': False,
    'plugins.always_open_pdf_externally': True,
    'plugins.plugins_list': [{'enabled': False, 'name': 'Chrome PDF Viewer'}],
    'download.default_directory': os.path.abspath(custom_logger.TEMP_DOWNLOAD_PATH),
    'download.extensions_to_open': 'applications/pdf'
}

options.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(options=options)
actions = ActionChains(browser)
params = {'behavior': 'allow', 'downloadPath': os.path.abspath(custom_logger.TEMP_DOWNLOAD_PATH)}
browser.execute_cdp_cmd('Page.setDownloadBehavior', params)
browser.maximize_window()

mods = {}
wrote_header = False


# Function: Take Screenshot
def take_scr_shot(prefix):
    fname = f'{prefix}_{datetime.datetime.now().strftime("%Y%m%d-%H%M%S")}.PNG'
    browser.save_screenshot(os.path.join(custom_logger.LOG_PATH, fname))
    log.info(f'Screenshot saved: {fname}')


# Update Excel sheet with status
def upd_XL_stat(row, provider="", download="", convert="", fName=""):
    bg_formats = {'': '', 'Success': success_format, 'Failed': failed_format, 'Skipped': skipped_format}
    if row: ws.write(row, 0, row)
    if provider: ws.write(row, 1, provider)
    if download: ws.write(row, 2, download, bg_formats[download])
    if convert: ws.write(row, 3, convert, bg_formats[convert])
    if fName: ws.write(row, 4, os.path.splitext(fName)[1][1:] if download == "Success" else '')
    if fName: ws.write(row, 5, fName)


def download_source(index, source):
    file = 'ERROR: couldn\'t download'

    # If Download set to 'No' skip
    if not source["Download"].lower()[0] == 'y':
        log.info(f'Skipping download for {source["Provider"]}...')
        upd_XL_stat(row=index + 1, provider=source["Provider"], download="Skipped", fName="*Download Skipped*")
        return

    try:
        # For each item, get website
        log.info(f'Fetching website: {source["Website"]}')
        try:
            browser.get(source["Website"])
        except WebDriverException as _e:
            err_msg = f'UNABLE TO CONNECT TO SOURCE!'
            log.error(err_msg)
            # log.exception(e)
            take_scr_shot('ConnectionErr')
            upd_XL_stat(row=index + 1, provider=source["Provider"], download="Failed", fName=err_msg)
            raise NextItem(err_msg)

        # Read steps to be performed
        num_steps = len(source['Steps'])
        if not num_steps:
            log.info(f'item #{index + 1}/{num_items} No steps direct download')

        # reset switched_tab flag
        switched_tab = False

        # For each step, read step configuration
        for stepnum, step in enumerate(source['Steps']):
            elXPath = step['XPath']
            elName = step['Name']
            elAction = step['Action']
            elData = step['Data']

            log.info(f'Item# {index + 1}/{num_items}. Step# {stepnum + 1}/{num_steps}')

            # Take screen shot and go to next step
            if elAction == 'Screenshot':
                log.info(f'  Taking screenshot...')
                take_scr_shot('Screenshot')
                continue

            # Wait for n secs and go to next step
            if elAction == 'Wait':
                log.info(f'  Waiting for {elData} seconds')
                time.sleep(int(elData))
                continue

            # Switch to newly opened tab, set flag and go to next step
            if elAction == 'Tab':
                log.info('  Switching tab')
                t0 = browser.window_handles[0]
                t1 = browser.window_handles[1]
                browser.switch_to.window(t1)
                switched_tab = True
                continue

            # Switch to iFrame of given name
            if elAction == 'Frame':
                log.info('  Switching Frame')
                browser.switch_to.frame(elName)
                continue

            log.info(f'  Locating {elName}. XPath: {elXPath}')

            # Only Verify, Click and Input verbs remaining.
            # Locate element, or fail with error
            try:
                # Wait for element to be loaded and be clickable
                log.info(f'  Waiting for element {elName}')
                WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, elXPath)))
            except NoSuchElementException as _n:
                err_msg = f'  No such Element: {elName}. XPath: {elXPath}'
                log.error(err_msg)
                # log.exception(n)
                take_scr_shot('NoSuchElement')
                raise NextItem(err_msg)
            except TimeoutException as _t:
                err_msg = f'  Timeout waiting for Element: {elName}. XPath: {elXPath}'
                log.error(err_msg)
                # log.exception(t)
                take_scr_shot('Timeout')
                raise NextItem(err_msg)
            # We could obtain element from earlier wait stmt, but it was giving error sometimes
            # so explicit find_element following wait
            element = browser.find_element(By.XPATH, elXPath)

            # Verify current value of element with Data
            if elAction == 'Verify':
                log.info(f'  Verifying if value of {elXPath} is {elData}')
                if element.text.strip() == elData:
                    log.info(f'  Verified successfully proceeding...')
                    continue
                else:
                    err_msg = f'  Verification failed. Value of {elXPath} is {element.text}'
                    log.error(err_msg)
                    raise NextItem(err_msg)

            # In some cases, it is an array of elements, if so, get first element
            if isinstance(element, list):
                element = element[0]

            if element:
                match elAction:
                    # Trigger Mouse click event
                    case "Click":
                        log.info(f'  Moving to {elName}')
                        actions.move_to_element(element).perform()
                        log.info(f'  Clicking after moving to {elName}...')
                        browser.execute_script("arguments[0].click();", element)
                    # Enter Data into textbox element
                    case "Input":
                        # send keys to clear existing data, type new data and hit enter
                        log.info(f'  Moving to {element}')
                        actions.move_to_element(element).perform()
                        log.info(f'  Clicking after moving to {elName}...')
                        browser.execute_script("arguments[0].click();", element)
                        log.info(f'  Sending \"{elData}\" to {elName} after moving')
                        element.send_keys(Keys.CONTROL + "a")
                        element.send_keys(Keys.DELETE)
                        element.send_keys(elData)
                        element.send_keys(Keys.ENTER)
                    #
                #
            else:
                log.error(f'  Element {elName} not found!!')

        start_time = datetime.datetime.now()
        # Copy downloaded file
        while True:
            time.sleep(0.2)
            curr_time = datetime.datetime.now()
            elapsed = int((curr_time - start_time).total_seconds())
            if elapsed > int(custom_logger.DWNL_TIMEOUT):
                err_msg = f'Timeout ({custom_logger.DWNL_TIMEOUT}s) waiting for file download... skipping...'
                take_scr_shot('Download Timeout')
                log.info(err_msg)
                raise NextItem(err_msg)

            tdp = custom_logger.TEMP_DOWNLOAD_PATH
            fdp = custom_logger.FINAL_DOWNLOAD_PATH
            files = os.listdir(tdp)
            if len(files) == 0:
                # log.info('Waiting for download to start...')
                # take_scr_shot('Wait2Strt')
                # time.sleep(2)
                continue
            if [file for file in files if (".crdownload" in file or ".htm" in file)]:
                # log.info('Waiting for download to complete...')
                # take_scr_shot('Wait2End')
                time.sleep(2)
                for hf in glob.glob(os.path.join(tdp, "*.htm")):
                    try:
                        os.remove(hf)
                    except PermissionError as _e:
                        pass
                continue
            else:
                file = files[0]
                log.info(f'Downloading file - {file}')
                src = os.path.join(tdp, file)
                dst = os.path.join(fdp, file)
                if os.path.exists(dst):
                    file_name, file_ext = os.path.splitext(file)
                    file = file_name + datetime.datetime.now().strftime("%H%M%S") + file_ext
                    dst = os.path.join(fdp, file)
                os.rename(src, dst)
                log.info('Download completed...')
                break

        upd_XL_stat(row=index + 1, provider=source["Provider"], download='Success', fName=file)
        if switched_tab:
            browser.close()
            browser.switch_to.window(t0)
        return file

    # Catch errors and process next item
    except NextItem as _e:
        upd_XL_stat(row=index + 1, provider=source["Provider"], download='Failed', fName=_e.message)
        return


def process_downloaded_file(itemnum, source):
    global wrote_header

    if source['Convert'][0].upper() == 'N':
        log.info(f'Skipping conversion as configured')
        upd_XL_stat(row=itemnum + 1, convert="Skipped")
        return

    if not source['FileName']:
        log.info(f'Skipping Conversion. Source not downloaded')
        upd_XL_stat(row=itemnum + 1, convert="Skipped")
        return

    mods[source['Provider']] = importlib.import_module(source['Provider'])
    data_records = mods[source['Provider']].processFile(
        os.path.join(custom_logger.FINAL_DOWNLOAD_PATH, source['FileName'])
    )
    log.info(f'Imported {len(data_records)} records from: {source["Provider"]}, File:{source["FileName"]} ')

    fname = source['Provider'] + '.csv' if custom_logger.MERGE_OUTPUT == 'N' else custom_logger.MERGED_CSV_FILENAME
    mode = 'w' if custom_logger.MERGE_OUTPUT == 'N' else 'a'
    output_csv_file = os.path.join(custom_logger.CSV_PATH, fname)

    with open(file=output_csv_file, mode=mode, encoding='utf-8') as c:

        if custom_logger.MERGE_OUTPUT == 'N':
            c.write(get_csv_header())
        elif not wrote_header:
            wrote_header = True
            c.write(get_csv_header())

        log.info(f'Writing {len(data_records)} CSV records into {fname}...')
        for data_record in data_records:
            c.write(dict_to_csv(data_record))

    upd_XL_stat(row=itemnum + 1, convert="Success")


# Read work queue from input.json
with open(custom_logger.BASE_INPUT_JSON, "r") as inp_file:
    inpq = json.load(inp_file)
num_items = len(inpq)

log.info(f'Found {num_items} sources to be processed')

try:
    for idx, item in enumerate(inpq):
        log.info('*'*80)
        log.info(f'Item# {idx+1}/{num_items}. Source:{item["Provider"]}')
        log.info('Downloading file...')
        if custom_logger.SKIP_DOWNLOAD == "N":
            item['FileName'] = download_source(index=idx, source=item)
        log.info(f'Converting file... {item["FileName"]}')
        if custom_logger.SKIP_CONVERT == "N": process_downloaded_file(itemnum=idx, source=item)

# Exit Ctrl+C Gracefully
except KeyboardInterrupt as _err:
    error_msg = "**INTERRUPTED BY USER. EXITING PROGRAM**"
    log.error(error_msg)
    upd_XL_stat(row=idx + 1, download='Skipped', fName=error_msg)

finally:
    # Close and save
    log.info('Processing Completed')
    ws.set_default_row(hide_unused_rows=True)
    ws.autofilter(0, 0, num_items, 4)
    wb.close()
