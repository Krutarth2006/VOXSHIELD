# VOXSHIELD

VOXSHIELD is an AI-powered real-time voice impersonation detection and prevention system for SIH demonstration.

This repository contains a complete starter implementation with:
- FastAPI backend
- ML model pipeline skeleton
- React + TypeScript frontend
- Risk engine and prevention logic
- Demo mode and threat monitoring mock data

## Project structure

- frontend/: React app
- backend/: FastAPI backend
- ml/: training, preprocessing, and inference logic
- models/: saved model artifacts
- experiments/: evaluation results
- reports/: generated reports
- dataset/: dataset metadata and data management scripts

## Quick start

### 1) Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 2) Frontend

```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0
```

## Demo note

This project is designed as a realistic SIH demonstrator. The ML model is implemented as a project-ready pipeline and uses a lightweight synthetic detector by default when no large public dataset is available locally. Replace the placeholder model with a trained ASVspoof or WaveFake-backed model for full competition-grade performance.

## Important

- Do not claim 100% detection accuracy.
- Use the demo mode clearly when running simulated scenarios.
- Keep speaker verification and spoof detection separate.
