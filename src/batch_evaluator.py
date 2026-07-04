import os
import time
import pandas as pd

from dataset_loader import get_dataset
from transcribe import transcribe
from evaluator import compute_wer

DATASET_FOLDER = "dataset/arabic_tts/wavs"

# Number of samples to evaluate
NUM_SAMPLES = 20

df = get_dataset()

results = []

start_time = time.time()

for i in range(NUM_SAMPLES):

    transcript = df.iloc[i]["transcript"]

    filename = df.iloc[i]["filename"]

    audio_path = os.path.join(DATASET_FOLDER, filename)

    prediction = transcribe(audio_path)

    error = compute_wer(transcript, prediction)

    results.append({
        "Filename": filename,
        "WER": error,
        "Ground Truth": transcript,
        "Prediction": prediction
    })

    print(f"{i+1}/{NUM_SAMPLES} completed")

end_time = time.time()

results_df = pd.DataFrame(results)

print("\n==============================")
print("Evaluation Complete")
print("==============================")

print(f"Average WER : {results_df['WER'].mean():.3f}")
print(f"Best WER    : {results_df['WER'].min():.3f}")
print(f"Worst WER   : {results_df['WER'].max():.3f}")

print(f"\nTotal Time  : {end_time-start_time:.2f} sec")

results_df.to_csv(
    "outputs/evaluation_results.csv",
    index=False
)

print("\nCSV report saved successfully!")