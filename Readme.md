## Setup Environment - Shell/Terminal
```
mkdir submission_analisis_data
cd submission_analisis_data
python -m venv venv
venv\Scripts\activate.bat
Get-ChildItem -Path venv\Scripts
Set-ExecutionPolicy Unrestricted -Scope Process
.\venv\Scripts\Activate
pip install -r requirements.txt

```

## Run steamlit app
```
streamlit run Dashboard/dashboard.py
```
