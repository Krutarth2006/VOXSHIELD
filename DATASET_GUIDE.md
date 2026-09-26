# VOXSHIELD Dataset Guide

## Recommended datasets

- ASVspoof 2019
- ASVspoof 2021 DF
- WaveFake
- Fake-or-Real (FoR)

## Data quality checks

The dataset pipeline should verify:
- missing files
- corrupted audio
- sampling rate mismatches
- channel issues
- class imbalance
- speaker distribution
- duplicate recordings

## Label scheme

- REAL = 0
- SPOOF/AI = 1

## Example metadata structure

```csv
file_path,label,speaker_id,dataset_source,spoof_type,sampling_rate
real/001.wav,0,S01,ASVspoof2019,NA,16000
spoof/001.wav,1,S02,ASVspoof2019,vc,16000
```

## Important note

Do not rely only on file names. Use official metadata and dataset documentation to avoid label leakage and incorrect training splits.

## Build an ASVspoof manifest

Download the ASVspoof 2019 Logical Access audio archive and protocol files from the official dataset source. Keep the extracted files outside version control, for example:

```text
dataset/raw/ASVspoof2019_LA/ASVspoof2019_LA_train/flac/
dataset/raw/ASVspoof2019_LA/ASVspoof2019_LA_cm_protocols/ASVspoof2019.LA.cm.train.trn.txt
```

Then build a manifest using the protocol labels:

```bash
python -m dataset.build_asvspoof_manifest \
	--protocol dataset/raw/ASVspoof2019_LA/ASVspoof2019_LA_cm_protocols/ASVspoof2019.LA.cm.train.trn.txt \
	--audio-root dataset/raw/ASVspoof2019_LA/ASVspoof2019_LA_train/flac \
	--split train \
	--output dataset/manifests/asvspoof_train.csv
```

Run the command again with the development and evaluation protocol/audio directories. The command exits with status 2 when any referenced audio file is missing, preventing an incomplete manifest from silently entering training.
