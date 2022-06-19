from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': {'name': "akil"}}


@app.get('/about')
def about():
    return {'data': {"age": 26}}