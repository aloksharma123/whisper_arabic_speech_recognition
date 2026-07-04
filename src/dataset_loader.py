import pandas as pd
import os

# ==========================
# Dataset Configuration
# ==========================

DATASET_FOLDER = "dataset/arabic_tts"
METADATA_FILE = os.path.join(DATASET_FOLDER, "metadata.csv")
WAV_FOLDER = os.path.join(DATASET_FOLDER, "wavs")


def load_dataset():
    """
    Reads metadata.csv and returns a DataFrame.
    """

    df = pd.read_csv(
        METADATA_FILE,
        sep="|",
        header=None,
        names=["transcript", "filename"]
    )

    return df


def get_sample(index=0):
    """
    Returns one sample from the dataset.
    """

    df = load_dataset()

    row = df.iloc[index]

    transcript = row["transcript"]
    filename = row["filename"]

    audio_path = os.path.join(WAV_FOLDER, filename)

    return audio_path, transcript


def get_dataset():
    """
    Returns the complete dataset.
    """

    return load_dataset()