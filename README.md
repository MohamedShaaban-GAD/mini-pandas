# MiniPandas

MiniPandas is a lightweight Python library that mimics some core functionalities of the pandas `DataFrame`, implemented from scratch for learning and practice purposes.

The project focuses on data handling, basic statistics, and CSV file operations without relying on the pandas library.

---

## Features

- Custom `DataFrame` class
- Basic statistical operations (min, max, mean, median, mode)
- Handling missing values
- CSV file reading and writing
- Automatic generation of descriptive statistics as a CSV file

---

## Project Structure

MiniPandas/
├── main.py
├── dataframe.py
├── stats.py
└── file_handler.py
---

## Modules Overview

### dataframe.py
Contains the core `DataFrame` class.

**Attributes**
- `data`: stores the dataset
- `dtype`: stores data types for each column

**Methods**
- `count_nulls()` – counts missing values in each column
- `fill_na(value)` – fills missing values with a specified value
- `describe()` – computes statistical summaries and exports them to a CSV file
- `to_csv(file_name)` – writes the DataFrame to a CSV file

---

### stats.py
Contains all statistical functions used by the library.

**Functions**
- `min`
- `max`
- `mean`
- `median`
- `mode`
- `get_stats` – generates a complete statistical summary for a column

---

### file_handler.py
Handles file input and output operations.

**Functions**
- `read_dtype()` – detects and reads column data types
- `read_csv_file()` – reads data from a CSV file
- `write_csv_file()` – writes data to a CSV file

---

### main.py
Entry point used to test and demonstrate the MiniPandas library functionality.

---

## Usage Example

```python
from dataframe import DataFrame

df = DataFrame("data.csv")

df.fill_na(0)
df.describe()
df.to_csv("output.csv")
```


## Requirements

Python 3.x
(No external dependencies)

---
## Purpose of the Project

This project was developed for educational purposes to:

- Understand how pandas works internally

- Practice object-oriented programming in Python

- Build a custom data manipulation library from scratch

# Author

## Mohamed Shaaban