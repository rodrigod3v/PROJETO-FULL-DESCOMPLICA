from typing import Any, List
from pydantic import BaseModel

class ItemBase(BaseModel):
    id: int
    idMusica: int

class PlaylistBase(BaseModel):
    id: int
    descricao: str

class Item(ItemBase):
    ...
    playlist: Any

    class Config:
        orm_mode = True

class Playlist(PlaylistBase):
    ...

    class Config:
        orm_mode = True

class PlaylistCreate(BaseModel):
    descricao: str

class ItemCreate(BaseModel):
    idMusica: int
    idPlaylist:int