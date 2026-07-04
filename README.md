# Whisper Arabic Speech Recognition

## Overview

Whisper Arabic Speech Recognition is an end-to-end Automatic Speech Recognition (ASR) project built using OpenAI's Whisper model and Python. The project demonstrates how to load an Arabic speech dataset, transcribe audio into text, evaluate transcription quality using Word Error Rate (WER), and generate batch evaluation reports.

This repository is designed as a learning project while following professional machine learning engineering practices. It provides a clean and modular codebase that can be extended for research, experimentation, benchmarking, and future fine-tuning.

---

# Features

* Arabic speech transcription using Whisper
* Modular project architecture
* Dataset loading from metadata
* Automatic audio file selection
* Single audio transcription
* Batch transcription for multiple audio files
* Word Error Rate (WER) evaluation
* CSV report generation
* Easily extendable architecture
* Beginner-friendly implementation

---

# Project Structure

```text
Whisper_Arabic_Speech_Recognition/
│
├── dataset/
│   └── arabic_tts/
│       ├── metadata.csv
│       └── wavs/
│
├── outputs/
│
├── src/
│   ├── main.py
│   ├── transcribe.py
│   ├── dataset_loader.py
│   ├── evaluator.py
│   └── batch_evaluator.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# Technologies Used

* Python 3.12
* PyTorch
* OpenAI Whisper
* Pandas
* JiWER
* FFmpeg

---

# Dataset

The project uses an Arabic speech dataset containing:

* Arabic speech recordings
* Ground truth Arabic transcripts
* Metadata file mapping audio to text

The dataset is not included in this repository due to its size.

---

# Workflow

The complete pipeline works as follows:

```text
Dataset
   │
   ▼
Load Metadata
   │
   ▼
Locate Audio File
   │
   ▼
Whisper Model
   │
   ▼
Arabic Transcription
   │
   ▼
WER Evaluation
   │
   ▼
CSV Report
```

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd Whisper_Arabic_Speech_Recognition
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment.

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install FFmpeg and ensure it is available in your system PATH.

---

# Running Single Audio Evaluation

Run:

```bash
python src/main.py
```

The program will:

* Load one audio sample
* Transcribe it using Whisper
* Compare it with the ground truth
* Compute Word Error Rate

Example output:

```text
Ground Truth:
هو يحبّها و هي تحبّه أيضا.

Prediction:
ويو حيب بها وحيب بهو عيبا

WER:
1.00
```

---

# Running Batch Evaluation

Run:

```bash
python src/batch_evaluator.py
```

The script will:

* Process multiple audio files
* Generate predictions
* Compute WER for every sample
* Save results as a CSV file

Example:

```text
Average WER : 0.839
Best WER    : 0.400
Worst WER   : 1.500
```

---

# Evaluation Metric

The project uses **Word Error Rate (WER)**.

WER measures the number of insertions, deletions, and substitutions required to transform the predicted transcription into the reference transcription.

Lower WER indicates better transcription quality.

---

# Current Capabilities

✔ Single audio transcription

✔ Batch evaluation

✔ Whisper Base model support

✔ CSV export

✔ Modular architecture

✔ Arabic speech recognition

---

# Future Improvements

* Support Whisper Tiny, Small, Medium, and Large models
* Compare multiple ASR models
* Arabic text normalization
* Character Error Rate (CER)
* Confidence score visualization
* Progress bars using tqdm
* Automatic performance reports
* Graphical dashboards
* GPU acceleration
* Fine-tuning on custom Arabic datasets
* ONNX and TensorRT deployment
* REST API for inference
* Docker support

---

# Learning Outcomes

This project demonstrates practical experience with:

* Speech Recognition
* Machine Learning Engineering
* Model Evaluation
* Dataset Handling
* Python Project Organization
* Batch Processing
* Performance Benchmarking
* Whisper Integration
* Error Analysis

---

# License

This project is intended for educational and research purposes.

Please ensure that any datasets and third-party libraries used comply with their respective licenses.

---

# Acknowledgements

* OpenAI Whisper
* PyTorch
* JiWER
* Pandas
* FFmpeg
* Mozilla Common Voice and other open Arabic speech datasets

---

# Author

**Alok Sharma**

Machine Learning and AI Enthusiast

This repository is part of a hands-on journey toward building production-ready AI applications in Computer Vision, Natural Language Processing, and Speech Recognition.
