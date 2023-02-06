from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db

router = APIRouter()


@router.get('/', response_model=list[schemas.Artist])
def get_artists(db: Session = Depends(get_db)):
    artists = db.query(models.Artist).all()
    return artists


@router.get('/{artist_id}', response_model=schemas.Artist)
def get_artist(artist_id: int, db: Session = Depends(get_db)):
    artist = db.query(models.Artist).filter(models.Artist.id == artist_id).first()
    if not artist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Artist: {artist_id} not found')

    return artist


@router.post('/', response_model=schemas.Artist, status_code=status.HTTP_201_CREATED)
def create_artist(payload: schemas.ArtistBase, db: Session = Depends(get_db)):
    new_artist = models.Artist(**payload.dict())
    db.add(new_artist)
    db.commit()
    db.refresh(new_artist)
    return new_artist


@router.put('/{artist_id}', response_model=schemas.Artist)
def update_artist(artist_id: int, payload: schemas.ArtistBase, db: Session = Depends(get_db)):
    artist_query = db.query(models.Artist).filter(models.Artist.id == artist_id)
    artist = artist_query.first()

    if not artist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Artist: {artist_id} not found')

    update_data = payload.dict(exclude_unset=True)
    artist_query.update(update_data, synchronize_session=False)

    db.commit()
    db.refresh(artist)
    return artist


@router.delete('/{artist_id}')
def delete_artist(artist_id: int, db: Session = Depends(get_db)):
    artist_query = db.query(models.Artist).filter(models.Artist.id == artist_id)
    artist = artist_query.first()

    if not artist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Artist: {artist_id} not found')

    artist_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
