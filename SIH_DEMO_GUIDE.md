# SIH Demo Guide

## Scenario 1: Genuine voice
- Open dashboard.
- Start live detection.
- Use a genuine enrolled voice sample.
- Expect authenticity to remain high and risk to remain low.

## Scenario 2: AI clone / impersonation attempt
- Trigger a synthetic sample.
- Expect high synthetic probability and low speaker match.
- Risk should escalate to critical.
- The system blocks the action and asks for secondary verification.

## Scenario 3: Unknown speaker
- Use a voice that is not enrolled.
- Speaker verification should reject the user.
- The system raises medium or high risk.

## Demo narrative

1. Dashboard overview
2. Live detection step
3. Genuine voice sample
4. AI clone scenario
5. Threat detection and blocking
6. Secondary verification instructions
7. Threat monitoring and report summary
