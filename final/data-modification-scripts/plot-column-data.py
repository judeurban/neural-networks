import matplotlib.pyplot as plt
from pandas import DataFrame, read_csv
from tqdm import tqdm

translated_df = read_csv("final/modified-data/bank_categorical_translate.csv")

for col in tqdm(translated_df.columns):

    # build column axis
    ax = plt.axes()
    ax.scatter(range(0, len(translated_df)), translated_df[col], color='red')
    ax.set_title(f'Normalized {col} variation')
    ax.set_xlabel("Data Frame Index")

    # for idx in range(len(translated_df)):
    #     ax.scatter(idx, translated_df[col][idx], color='blue')

    fig = plt.gcf()
    fig.savefig(f'doak-{col}.png')
    fig.clear()
    ax.clear()