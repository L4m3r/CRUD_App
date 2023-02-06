from pydantic import BaseModel


class ArtistBase(BaseModel):
    name: str


class Artist(ArtistBase):
    id: int

    class Config:
        orm_mode = True


class AlbumBase(BaseModel):
    title: str


class AlbumCreate(AlbumBase):
    artist_id: int


class AlbumUpdate(AlbumBase):
    title: str | None = None
    artist_id: int | None = None


class AlbumResponse(AlbumBase):
    class Config:
        orm_mode = True


class AlbumList(AlbumResponse):
    artist_id: int


class Album(AlbumResponse):
    id: int
    artist: Artist
