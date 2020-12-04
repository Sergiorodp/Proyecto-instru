import getData from '../consult'
import {useState,useEffect} from 'react'


function UpdateData(props){
    // console.log("Las prosp de get son");
    console.log(props);
    getData().ref(`Leds/N${props.num}`).update({state : props.state})
}

function GetdataProps(props){
    
    const [GetD, setGetD] = useState({state : false})

    console.log(props)

    useEffect(() => {
        if(props !== 0){
            getData().ref(`Leds/N${props}`).on("value",snap =>{
                const Data = snap.val()
                console.log(Data);
                setGetD(Data)
            })
        }
        },[props])

    return(GetD.state)
}

export {GetdataProps}
export default UpdateData