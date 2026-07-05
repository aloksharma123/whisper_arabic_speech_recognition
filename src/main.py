from dataset_loader import get_sample
from transcribe import transcribe

audio_path, ground_truth = get_sample(0)

prediction = transcribe(audio_path, task="translate")

print("=" * 60)
print("Audio File:", audio_path)
print("=" * 60)

print("Arabic:")
print(ground_truth)

print()

print("English Translation:")
print(prediction)