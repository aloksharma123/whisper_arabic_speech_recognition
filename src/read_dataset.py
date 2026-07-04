import pandas as pd

# Read the dataset
df = pd.read_csv(
    "dataset/metadata-wav.csv",
    sep="|",
    header=None
)

print(df.head())