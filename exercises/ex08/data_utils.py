"""Dictionary related utility functions."""

__author__ = ""

# Define your functions below


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reading the rows of a csv file into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    
    file_handle.close()
    return result 


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Producing a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table: 
        item: str = row[column]
        result.append(item)
    return result 


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(column_table: dict[str, list[str]], number: int) -> dict[str, list[str]]:
    """Produce a new column based table from a certain number of rows."""
    result: dict[str, list[str]] = {}

    for key in column_table:
        empty: list[str] = []
        if number > len(column_table[key]):
            return column_table
        i: int = 0 
        while i < number:
            empty.append(column_table[key][i])
            i += 1
        result[key] = empty
    return result


def select(original_columns: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column based table with only selected ones."""
    result: dict[str, list[str]] = {}

    for column in names:
        result[column] = original_columns[column]
    return result


def concat(col_table_1: dict[str, list[str]], col_table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column based table from combining two column based tables."""
    result: dict[str, list[str]] = {}

    for column in col_table_1:
        result[column] = col_table_1[column]
    for column in col_table_2:
        if column in result: 
            result[column] += col_table_2[column]
        else:
            result[column] = col_table_2[column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Returns a dictionary of the number of items from the list of values."""
    result: dict[str, int] = {}
    for value in values:
        if value in result:
            result[value] += 1
        else: 
            result[value] = 1
    return result 