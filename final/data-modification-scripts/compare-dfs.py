from pandas import DataFrame, read_csv

original_df = read_csv("final/orignal-data/bank-additional-full.csv", delimiter=';')
translated_df = read_csv("translated.df.csv")

# indecies = [0, 7, 100, 10_000, 30_000]
idx = 30_000

print(f'col: original_df -> translated_df\n')

for col in original_df.columns:

    # I changed the name of this column
    if col == "y":
        print(f'{col}: {original_df[col][idx]} -> {translated_df[col]["target"]}')
        continue

    print(f'{col}: {original_df[col][idx]} -> {translated_df[col][idx]}')

# TODO plot scarcity of data