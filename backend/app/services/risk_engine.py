from dataclasses import dataclass


@dataclass
class RiskAssessment:
    risk_score: int
    risk_level: str
    decision: str
    recommended_action: str


def assess_risk(synthetic_probability: float, speaker_match: float, audio_quality: float = 0.8, anomalies: float = 0.1) -> RiskAssessment:
    score = (
        synthetic_probability * 60
        + (1 - speaker_match) * 25
        + (1 - audio_quality) * 10
        + anomalies * 15
    )
    risk_score = max(0, min(100, int(score)))

    if risk_score >= 80:
        return RiskAssessment(risk_score, 'CRITICAL', 'BLOCK', 'SECONDARY_VERIFICATION')
    if risk_score >= 60:
        return RiskAssessment(risk_score, 'HIGH', 'MONITOR', 'MANUAL_REVIEW')
    if risk_score >= 35:
        return RiskAssessment(risk_score, 'MEDIUM', 'ALLOW_WITH_ALERT', 'OTP_VERIFICATION')
    return RiskAssessment(risk_score, 'LOW', 'ALLOW', 'ALLOW')
