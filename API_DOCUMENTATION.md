# VOXSHIELD API Documentation

## Endpoints

### GET /system-status
Returns current backend system state.

### GET /threats
Returns a list of active or recent threats.

### GET /reports
Returns available reports.

### POST /analyze-audio
Analyzes a voice sample and returns:
- authentic_probability
- synthetic_probability
- speaker_match
- risk_score
- risk_level
- decision
- recommended_action

### POST /verify-speaker
Checks whether the voice matches the claimed speaker.

### POST /enroll-speaker
Enrolls a new speaker for verification.

### WebSocket /ws/live-detection
Streams live detection updates.

## Example response

```json
{
  "authentic_probability": 0.08,
  "synthetic_probability": 0.92,
  "speaker_match": 0.31,
  "risk_score": 94,
  "risk_level": "CRITICAL",
  "decision": "BLOCK",
  "recommended_action": "SECONDARY_VERIFICATION"
}
```
