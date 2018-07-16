Instruction
Time to wrap things up! In this part of the course, we talked about DataFrames, the basic data structure of the pandas library. Let's recap what we learned.

pd.read_csv('file.csv') creates a new DataFrame based on file.csv.

To access a single column, use:
dataframe['column_name']

To create a new column, use:
dataframe['new_column'] = ...

To drop a column, use:
dataframe.drop('column_name', axis=1)

To select a row based on its integer location, use:
dataframe.iloc[2]

To select a row based on the current index, use:
dataframe.loc[index_value]

To filter rows in a DataFrame using the index slice notation use:
dataframe[start_index:end_index]
The start_index is inclusive, the end_index is exclusive.

To filter rows by index and columns by name at the same time, use:
dataframe.loc[index_value, 'column name']

To set a column as the index, use:
dataframe.set_index('column_name')

To reset the index, use:
dataframe.reset_index(drop=True)

To sort rows, use:
dataframe.sort_values(by='column_name')

Okay, how about a short quiz now?
