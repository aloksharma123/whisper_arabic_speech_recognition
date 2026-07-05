from dataset_loader import get_sample
from transcribe import transcribe
from jiwer import wer

audio_path, ground_truth = get_sample(0)

prediction = transcribe(audio_path)

# -------------------------
# CLEAN TEXT (important)
# -------------------------
gt = ground_truth.strip()
pred = prediction.strip()

# -------------------------
# WER CALCULATION
# -------------------------
error_rate = wer(gt, pred)
accuracy = (1 - error_rate) * 100

# -------------------------
# OUTPUT
# -------------------------
print("=" * 60)
print("Audio File:", audio_path)
print("=" * 60)

print("Ground Truth (Arabic):")
print(gt)

print("\nPredicted Arabic Transcript:")
print(pred)

print("\n================ METRICS ================")
print(f"Word Error Rate (WER): {error_rate:.4f}")
print(f"Accuracy: {accuracy:.2f}%")