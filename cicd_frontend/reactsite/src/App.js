import { useState } from 'react';
import ListaArtistas from './components/ListaArtistas.js';
import ListaAlbuns from './components/ListaAlbuns.js';
import ListaMusicas from './components/ListaMusicas.js';
import ListaPlaylists from './components/ListaPlaylists.js';
import './App.css';
import ListaItens from './components/ListaItens.js';

function App() {

  const[idArtista, setIdArtista] = useState("none");
  const[idAlbum, setIdAlbum] = useState("none");
  const[idMusica, setIdMusica] = useState("none");
  const[idPlaylist, setIdPlaylist] = useState("none");
  
  const handleArtista = (artista) => {
    setIdArtista(artista);
  }

  const handleAlbum = (album) => {
    setIdAlbum(album);
  }

  const handleMusica = (musica) => {
    setIdMusica(musica);
  }

  const handlePlaylist = (playlist) => {
    setIdPlaylist(playlist);
  }

  return (
    <div className="App">
      <div className='App-Content'>
          <ListaArtistas handleArtista={handleArtista} handleAlbum={handleAlbum} />
          <ListaAlbuns idArtista={idArtista} handleAlbum={handleAlbum}/>
          <ListaMusicas idAlbum={idAlbum} handleMusica={handleMusica} />
          <ListaPlaylists handlePlaylist={handlePlaylist} />
          <ListaItens idPlaylist={idPlaylist} idMusica={idMusica} />
      </div>
    </div>
  );
}

export default App;
