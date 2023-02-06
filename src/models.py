from .database import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Artist(Base):
    __tablename__ = 'Artist'
    id = Column('ArtistId', Integer, primary_key=True)
    name = Column('Name', String, nullable=False)

    albums = relationship("Album", back_populates="artist")


class Album(Base):
    __tablename__ = 'Album'
    id = Column('AlbumId', Integer, primary_key=True)
    title = Column('Title', String, nullable=False)
    artist_id = Column('ArtistId', Integer, ForeignKey('Artist.ArtistId'))

    artist = relationship("Artist", back_populates="albums")
