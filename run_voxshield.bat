@echo off
title VOXSHIELD Voice Spoofing Detection System Launcher
echo =========================================================
echo       VOXSHIELD AI VOICE SPOOFING DETECTION PLATFORM
echo =========================================================
echo.

cd /d "g:\Voice Detection\voxshield"

echo 1. Starting FastAPI Machine Learning Backend Server...
start "VOXSHIELD Backend API" cmd /k "python -m uvicorn backend.app.main:app --host 0.0.0.0 --port 8000"

echo 2. Starting Vite React Web Dashboard...
cd frontend
start "VOXSHIELD Web Dashboard" cmd /k "npm run dev"

echo 3. Opening VOXSHIELD in your Web Browser...
timeout /t 3 >nul
start http://localhost:5173

echo.
echo =========================================================
echo SUCCESS: VOXSHIELD is active and running!
echo Access anytime at: http://localhost:5173
echo =========================================================
pause
