![GitHub release (latest by date)](https://img.shields.io/github/v/release/kulichr/WPvSCAN?style=for-the-badge) ![GitHub top language](https://img.shields.io/github/languages/top/kulichr/WPvSCAN?style=for-the-badge) ![GitHub last commit](https://img.shields.io/github/last-commit/kulichr/WPvSCAN?style=for-the-badge)
# WPvSCAN
WPvSCAN scans the version of CMS WordPress on the target website and compares it with the most recent version. After that, it also offers the option of listing all know exploits using [SearchSploit](https://github.com/offensive-security/exploitdb) tool by Offensive Security.
![Example of result](https://github.com/cyb3rd3s/cyb3rd3s/blob/main/wpvscan_example.png)
## Usage
```
python3 wpvscan.py -t target.com
```

## Requirements
### Pip dependencies
Necessary python dependencies should be installed with following command.
```
pip install -r requirements.txt
```
### Python 3
Whole script is written in Python 3.7., which is recommended for best functionality. Something might not work well in older versions. Python is free to download from [official website](https://www.python.org/downloads/) for all platforms.

### SearchSploit
Script offers exploits for found version of WordPress. SearchSploit could be install from official [GitHub repository.](https://github.com/offensive-security/exploitdb)

## Help & issues
If you have any question, ideas or issues, you can report them through [Issues](https://github.com/cyb3rd3s/WPvSCAN/issues).
