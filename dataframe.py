import csv
from stats import *
from file_handler import read_csv_file, read_dtype, write_csv_file

class DataFrame:
    def __init__(self, data, dtype):
        '''
        Docstring for __init__
        initialize the DataFrame object
        
        :param self: Description the DataFrame object
        :param data: Description the data dictionary
        :param dtype: Description the data types dictionary
        '''
        self.data = data
        self.dtype = dtype

    @classmethod
    def read_csv(cls, data_path, dtype_path):
        '''
        Docstring for read_csv
        reads a csv file and a data type file and returns a DataDrame object
        
        :param cls: Description the DataFrame class
        :param data_path: Description the path to the data file
        :param dtype_path: Description the path to the data types file
        '''
        dtype = read_dtype(dtype_path)
        data = read_csv_file(data_path, dtype)
        return cls(data, dtype)

    def count_nulls(self, ):
        '''
        Docstring for count_nulls counts the number of missing values in each column
        '''
        return { 
            col : sum( x is None for x in self.data [col]) 
            for col in self.data
                }

    def describe(self, path="describe.csv"):
        '''
        Docstring for describe generate a csv file containing statistics for each column
        
        :param self: Description the DataFrame object
        :param path: Description the path to the output file
        '''
        data_dict = {
            "column": [],
            "nulls": [],
            "max": [],
            "min": [],
            "mean": [],
            "median": [],
            "mode": []
        }

        for col in self.data:
            data_dict["column"].append(col)
            data_dict["nulls"].append(sum(x is None for x in self.data[col]))
            if self.dtype[col] in ("int", "float" ):
                data_dict["max"].append(get_col_max(self.data[col]))
                data_dict["min"].append(get_col_min(self.data[col]))
                data_dict["mean"].append(get_col_mean(self.data[col]))
                data_dict["median"].append(get_col_median(self.data[col]))
                data_dict["mode"].append(get_col_mode(self.data[col]))
            else:
                data_dict["max"].append(None)
                data_dict["min"].append(None)
                data_dict["mean"].append(None)
                data_dict["median"].append(None)
                data_dict["mode"].append(get_col_mode(self.data[col]))

        write_csv_file(path , data_dict)

            

    def fill_na(self, num_strategy, cat_strategy):
        '''
        Docstring for fill_na fill the missing values in the DataFrame using the provided strategies
        
        :param num_strategy: Description the strategy function for numercal columns
        :type num_strategy: function
        :param cat_strategy: Description the strategy function for categorical columns
        :type cat_strategy: function
        '''
        for col in self.data:
            if self.dtype[col] in ("int", "float" ):
                fill_value = num_strategy(self.data[col])
            else  :
                fill_value = cat_strategy(self.data[col])
            
            self.data[col] = [
                fill_value if x is None  else x
                for x in self.data[col]
            ]

    def to_csv(self, path = "data/out.csv"):
        '''
        Docstring for to_csv write the DataFrame to a csv file
        
        :param self: Description the DataFrame object
        :param path: Description the path to the output file
        '''
        write_csv_file( path , self.data)