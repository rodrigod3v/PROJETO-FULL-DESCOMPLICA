from typing import Any, Union
from ..data import crud
from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..entity import schemas

def create_Item(db: Session, item: schemas.ItemCreate):
    db_Item = crud.get_Item_by_IdMusica(db, idMusica=item.idMusica)
    valida_Item_JaExiste(db_Item=db_Item, id=item.idMusica)
    return crud.create_Item(db=db, item=item)

def update_Item(db: Session, id: int, newItem: schemas.ItemCreate):
    db_Item = crud.get_Item_by_IdMusica(db=db, idMusica=newItem.idMusica)
    valida_Item_JaExiste(db_Item=db_Item, id=newItem.idMusica)
    db_Item = crud.get_Item(db=db, id=id)
    valida_Item_NaoEncontrado(db_Item=db_Item, id=id)
    return crud.update_Item(db=db, item=db_Item, newItem=newItem)

def read_Itens(db: Session, skip: int, limit: int, idPlaylist: Union[str, None] = None):
    itens = crud.get_Itens(db=db, skip=skip, limit=limit, idPlaylist=idPlaylist)
    return itens

def read_Item(db: Session, id: int):
    db_Item = crud.get_Item(db=db, id=id)
    valida_Item_NaoEncontrado(db_Item=db_Item, id=id)
    return db_Item

def delete_Item(db: Session, id: int):
    db_Item = crud.get_Item(db=db, id=id)
    valida_Item_NaoEncontrado(db_Item=db_Item, id=id)
    crud.delete_Item(db=db, id=id)
    return

def valida_Item_NaoEncontrado(db_Item: Any, id: int):
    if db_Item is None:
        raise HTTPException(status_code=404, detail="Item não encontrado. Id: " + str(id))

def valida_Item_JaExiste(db_Item: Any, id: int):
    if db_Item:
        raise HTTPException(status_code=400, detail="Item já existe. IdMusica: " + str(id))