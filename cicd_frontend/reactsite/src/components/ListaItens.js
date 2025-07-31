import React, { useState, useEffect } from 'react';
import { useFetch } from "../hooks/useFetch";
import PythonApiUrl from "../api/PythonApiUrl";

const ListaItens = ({ idPlaylist, idMusica }) => {
    const { data: itens, dataItem: item, httpConfig, loading } = useFetch(PythonApiUrl("/itens"), "?idPlaylist=" + idPlaylist);
    
    const adicionarItem = () => {
        const novoItem = {
            idMusica,
            idPlaylist,
        };
        httpConfig(novoItem, "POST", null);
    }

    const excluirItem = () => {
        if (item !== null)
            httpConfig(null, "DELETE", item.id);
    }

    return (
        <div id="item">
            <h1>Itens</h1>
            {loading && <p>Carregando itens...</p>}
            <ul>
                {itens && itens.map((item) => (
                    <li key={item.id} id={item.id} onClick={(e) => httpConfig(null, "GET", e.target.id)}>
                        {item.idMusica}
                    </li>
                ))}
            </ul>
            <br/>
            <div>
                <button onClick={adicionarItem}>Adicionar</button>
                <button onClick={excluirItem}>Excluir</button>
            </div>
        </div>
    )
};

export default ListaItens;