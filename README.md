# COM_Hijacking

Author: **Asher Davila L.**

## Description:

This script is written in Python 3 and is designed to automate the creation of missing registry keys for potential COM hijacking objects. It takes a CSV file obtained from ProcMon dumps as input and attempts to hijack the objects by creating the necessary registry entries.

## Prerequisites
Before running the script, ensure that you have the following:

Python 3.x installed on your system.
Required packages: csv, os, re, shutil, winreg.

**This script works only on Windows systems. It has been tested on Windows 10 and Windows 11**

## Usage

1. Using Procmon, dump a CSV file with the following criteria/filters:
  - All the failures of RegKey Open - Operation: RegOpenKey
  - Path suffix contains InprocServer32 or InprocServer OR InprocHandler or InprocHandler32
  - HKCU before it is searched in HKLM
3. Place the CSV file ('InProcServer.CSV') containing the potential COM hijacking objects in the project directory.
4. Run one of the next scripts depending on your needs:
- The `com_hijacking_write.py` script is used to attack the identified COM registry keys. It reads the Procmon data and creates the necessary registry entries to attempt hijacking. The script takes a CSV file as input and utilizes the information within to perform the hijacking.
- The `com_hijacking_clean.py` script is used to clean the registry keys that may have been polluted after executing the attack with the `com_hijacking_write.py` script. 


## Contributing
Any feedback and any help from external maintainers are appreciated.

Create an [issue](https://github.com/AsherDLL/COM_Hijacking/issues) for feature requests or bugs that you have found.

Submit a pull request for fixes and enhancements for this tool.

## License
This plugin is released under an [Apache 2.0 License](https://github.com/AsherDLL/COM_Hijacking/blob/main/LICENSE).
