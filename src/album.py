from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db

router = APIRouter()


@router.get('/', response_model=list[schemas.AlbumList])
def get_albums(db: Session = Depends(get_db)):
    albums = db.query(models.Album).all()
    return albums


@router.get('/{album_id}', response_model=schemas.Album)
def get_album(album_id: int, db: Session = Depends(get_db)):
    album = db.query(models.Album).filter(models.Album.id == album_id).first()
    if not album:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Album: {album_id} not found')

    return album


@router.post('/', response_model=schemas.Album)
def create_album(payload: schemas.AlbumCreate, db: Session = Depends(get_db)):
    new_album = models.Album(**payload.dict())
    db.add(new_album)
    db.commit()
    db.refresh(new_album)
    return new_album


@router.put('/{album_id}', response_model=schemas.Album)
def update_album(album_id: int, payload: schemas.AlbumUpdate, db: Session = Depends(get_db)):
    album_query = db.query(models.Album).filter(models.Album.id == album_id)
    album = album_query.first()

    if not album:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Album: {album_id} not found')

    update_data = payload.dict(exclude_unset=True)
    album_query.update(update_data, synchronize_session=False)

    db.commit()
    db.refresh(album)
    return album


@router.delete('/{album_id}')
def delete_artist(album_id: int, db: Session = Depends(get_db)):
    album_query = db.query(models.Album).filter(models.Album.id == album_id)
    album = album_query.first()

    if not album:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Album: {album_id} not found')

    album_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
