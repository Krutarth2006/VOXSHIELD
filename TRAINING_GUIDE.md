# VOXSHIELD Training Guide

## 1. Environment setup

```bash
cd voxshield
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Dataset preparation

Place the dataset in a structure such as:

```text
dataset/
  real/
  spoof/
```

Or use metadata-driven organization using a CSV file with columns such as:

- file_path
- label
- speaker_id
- dataset_source
- spoof_type
- sampling_rate

## 3. Train model

```bash
python train.py
```

## 4. Run inference

```bash
python predict.py sample.wav
```

## 5. Notes

- Use speaker-disjoint splits where possible.
- Keep validation/test data free from augmentation.
- Use the same preprocessing config for training and inference.
- Report performance honestly, especially out-of-domain generalization.
