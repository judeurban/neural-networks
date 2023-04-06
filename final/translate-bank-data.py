from pandas import read_csv, DataFrame
from tqdm import tqdm
import numpy as np

# Load our Data From the CSV File in this Directory
raw_df = read_csv('final/bank-full.csv', delimiter=';')
# raw_df = read_csv('final/bank-additional-full.csv', delimiter=';')

# translation dataframe to be populated
translated_df = DataFrame()

# create an enumerated value for each new field we get
translation_field_bank = dict()

# custom months dictionary
translation_field_bank['month'] = {
    'jan': 1,
    'feb': 2,
    'mar': 3,
    'apr': 4,
    'may': 5,
    'jun': 6,
    'jul': 7,
    'aug': 8,
    'sep': 9,
    'oct': 10,
    'nov': 11,
    'dec': 12    
}

# columns where we need to perform "translation"
translation_columns = [
    "job",
    "marital",
    "education",
    "default",
    "housing",
    "loan",
    "contact",
    "month",
    "poutcome",
    "y"
]

binary_dict = {
    "no": 0,
    "yes": 1
}

print("Translating Data...")

# iterate through each column in the dataframe
for column_name in tqdm(raw_df.columns):

    new_column_values = np.zeros(len(raw_df), dtype=np.int32)

    if column_name not in translation_columns:

        # iterate through each row in the column and copy the row value. These are the default values.
        for index, row_value in enumerate(raw_df[column_name]):
            new_column_values[index] = row_value
        
        translated_df[column_name] = new_column_values
        continue 
    
    elif column_name == "month":
        
        # iterate through each row and place the enumerated month instead of the string
        for index, row_value in enumerate(raw_df['month']):
            new_column_values[index] = translation_field_bank['month'][row_value]
        
        translated_df[column_name] = new_column_values
        continue

    # binary assignment
    if raw_df[column_name][0] == "yes" or raw_df[column_name][0] == "no":
        translation_field_bank[column_name] = binary_dict.copy()
    
    # create a new, unique dictionary that will populate this enumeration object.
    else:
        translation_field_bank[column_name] = dict()

    # enumeration field, starts at zero and increments by one as a uniuqe field is added to our bank.
    enumeration_idx: int = 0

    # iterate through each row in the column
    for index, row_value in enumerate(raw_df[column_name]):

        # if the row value doesn't exist, add it
        if row_value not in translation_field_bank[column_name].keys():
            translation_field_bank[column_name][row_value] = enumeration_idx
            enumeration_idx += 1

        new_column_values[index] = translation_field_bank[column_name][row_value]

    translated_df[column_name] = new_column_values

# rename target data
translated_df = translated_df.rename(columns={'y': 'target'})

# if you want to look at the dataframe
translated_df.to_csv("final/bank-full-translated.csv")

# import json
# print(json.dumps(translation_field_bank))