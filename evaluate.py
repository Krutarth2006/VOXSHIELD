"""VOXSHIELD Comprehensive Multi-Dataset Evaluation Script.

Evaluates trained model on:
1. ASVspoof 2019 LA Dev Manifest (la_dev.csv)
2. WaveFake / Combined Test Manifest (combined_test.csv)
3. Unseen AI Test Sample (p226_c0022.wav)

Calculates:
- Accuracy, Precision, Recall, F1 Score
- ROC-AUC Score
- Confusion Matrix
- False Negative Rate (FNR)
"""

import csv
import json
from pathlib import Path
from typing import Dict, Any, List

import joblib
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

from ml.preprocessing.processor import extract_audio_features_from_path

PROJECT_ROOT = Path(__file__).resolve().parent
MODEL_PATH = PROJECT_ROOT / "ml" / "models" / "voxshield_voice_detector.joblib"
MANIFEST_DIR = PROJECT_ROOT / "dataset" / "manifests"
REPORTS_DIR = PROJECT_ROOT / "reports"

from ml.training.trainer import load_manifest_dataset

def load_manifest_eval_data(manifest_path: Path, limit: int | None = None) -> tuple[List[np.ndarray], List[int], List[str]]:
    if not manifest_path.exists():
        raise FileNotFoundError(f"Manifest path not found: {manifest_path}")
        
    X_mat, y_arr = load_manifest_dataset(manifest_path, limit=limit, use_cache=True)
    return list(X_mat), list(y_arr), []

def compute_metrics(y_true: np.ndarray, y_pred: np.ndarray, y_prob: np.ndarray) -> Dict[str, Any]:
    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])
    tn, fp, fn, tp = cm.ravel() if cm.size == 4 else (0, 0, 0, 0)
    
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, zero_division=0)
    rec = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)
    
    try:
        roc_auc = roc_auc_score(y_true, y_prob) if len(np.unique(y_true)) > 1 else 1.0
    except Exception:
        roc_auc = 0.5
        
    fnr = fn / (fn + tp) if (fn + tp) > 0 else 0.0
    
    return {
        "accuracy": round(float(acc), 4),
        "precision": round(float(prec), 4),
        "recall": round(float(rec), 4),
        "f1_score": round(float(f1), 4),
        "roc_auc": round(float(roc_auc), 4),
        "false_negative_rate": round(float(fnr), 4),
        "confusion_matrix": {
            "true_negatives": int(tn),
            "false_positives": int(fp),
            "false_negatives": int(fn),
            "true_positives": int(tp)
        },
        "total_samples": int(len(y_true))
    }

def evaluate_model(limit: int | None = None) -> Dict[str, Any]:
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
        
    print(f"Loading model from: {MODEL_PATH}")
    model = joblib.load(MODEL_PATH)
    n_feats = getattr(model, 'n_features_in_', 348)
    
    results = {}
    
    # 1. Evaluate on Combined Test Set
    comb_test_csv = MANIFEST_DIR / "combined_test.csv"
    if comb_test_csv.exists():
        print(f"Evaluating on Combined Test Set ({comb_test_csv})...")
        X, y, _ = load_manifest_eval_data(comb_test_csv, limit=limit)
        if X:
            X_mat = np.vstack(X)[:, :n_feats]
            y_arr = np.array(y)
            probs = model.predict_proba(X_mat)[:, 1] if hasattr(model, "predict_proba") else model.predict(X_mat)
            preds = (probs >= 0.5).astype(int)
            results["combined_test"] = compute_metrics(y_arr, preds, probs)
            
    # 2. Evaluate on ASVspoof LA Dev Set
    la_dev_csv = MANIFEST_DIR / "la_dev.csv"
    if la_dev_csv.exists():
        print(f"Evaluating on ASVspoof LA Dev Set ({la_dev_csv})...")
        X, y, _ = load_manifest_eval_data(la_dev_csv, limit=limit or 1500)
        if X:
            X_mat = np.vstack(X)[:, :n_feats]
            y_arr = np.array(y)
            probs = model.predict_proba(X_mat)[:, 1] if hasattr(model, "predict_proba") else model.predict(X_mat)
            preds = (probs >= 0.5).astype(int)
            results["asvspoof_la_dev"] = compute_metrics(y_arr, preds, probs)
            
    # 3. Evaluate specific unseen sample: p226_c0022.wav
    p226_path = PROJECT_ROOT / "dataset" / "unseen_test" / "p226_c0022.wav"
    if not p226_path.exists():
        p226_path = PROJECT_ROOT / "dataset" / "WaveFake" / "fake" / "p226_c0022.wav"
        
    if p226_path.exists():
        print(f"Evaluating unseen AI test file: {p226_path}")
        from ml.training.trainer import predict_voice_sample
        pred_res = predict_voice_sample(str(p226_path))
        prob = pred_res['synthetic_probability']
        decision = pred_res['decision']
        is_correct = (decision == 'BLOCK') # p226_c0022 is AI-generated (spoof = 1) -> must BLOCK
        results["unseen_p226_c0022"] = {
            "file": "p226_c0022.wav",
            "true_label": "spoof (1)",
            "predicted_probability_spoof": prob,
            "decision": decision,
            "predicted_label": "spoof" if decision == 'BLOCK' else "bonafide",
            "correct_classification": is_correct
        }

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_file = REPORTS_DIR / "evaluation_report.json"
    report_file.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"\nSaved evaluation results to: {report_file}")
    
    return results

if __name__ == "__main__":
    eval_res = evaluate_model()
    print("\n" + "="*50)
    print("EVALUATION SUMMARY RESULTS")
    print("="*50)
    print(json.dumps(eval_res, indent=2))
