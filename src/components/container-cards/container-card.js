import React,{useState, useEffect,lazy,Suspense} from 'react'
// import Datarender from '../data/data';

import getData  from '../../services/consult'
const StreamSchart = lazy(() => import('./chart/chart'))

var dataArray = [0,0,0,0,0,0,0,0,0,0]

// const home = 'https://sergiorodp.github.io/Proyecto-instru/'
const home = '/Proyecto-instru/'

const Card = React.memo( function Card({params}){

    const [sense,setSense] = useState({
        valor : 0,
        nombre : "cargando...",
        vecesprendido : 0,
    })

    const keyWord = params.key
    // console.log(params);
    
    useEffect(() => {
        getData().ref(`quiz/eladc${keyWord}`).on("value",(snap) => {
            const data = snap.val()
            const dataplus = {
                valor : data.valor,
                promedio : data.prom,
                nombre : data.nombre,
                masinfo : `ADC numero ${keyWord}`,
            }
            dataArray.shift() 
            dataArray.push( data.valor)
            // console.log(data);
            setSense(dataplus);
        })
    }, [keyWord])

    return(
    <div className = "card">
        <div className = "card-header">
    <h2 className = "aqua"> SENSOR : {sense.nombre}</h2>
            </div>
                <div className = " card-body">
                    <p>Valor: {sense.valor}</p>
                    <p>promedio: {sense.promedio}</p> 
                    <p>Mas info: {sense.masinfo}</p>
                    <Suspense fallback = {<p>cargando... </p>}> 
                        <StreamSchart num = {sense.valor} arrayLol = {dataArray}/>
                    </Suspense>
                </div>
            <div className = "card-footer">
                <a href = {`${home}`}>pagina principal</a>
        </div>
    </div>
    )

})
export default Card;
