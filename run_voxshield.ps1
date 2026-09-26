$backend = "G:\Voice Detection\voxshield\backend"
$frontend = "G:\Voice Detection\voxshield\frontend"

Write-Host "Starting VOXSHIELD backend..."
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$backend'; `$env:PYTHONPATH='$($backend | Split-Path)'; & '.\.venv310\Scripts\python.exe' -m uvicorn app.main:app --host 0.0.0.0 --port 8000"

Write-Host "Starting VOXSHIELD frontend..."
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$frontend'; npm.cmd run dev -- --host 0.0.0.0"

Write-Host "VOXSHIELD started. Open http://localhost:5173"
