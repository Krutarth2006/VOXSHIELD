import argparse
from pathlib import Path

from ml.preprocessing.processor import build_preprocessing_config
from ml.training.trainer import train_voice_detector


def main() -> None:
    parser = argparse.ArgumentParser(description='VOXSHIELD Model Training Pipeline')
    parser.add_argument('--manifest', type=Path, default=None, help='Path to manifest CSV')
    parser.add_argument('--limit', type=int, default=None, help='Optional row limit')
    args = parser.parse_args()

    print('VOXSHIELD training pipeline started')
    config = build_preprocessing_config(sample_rate=16000, duration_seconds=4.0)
    print('Preprocessing config:', config)
    result = train_voice_detector(random_seed=7, manifest_path=args.manifest, limit=args.limit)
    print('Training result:', result)

    reports_dir = Path('reports')
    reports_dir.mkdir(exist_ok=True)
    Path('reports/model_training_status.txt').write_text(str(result), encoding='utf-8')
    print('Training status saved to reports/model_training_status.txt')


if __name__ == '__main__':
    main()
