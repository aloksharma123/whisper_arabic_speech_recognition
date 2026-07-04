from jiwer import wer


def compute_wer(reference, hypothesis):
    """
    Compute Word Error Rate (WER)
    """
    error = wer(reference, hypothesis)
    return error


def print_evaluation(reference, hypothesis):
    """
    Print evaluation results.
    """

    error = compute_wer(reference, hypothesis)

    accuracy = max(0.0, (1 - error) * 100)

    print("\n" + "=" * 60)
    print("EVALUATION RESULT")
    print("=" * 60)

    print(f"Ground Truth : {reference}")
    print(f"Prediction   : {hypothesis}")
    print(f"WER          : {error:.2f}")
    print(f"Accuracy     : {accuracy:.2f}%")

    print("=" * 60)