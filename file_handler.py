'''
Docstring for file_handler
'''
import csv

def read_dtype(file_path):
    '''
    returns a dict with key are the col names and values are the cols dtypes
    
    :param file_path: path to the csv file containing the data we would like to summarize their dtype
    '''
    dtypes = {}
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for d in reader:
            dtypes[d["column"]] = d["dtype"]
            
    return dtypes


def read_csv_file(file_path, dtpye: dict):
    '''
    Docstring for read_csv_file
    read a csv file and convert each cell to the approriate dype.
    returns a dict where keys are column names and values are list of values with missing data as None.
    
    :param file_path: path to the csv file.
    :param dtype: dict of the required data types for each colum.

    '''
    try:

        with open(file_path, 'r') as f:
            data = {}
            reader = csv.DictReader(f)
            reader_list = list(reader)
            if not reader_list:
                raise Exception
            
            headers = reader.fieldnames

            for key in headers:
                data[key] = [row_dict[key] for row_dict in reader_list]

            for key, lst in data.items():
                for i, value in enumerate(lst):
                    if value == "":
                        data[key][i] = None
                    else:
                        if dtpye[key] == "int":
                            data[key][i] = int(value)
                        elif dtpye[key] == "float":
                            data[key][i] = float(value)
                        else :
                            data[key][i] = str(value)
            return data
        
    except Exception as e:
            print("File is empty")


def write_csv_file(file_path, data: dict):
    '''
    Docstring for write_csv_file
    Writes the data from a dict into a csv file
    
    :param file_path: path where the file will be written
    :param data: dict with data to be written
    '''
    with open(file_path, 'w') as f:
        writer = csv.writer(f)
        headers = list(data.keys())
        
        writer.writerow(headers)


        rows_len = len(data[headers[0]])

        for i in range(rows_len):
            row = []
            for key in headers:
                row.append(data[key][i])
            writer.writerow(row)


