from dataset_loader import get_sample
from transcribe import transcribe
from evaluator import print_evaluation

# Load sample
audio_path, ground_truth = get_sample(0)

# Whisper prediction
prediction = transcribe(audio_path)

# Print raw info
print("=" * 60)
print("Audio File:", audio_path)
print("=" * 60)

# Evaluate
print_evaluation(ground_truth, prediction)