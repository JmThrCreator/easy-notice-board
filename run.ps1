PowerShell.exe -windowstyle hidden {
    python run.py
    cd .
    venv\Scripts\activate
    start http://127.0.0.1:5000/
    python -m flask run
}