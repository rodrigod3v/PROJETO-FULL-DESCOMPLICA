from typing import Any, List
from ..data import crud
from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..entity import schemas

def create_Playlist(db: Session, playlist: schemas.PlaylistCreate):
    db_Playlist = crud.get_Playlist_by_Descricao(db, descricao=playlist.descricao)
    valida_Playlist_JaExistente(db_Playlist=db_Playlist, descricao=playlist.descricao)
    return crud.create_Playlist(db=db, playlist=playlist)

def update_Playlist(db: Session, id: int, newPlaylist: schemas.PlaylistCreate):
    db_Playlist = crud.get_Playlist(db=db, id=id)
    valida_Playlist_NaoEncontrada(db_Playlist=db_Playlist, id=id)
    db_PlaylistDescricao = crud.get_Playlist_by_Descricao(db=db, descricao=newPlaylist.descricao)
    valida_Playlist_JaExistente(db_Playlist=db_PlaylistDescricao, descricao=newPlaylist.descricao)
    return crud.update_Playlist(db=db, playlist=db_Playlist, newPlaylist=newPlaylist)

def read_Playlists(db: Session, skip: int, limit: int):
    playlists = crud.get_Playlists(db=db, skip=skip, limit=limit)
    return playlists

def read_Playlist(db: Session, id: int):
    db_Playlist = crud.get_Playlist(db=db, id=id)
    valida_Playlist_NaoEncontrada(db_Playlist=db_Playlist, id=id)
    return db_Playlist

def delete_Playlist(db: Session, id: int):
    db_Playlist = crud.get_Playlist(db=db, id=id)
    valida_Playlist_NaoEncontrada(db_Playlist=db_Playlist, id=id)
    crud.delete_Playlist(db=db, id=id)
    return

def valida_Playlist_NaoEncontrada(db_Playlist: List, id: int):
    if db_Playlist is None:
        raise HTTPException(status_code=404, detail="Playlist não encontrada. Id: " + str(id))

def valida_Playlist_JaExistente(db_Playlist: Any, descricao: str):
    if db_Playlist:
        raise HTTPException(status_code=400, detail="Playlist já existe. Descrição: " + descricao)