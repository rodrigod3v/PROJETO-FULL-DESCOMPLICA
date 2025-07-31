from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..data.database import Base

class Playlist(Base):
    __tablename__ = "Playlist"
    id = Column("Id", Integer, primary_key=True, index=True)
    descricao = Column("Descricao", String(100), unique = True, index=True)
    itens = relationship("Item", back_populates="playlist")

class Item(Base):
    __tablename__ = "Item"
    id = Column("Id", Integer, primary_key=True, index=True)
    idMusica = Column("Id_Musica", Integer)
    idPlaylist = Column("Id_Playlist", Integer, ForeignKey("Playlist.Id"))
    playlist = relationship("Playlist", back_populates="itens")