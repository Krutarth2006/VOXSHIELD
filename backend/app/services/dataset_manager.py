from pathlib import Path


def generate_dataset_report(dataset_root: str) -> dict:
    root = Path(dataset_root)
    real_files = list(root.glob('real/**/*.wav')) + list(root.glob('real/**/*.mp3'))
    spoof_files = list(root.glob('spoof/**/*.wav')) + list(root.glob('spoof/**/*.mp3'))

    return {
        'dataset_root': dataset_root,
        'total_files': len(real_files) + len(spoof_files),
        'real_files': len(real_files),
        'spoof_files': len(spoof_files),
        'class_balance': 'imbalanced-unless-dataset-is-balanced',
        'status': 'metadata-driven-pipeline-ready',
    }
