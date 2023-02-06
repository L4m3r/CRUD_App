from fastapi import FastAPI
from .database import engine
from . import artist, models, album

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(artist.router, tags=['artists'], prefix='/artists')
app.include_router(album.router, tags=['albums'], prefix='/albums')


@app.get('/')
def root():
    return {'message': 'Ok!'}
