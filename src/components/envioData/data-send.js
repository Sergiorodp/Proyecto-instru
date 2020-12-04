import React from 'react'
// import Datarender from '../data/data';

// Components
import Input from './data-checkbox/data-checkbox'


function SendData(props){

    let nComponents = []

    for(let i = 0 ; i < props.num;i++){
        nComponents[i] = i+1;
    }

    const handelSubmit = evt =>{
        evt.preventDefault()
        console.log("ENTRE");
    }

    const mapInput = nComponents.map(num =>{
        return (<Input key = {num} numero = {num}/>)
    })

    return(
        <form onSubmit={handelSubmit} className = "p-1">
            <div className="btn-group " data-toggle="buttons">
                {mapInput}
            </div>
        </form>
    )
}
export default SendData;