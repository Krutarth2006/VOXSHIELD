import sys
from pathlib import Path

from ml.training.trainer import predict_voice_sample


def main():
    if len(sys.argv) < 2:
        print('Usage: python predict.py <audio_file>')
        raise SystemExit(1)

    audio_path = Path(sys.argv[1])
    if not audio_path.exists():
        print(f'Audio file not found: {audio_path}')
        raise SystemExit(1)

    result = predict_voice_sample(str(audio_path))
    print('VOXSHIELD prediction')
    print(f'Input: {audio_path}')
    print(f"Authentic Probability: {result['authentic_probability'] * 100:.2f}%")
    print(f"Synthetic Probability: {result['synthetic_probability'] * 100:.2f}%")
    print(f"Speaker Match: {result['speaker_match'] * 100:.2f}%")
    print(f"Risk Level: {result['risk_level']}")
    print(f"Decision: {result['decision']}")


if __name__ == '__main__':
    main()
