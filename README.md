# FastAPI w/ MySQL - Quickstart Boilerplate

Clone this repository to your local computer.

If you don't have a pipenv, run
```
pip install pipenv
```

Navigate to your project folder on cmd or powershell.

To Activate the shell and install the packages, run
```
pipenv install
```

(The ASGI server used here is Uvicorn. You can also use Hypercorn instead.)

Start your server
```
uvicorn main:app --reload
```

On your browser, head over to
http://127.0.0.1:8000

You can also view your API docs here.
http://127.0.0.1:8000/docs
or
http://127.0.0.1:8000/redoc

![image](https://user-images.githubusercontent.com/67852344/137637131-a56cdb8b-cbc8-4cb2-808b-ae86dfe0bcff.png)

