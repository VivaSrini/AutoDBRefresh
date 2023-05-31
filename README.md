# Auto DB Refresh
## Overview
AutoDBRefresh is a python script which is currently used to download certified minority vendor directories
from various govt. web sources. The downloaded files are the converted into a standard CSV format
## Program Structure
 - **src** folder
   - `main.py` - Main Python program
   - `custom_logger.py`  - Sets up Logging and other options
   - `utilities.py`  - Common utilities for modules
 - **config** folder (input)
   - `input.json` - URLs to be processed and steps to be performed
   - `config.ini` - Program configuration - folder and file names, log format and other options
 - **run** folder (output)
   - `Run_Results.xlsx` - Status of each source downloaded and processed in this run and name of downloaded file
   - **config** folder - Copy of the configuration for this run
   - **downloads** folder - All files downloaded in this run
   - **csv** folder - Converted file(s). Either <em>module_name.csv</em> per module, or a consolidated one as named in config.ini
   - **log** folder - log file and screenshots for this run
## Input.json Structure
The `input.json` file contains all the source items to be processed. Each Item will follow zero or multiple steps and download one file
### Sample file
~~~
[
  {
    "Provider": "WI_DOA",
    "State": "WI",
    "Name": "Wisconsin DOA",
    "Website": "https://wisdp.wi.gov/Search.aspx",
    "Title": "Business Search",
    "Download": "Yes",
    "Convert": "Yes",
    "FileName": "",
    "Steps": [
      {
        "XPath": "//span[@id='ctl00_MainContent_btnSearch']",
        "Name": "Searchbutton",
        "Action": "Click",
        "Data": "None"
      },
      {
        "XPath": "//input[@name='sSearchBasic']",
        "Name": "Search box",
        "Action": "Input",
        "Data": "[a-z]"
      },
      {
        "XPath": "//h3",
        "Name": "",
        "Action": "Verify",
        "Data": "Minority and Women Owned Business Directory"
      },
      {
        "XPath": "//html",
        "Name": "Wait for 10 seconds",
        "Action": "Wait",
        "Data": "10"
      },
      {
        "XPath": "",
        "Name": "",
        "Action": "Screenshot",
        "Data": ""
      }
    ]
  }
  {
    "Provider": "MN_DOA",
    "State": "MN",
    "Name": "Minnesota DOA",
    "Website": "https://mn.gov/admin-stat/osp/download/vmpvendors.csv",
    "Title": "Equity in Procurement (TG/ED/VO) Directory / Minnesota Office of State Procurement",
    "Steps": [
    ]
  }
]
~~~
### Item Fields
|Item Field|Description|
|-|-|
|Provider|Handle for the item|
|State|State from input links file|
|Name|Name of source from input links file|
|Website|Website of source from input links file|
|Title|Browser Window title (not used for validation anymore)|
|Download|Yes/No Download this source file?|
|Convert|Yes/No Convert and add records to output?|
|Filename|If manually downloaded separately, specify filename here to convert|
|Steps|Steps to be performed. Each Step has four fields explained below|
### Step fields
|Step Field|Description|
|-|-|
|XPath|Xpath of the element to be acted upon|
|Name|Name of the element to be used in log|
|Action|Action Verb. There are seven verbs - explained below|
|Data|Data to be entered in the Textbox|
### Action Verbs
|Verb|Description|
|-|-|
|Click|Mouse click on the element|
|Input|Enter data from Data field in a Textbox|
|Tab|Switch to next tab and continue|
|Frame|Switch to frame specified in 'Name'|
|Screenshot|Take a screenshot|
|Verify|Verify that element has value specified in 'Data'|
|Wait|Pause execution for 'Data' seconds|
