# VOXSHIELD System Architecture

## 1. Overview

VOXSHIELD is an AI-powered voice impersonation detection and prevention platform designed for SIH demonstrations. The system combines audio signal processing, spoof detection, speaker verification, risk assessment, and prevention logic.

## 2. Core pipeline

1. Audio input
2. Preprocessing
3. Feature extraction
4. Spoof classification
5. Speaker verification
6. Risk scoring
7. Prevention decision
8. Dashboard reporting

## 3. Components

### Frontend
- React + TypeScript
- Tailwind CSS
- Recharts
- Lucide icons

### Backend
- FastAPI
- WebSocket support
- REST endpoints for analysis and model status

### ML engine
- TensorFlow/Keras CNN model
- Librosa + NumPy + SciPy feature extraction
- Real-time and offline inference path

### Data layer
- Metadata-driven dataset organization
- Dataset validation and quality checks
- Speaker-disjoint split logic

## 4. Security flow

- A voice sample is analyzed for authenticity.
- The system checks whether the claimed speaker matches a known enrollment profile.
- A risk score is computed based on all relevant signals.
- The prevention engine decides whether to allow, monitor, or block the request.

## 5. Demo mode

Demonstrations intentionally show a clear distinction between real inference and simulated demo outputs. If the trained model is unavailable, the system displays DEMO SIMULATION and clearly labels it.
