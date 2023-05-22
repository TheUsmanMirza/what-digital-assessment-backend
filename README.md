## What Digital Assessment Backend App

## Setup Project

1. Clone the project using following command
```
git clone https://github.com/TheUsmanMirza/what-digital-assessment-backend.git

2. Make sure you have python 3 installed in your system

3. Create Virtual Environment in the project Directory
```
python -m venv {{virtual_env}}
```

4. Activate Environment
```
source {{virtual_env}}/bin/activate
```

5. Install Required Dependencies
```
pip install -r requirements.txt
```

6. Run following command to run server
```
python manage.py runserver
```


## How to Run on Docker
- Run Command to Create Image :
```
docker build -t what_ds_backend .
```
- Run app on docker
```
docker run -p 8000:8000 what_ds_backend
```

## Avalibale Existing User in Sqlite DB
email: admin@gmail.com
password: testpassword

## Avaliable Existing Product
1- Wheat
2- Coco Powder
3- Dairy Milk
