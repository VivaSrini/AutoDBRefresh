# Auto DB Refresh
## Overview
AutoDBRefresh is a python script which is currently used to download certified minority vendor directories from various govt. web sources.
## Program Structure
 - **src** folder
   - `main.py` - Main Python program
   - `custom_logger.py`  - Sets up Logging and other options
 - **config** folder (input)
   - `input.json` - URLs to be processed and steps to be performed
   - `config.ini` - Program configuration - folder and file names, log format and other options
 - **run** folder (output)
   - `Run_Results.xlsx` - Status of each URL processed in the batch and name of downloaded file
   - `config.ini` - Program configuration - folder and file names, log format and other options
   - **downloads** folder - All downloaded files
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
    "Steps": [
      {
        "XPath": "//span[@id='ctl00_MainContent_btnSearch']",
        "Name": "Searchbutton",
        "Action": "Click",
        "Data": "None"
      },
      {
        "XPath": "//input[@id='ctl00_MainContent_BusinessGrid_ctl00_ctl02_ctl00_ExportToExcelButton']",
        "Name": "Export to Excel button",
        "Action": "Click",
        "Data": "None"
      }
    ]
  },
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
|Steps|Steps to be performed. Each Step has four fields explained below|
### Step fields
|Step Field|Description|
|-|-|
|XPath|Xpath of the element to be acted upon|
|Name|Name of the element to be used in log|
|Action| **Click**: Mouse click on the element <br> **Input**: Enter data from Data field in a Textbox <br> **Tab**: Switch to next tab and continue <br> **Frame**: Switch to frame specified in 'Name' <br> **Screenshot**: Take a screenshot <br> **Verify**: Verify if the value of the element|
|Data|Data to be entered in the Textbox|

