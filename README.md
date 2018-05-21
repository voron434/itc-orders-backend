# How to run
You should install python 3.6 from [here](https://www.python.org/). 
Than install virtualenv:
```$ [sudo] pip install virtualenv```
After that clone repo and add new venv for it:
```
git clone https://github.com/voron434/itc-orders-backend
cd itc-orders-backend/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install wheel
```
You should run ```source venv/bin/activate``` every time you want to use thise code to modify your command line to:
```(venv) $```. To stop venv you should use ```(venv) $ deactivate```

```python manage.py migrate``` - to migrate your database
```python manage.py runserver``` - to run server

Quickstart:
```
pip install virtualenv
git clone https://github.com/voron434/itc-orders-backend
cd itc-orders-backend/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install wheel
python manage.py migrate
python manage.py runserver
```
