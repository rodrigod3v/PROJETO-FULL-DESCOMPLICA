import React, { useState, useEffect } from 'react';
import { useFetch } from "../hooks/useFetch";
import PythonApiUrl from "../api/PythonApiUrl";

const ListaPlaylists = ({ handlePlaylist }) => {
    const { data: playlists, dataItem: playlist, httpConfig, loading } = useFetch(PythonApiUrl("/playlists"), null);
    const [descricao, setDescricao] = useState("");
    
    useEffect(() => {
        async function fetchData() {
            if (playlist !== null)
                setDescricao(playlist.descricao);
        };

        fetchData();
    }, [playlist]);

    const selecionarPlaylist = (e) => {
        httpConfig(null, "GET", e.target.id);
        handlePlaylist(e.target.id);
    }

    const adicionarPlaylist = () => {
        const novaPlaylist = {
            descricao,
        };
        httpConfig(novaPlaylist, "POST", null);
    }

    const alterarPlaylist = () => {
        if (playlist !== null) {
            const novaPlaylist = {
                descricao,
            };

            httpConfig(novaPlaylist, "PUT", playlist.id);
        }
    }

    const excluirPlaylist = () => {
        if (playlist !== null)
            httpConfig(null, "DELETE", playlist.id);
    }

    return (
        <div id="playlist">
            <h1>Playlists</h1>
            {loading && <p>Carregando playlists...</p>}
            <ul>
                {playlists && playlists.map((playlist) => (
                    <li key={playlist.id} id={playlist.id} onClick={selecionarPlaylist}>
                        {playlist.descricao}
                    </li>
                ))}
            </ul>
            <br/>
            <div>
                <p>
                    <label>
                        <span>Playlist: </span>
                        <input 
                            name="playlist"
                            placeholder="Digite o nome da playlist"
                            type="text"
                            value={descricao}
                            onChange={(e) => setDescricao(e.target.value)}/>
                    </label>
                    
                </p>
                <button onClick={adicionarPlaylist}>Adicionar</button>
                <button onClick={alterarPlaylist}>Alterar</button>
                <button onClick={excluirPlaylist}>Excluir</button>
            </div>
        </div>
    )
};

export default ListaPlaylists;