Write-Host "Starting up!\n\nInstalling Requirements!\n\n"
python -m pip install -r ./requirements.txt
$FLASK_APP='app.py'
python -m flask run --port=5000 
