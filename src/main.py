import re
from dataset_loader import get_sample
from transcribe import transcribe
from jiwer import wer

# -------------------------
# Arabic normalization
# -------------------------
def normalize_arabic(text):
    # remove diacritics
    text = re.sub(r'[\u064B-\u0652]', '', text)

    # remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    return text

audio_path, ground_truth = get_sample(0)

prediction = transcribe(audio_path)

# -------------------------
# CLEAN TEXTS
# -------------------------
gt = normalize_arabic(ground_truth)
pred = normalize_arabic(prediction)

# -------------------------
# METRICS
# -------------------------
error_rate = wer(gt, pred)
accuracy = (1 - error_rate) * 100

# -------------------------
# OUTPUT
# -------------------------
print("=" * 60)
print("Audio File:", audio_path)
print("=" * 60)

print("Ground Truth (cleaned):")
print(gt)

print("\nPrediction (cleaned):")
print(pred)

print("\n================ METRICS ================")
print(f"WER: {error_rate:.4f}")
print(f"Accuracy: {accuracy:.2f}%")