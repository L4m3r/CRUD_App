# CRUD_App

This is simple [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) app
using open [database](https://github.com/lerocha/chinook-database).

## Installation and running

```shell
git clone https://github.com/L4m3r/crud_app.git
cd crud_app
pip install -r requirements.txt
cd src
uvicorn main:app --host localhost --port 8000 --reload
```

FastAPI server will start on `127.0.0.1:8000`

## TO-DO

- [ ] Add authentication
- [ ] Add all models 
