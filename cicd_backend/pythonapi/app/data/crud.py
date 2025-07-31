from typing import Union
from sqlalchemy.orm import Session

from ..entity import models
from ..entity import schemas

def create_Playlist(db: Session, playlist: schemas.PlaylistCreate):
    db_Playlist = models.Playlist(descricao=playlist.descricao)
    db.add(db_Playlist)
    db.commit()
    db.refresh(db_Playlist)
    return db_Playlist

def update_Playlist(db: Session, playlist: any, newPlaylist: schemas.PlaylistCreate):
    playlist.descricao = newPlaylist.descricao
    db.commit()
    return playlist

def get_Playlists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Playlist).offset(skip).limit(limit).all()

def get_Playlist(db: Session, id: int):
    return db.query(models.Playlist).filter(models.Playlist.id == id).first()

def get_Playlist_by_Descricao(db: Session, descricao: str):
    return db.query(models.Playlist).filter(models.Playlist.descricao == descricao).first()

def delete_Playlist(db: Session, id: int):
    playlist = db.query(models.Playlist).filter(models.Playlist.id == id).first()
    db.delete(playlist)
    db.commit()
    return None

def create_Item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_Item(db: Session, item: any, newItem: schemas.ItemCreate):
    item.idMusica = newItem.idMusica
    db.commit()
    return item

def get_Itens(db: Session, skip: int = 0, limit: int = 100, idPlaylist: Union[str, None] = None):
    if idPlaylist is None:
        return db.query(models.Item).offset(skip).limit(limit).all()
    else:
        return db.query(models.Item).filter(models.Item.idPlaylist == idPlaylist).offset(skip).limit(limit).all()

def get_Item(db: Session, id: int):
    return db.query(models.Item).filter(models.Item.id == id).first()

def get_Item_by_IdPlaylist(db: Session, idPlaylist: str, skip: int = 0, limit: int = 100):
    return db.query(models.Item).filter(models.Item.idPlaylist == idPlaylist).offset(skip).limit(limit).all()

def get_Item_by_IdMusica(db: Session, idMusica: int):
    return db.query(models.Item).filter(models.Item.idMusica == idMusica).first()

def delete_Item(db: Session, id: int):
    item = db.query(models.Item).filter(models.Item.id == id).first()
    db.delete(item)
    db.commit()
    return None