from pandas import read_csv, DataFrame
import random

# load the translated bank data
translated_df = read_csv('final/bank-full-translated.csv')

total_datapoints = 45210 + 1
total_validation_points = 4500
total_training_points = total_datapoints - total_validation_points

training_dict = dict()
validation_dict = dict()

random_indeces = random.sample(range(0, total_datapoints - 1), total_validation_points)

for column_name in translated_df.columns:
    
    # allocate the emtpy structures for two separate dataframes
    training_dict[column_name] = np.zeros(total_training_points)
    validation_dict[column_name] = np.zeros(total_validation_points)

    # build the valiation dataframe
    for i, random_idx in enumerate(random_indeces):
        validation_dict[column_name][i] = translated_df[column_name][random_idx]

    # build the training dataframe

    training_idx = 0
    for idx in range(total_datapoints):

        if idx in random_indeces: continue

        training_dict[column_name][training_idx] = translated_df[column_name][idx]
        training_idx += 1

training_data_df = DataFrame(training_dict)
validation_data_df = DataFrame(validation_dict)
training_data_df.to_csv('final/translated-training-data.csv')
validation_data_df.to_csv('final/validation-training-data.csv')