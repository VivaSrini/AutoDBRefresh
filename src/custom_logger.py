from configparser import RawConfigParser
import datetime
import logging
import os
import sys

config = RawConfigParser(inline_comment_prefixes=('#',))
config.read(r'config/config.ini')

# Setup i/o files and folders
INPUT_JSON_FILE_NAME = config['Files']['INPUT_JSON']
OUTPUT_LOG_FILE_NAME = config['Files']['LOG_FILE']
RUN_FOLDER_NAME = config['Folders']['RUN_FOLDER']
LOG_FOLDER_NAME = config['Folders']['LOG_FOLDER']
MOD_FOLDER_NAME = config['Folders']['MOD_FOLDER']
CSV_FOLDER_NAME = config['Folders']['CSV_FOLDER']
CONFIG_FOLDER_NAME = config['Folders']['CFG_FOLDER']
DOWNLOAD_FOLDER_NAME = config['Folders']['DNL_FOLDER']
TEMP_FOLDER_NAME = config['Folders']['TMP_FOLDER']

LOG_LVL_SCR = int(config['Log']['LOG_LVL_SCR'])
LOG_LVL_FIL = int(config['Log']['LOG_LVL_FIL'])
LOG_FMT_SCR = config['Log']['LOG_FMT_SCR']
LOG_FMT_FIL = config['Log']['LOG_FMT_FIL']
LOG_DTE_FMT = config['Log']['LOG_DTE_FMT']
log_formatter = logging.Formatter(LOG_FMT_SCR)

PROFILE = config['Chrome']['PROFILE']
DWNL_TIMEOUT = config['Params']['DWNL_WAIT_TIMEOUT']
SKIP_DOWNLOAD = config['Params']['SKIP_DOWNLOAD'].upper()[0]
SKIP_CONVERT = config['Params']['SKIP_CONVERT'].upper()[0]
MERGE_OUTPUT = config['Params']['MERGE_OUTPUT'].upper()[0]
MERGED_CSV_FILENAME = config['Params']['MERGED_CSV_FILENAME']

BASE_PATH = os.path.realpath("./")
CONFIG_PATH = os.path.join(BASE_PATH, CONFIG_FOLDER_NAME)
MODULE_PATH = os.path.join(BASE_PATH, MOD_FOLDER_NAME)
RUN_PATH = os.path.relpath(os.path.join(
    BASE_PATH,
    RUN_FOLDER_NAME,
    f'run_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}'
))
FINAL_DOWNLOAD_PATH = os.path.join(RUN_PATH, DOWNLOAD_FOLDER_NAME)
TEMP_DOWNLOAD_PATH = os.path.join(FINAL_DOWNLOAD_PATH, TEMP_FOLDER_NAME)
RUN_CONFIG_PATH = os.path.join(RUN_PATH, CONFIG_FOLDER_NAME)

XL_FILE = os.path.join(RUN_PATH, config['Files']['RUN_REPORT_FILE'])
XL_SHEET = config['Files']['RUN_REPORT_SHEET']

BASE_INPUT_JSON = os.path.join(CONFIG_PATH, INPUT_JSON_FILE_NAME)
RUN_INPUT_JSON = os.path.join(RUN_CONFIG_PATH, INPUT_JSON_FILE_NAME)
CSV_PATH = os.path.join(RUN_PATH, CSV_FOLDER_NAME)
LOG_PATH = os.path.join(RUN_PATH, LOG_FOLDER_NAME)
LOG_FILE = os.path.realpath(os.path.join(LOG_PATH, OUTPUT_LOG_FILE_NAME))

# Create run folders and copy input.json for this run
os.makedirs(RUN_PATH)
os.makedirs(LOG_PATH)
os.makedirs(CSV_PATH)
os.makedirs(FINAL_DOWNLOAD_PATH)
os.makedirs(RUN_CONFIG_PATH)
os.makedirs(TEMP_DOWNLOAD_PATH)
sys.path.append(MODULE_PATH)


class LogGen:

    @staticmethod
    def logGen():
        logging.basicConfig(filename=LOG_FILE, level=LOG_LVL_FIL, datefmt=LOG_DTE_FMT, filemode='w', format=LOG_FMT_FIL)
        console_log_handler = logging.StreamHandler(sys.stdout)
        console_log_handler.setLevel(LOG_LVL_SCR)
        console_log_handler.setFormatter(log_formatter)

        log = logging.getLogger(__name__)

        if log.hasHandlers():
            log.handlers.clear()
        log.setLevel(LOG_LVL_SCR)
        log.addHandler(console_log_handler)

        return log
