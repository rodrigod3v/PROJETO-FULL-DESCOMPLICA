from typing import List, Union

from .entity import models
from .functions import itemfunction, playlistfunction

from fastapi import Depends, FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .entity import schemas
from .data.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/playlists", status_code = status.HTTP_201_CREATED, response_model=schemas.Playlist)
def postPlaylist(playlist: schemas.PlaylistCreate, db: Session = Depends(get_db)):
    return playlistfunction.create_Playlist(db=db, playlist=playlist)

@app.put("/api/playlists/{id}", status_code = status.HTTP_200_OK, response_model=schemas.Playlist)
def putPlaylist(id:int, newPlaylist: schemas.PlaylistCreate, db: Session = Depends(get_db)):
    return playlistfunction.update_Playlist(db=db, id=id, newPlaylist=newPlaylist)

@app.get("/api/playlists", status_code = status.HTTP_200_OK, response_model=List[schemas.Playlist])
def getPlaylists(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return playlistfunction.read_Playlists(db=db, skip=skip, limit=limit)

@app.get("/api/playlists/{id}", status_code = status.HTTP_200_OK, response_model=schemas.Playlist)
def getPlaylist(id: int, db: Session = Depends(get_db)):
    return playlistfunction.read_Playlist(db=db, id=id)

@app.delete("/api/playlists/{id}", status_code = status.HTTP_204_NO_CONTENT, response_class=Response)
def deletePlaylist(id: int, db: Session = Depends(get_db)):
    return playlistfunction.delete_Playlist(db=db, id=id)

@app.post("/api/itens", status_code = status.HTTP_201_CREATED, response_model=schemas.Item)
def postItem(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return itemfunction.create_Item(db=db, item=item)

@app.put("/api/itens/{id}", status_code = status.HTTP_200_OK, response_model=schemas.Item)
def putItem(id:int, newItem: schemas.ItemCreate, db: Session = Depends(get_db)):
    return itemfunction.update_Item(db=db, id=id, newItem=newItem)

@app.get("/api/itens", status_code = status.HTTP_200_OK, response_model=List[schemas.Item])
def getItens(idPlaylist: Union[str, None] = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return itemfunction.read_Itens(db=db, skip=skip, limit=limit, idPlaylist=idPlaylist)

@app.get("/api/itens/{id}", status_code = status.HTTP_200_OK, response_model=schemas.Item)
def getIem(id: int, db: Session = Depends(get_db)):
    return itemfunction.read_Item(db=db, id=id)

@app.delete("/api/itens/{id}", status_code = status.HTTP_204_NO_CONTENT, response_class=Response)
def deleteItem(id: int, db: Session = Depends(get_db)):
    return itemfunction.delete_Item(db=db, id=id)