# django-toy-project

## Create project and app
```
django-admin startproject [projectname]
```

```
python manage.py startapp [appname]
```
Register the app in settings.py

## Connect to MySQL databases
start mysql server
```
sudo mysqldsafe
```

Add databases config parameters in `setting.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'toydb',
        'USER': 'root',
        'PASSWORD': 'admin123',
        'HOST': '127.0.0.1',
        'PORT': 3306
    }
}
```
Use the following 2 commands to let django create tables
```
python manage.py makemigrations  
python manage.py migrate
```
or you can use `Tools`->`Run manage.py Task` in Pycharm