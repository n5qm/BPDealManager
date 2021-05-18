# WARNING
This script should be used at your own risk, I will not be responsible for any errors encountered while using the script or caused by the script.  Use of the script means that you understand this warning and agree that you are using the script at your own risk.

All of that said, I have been using this script to manage my deals and it is working as expected.

# BPDealManager
This Python script is intended to manage the Active Trader style of the [Block Party Strategy](https://www.blockpartytrading.com/).  It will check the status of your active deals every minute and update the Take Profit level based on the number of completed Safety Orders based on the strategy document.

| Completed Safety Orders | Take Profit Level |
| ----------------------- | ----------------- |
| 1                       | No Change         |
| 2                       | No Change         |
| 3                       | 1%                |
| 4                       | 2%                |
| 5                       | 3%                |
| 6                       | 4%                |
| 7                       | 5%                |
| 8                       | 6%                |


### Requirements
* Python version 3.X
* py3cw Python module available at the [Project Homepage](https://github.com/bogdanteodoru/py3cw) or via pip `pip install py3cw`.

### Configuration
The script requires minimal configuration.  All of the necessary changes are made at the top of the file.

`API_KEY = ''`
An API key for your 3Commas account.  The required permission are BotsRead and BotsWrite.

`API_SECRET = ''`
The API secret that matches the API key used.

`BOT_NAME = 'Block Party Bot'`
The name of the bot that we are managing.

### Running
Running the script is rather straightforward `python bp_deal_manager.py`

### Questions or Problems
If you run into any issues, please create an issue on this repository and I will do what I can to help out.
