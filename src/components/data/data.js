import React from 'react'
import { useEffect, useState } from 'react'

import getData from '../../services/consult'
import SendData from '../envioData/data-send'


// Pagina principal 

// const home = 'https://sergiorodp.github.io/Proyecto-instru/'
const home ='/Proyecto-instru/'

function Datarender(){

    const [valor,setValor] = useState([{nombre : "Cargando...", valor : 0 , vecesprendido : 0,pos : 0, link:'/'}]);
    const [Nsensores,setNsensores] = useState(0)

    useEffect(() => {
        getData().ref(`quiz`).on("value",(snapshot) => {
            const data = []
            const ndata = snapshot.val()
            setNsensores(ndata.nDatos)
            for (let i = 0; i < ndata.nDatos; i++){
                const temp = snapshot.child(`eladc${i+1}`).val()
                data[i] = { 
                    nombre : temp.nombre,
                    valor : temp.valor,
                    prom : temp.prom,
                    masinfo : "aca esta la info",
                    pos : (i+1), 
                    link : `${home}sensor${i+1}`
                }
            }
            setValor(data)
        })
    },[])

    const sensorList = valor.map(sensores => {
        return (
            <div key = {sensores.nombre} className = "card pb-2 pt-2 mr-auto ml-auto">
                <div className="card-header">
                    <h3>{sensores.nombre}</h3>
                </div>
                <div className = "card-body">
                    <p className="aqua">valor : {sensores.valor}</p>
                    <p>prom : {sensores.prom}</p>
                </div>
                <div className="card-footer">
                    <a href = {sensores.link} className="aqua">más info</a>
                </div>
            </div>
        )
    })

    let clase;
    clase = "organize-cards" 

    return(    
    <div className = "card">
        <div className = "card-header">
            <h2 className = "aqua">Mediciones</h2>
        </div>
        <div className = {`card-body ${clase}`}>
            {sensorList}
        </div>
        <div className = "card-footer">
            <SendData num = {Nsensores}/>
        </div>
    </div>
            
        
    )
} 

export default Datarender
