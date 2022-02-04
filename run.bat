cd .
CALL venv\Scripts\activate
python run.py
set FLASK_ENV=development
start "" http://127.0.0.1:5000/
python -m flask run