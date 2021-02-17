# memo

# virtualenv
설치
```
pip install virtualenv virtualenvwrapper # linux  
pip install virtualenv virtualenvwrapper-win # windows  
```

|명령어|기능|
|---|---|
|mkvirtualenv|생성|
|rmvirtualenv|삭제|
|workon|시작|
|deactivate|종료|


# python unittest
VSCode 
```
{
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        "./tests",
        "-p",
        "test_*.py"
    ],
    "python.testing.pytestEnabled": false,
    "python.testing.nosetestsEnabled": false,
    "python.testing.unittestEnabled": true
}
```
```
python -m unittest tests.test_xxx
```
