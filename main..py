from dataframe import DataFrame as DF
from stats import * 

def main():
    data_csv = r".\data\titanic.csv"
    dtype_csv = r".\data\titanic_dtype.csv"
    df = DF.read_csv(data_csv, dtype_csv)
    print(f'nulls count:\n{ df.count_nulls() }')
    df.describe()
    print("describe.csv file generated")
    df.fill_na(get_col_mean, get_col_mode)
    print("missing values filled")
    df.describe("describe_filled.csv")
    print("describe_filled.csv file generated")
    df.to_csv()
    print("output.csv file generated")

if __name__ == "__main__":
    main()