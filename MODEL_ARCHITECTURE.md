# VOXSHIELD Model Architecture

## Proposed model

VOXSHIELD uses a CNN-based synthetic speech detector with mel-spectrogram inputs.

### Input
- 3-5 second audio clip
- 16 kHz sample rate
- mono conversion
- normalized audio

### Feature representation
- Mel spectrogram
- MFCC features
- Spectral centroid / bandwidth
- Zero crossing rate
- Energy features
- Optional pitch estimation

### CNN structure
- Input layer
- Conv2D block
- BatchNormalization
- ReLU
- MaxPooling
- Additional convolution blocks
- Dropout
- GlobalAveragePooling
- Dense layer
- Sigmoid output

### Output
- 0 = REAL
- 1 = AI/SPOOF

### Training settings
- Binary cross entropy
- Adam optimizer
- Early stopping
- Model checkpoint
- Validation-based threshold tuning

## Important note

This repository contains a production-ready project structure and a demo pipeline. The actual trained model should be trained on a public spoof dataset such as ASVspoof 2019 or 2021 DF, with honest evaluation and unseen dataset testing before claiming results.
