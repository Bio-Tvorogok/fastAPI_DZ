Create and activate virtual environment
```
python3 -m venv env
source env/bin/activate
```
Install requirements
```
pip install -r requirements.txt
```

Start app
```
uvicorn main:APP --host 0.0.0.0 --port 8001 --reload
```

Run test
```
python test.py
```


