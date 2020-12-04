import React,{useState , useEffect} from 'react'
import UpdateData,{GetdataProps} from '../../../services/subirData/updateData'

function Input(props){
    
    const [Nbutton,setNbutton] = useState(0)
    const [sense,setSense] = useState({itsGoing : '' , numberOfGuest : 1})
    const [animation,setAnimation] = useState ("btn-secondary")

    const getData = GetdataProps(Nbutton);

    useEffect(()=>{
        console.log(getData);
        const ani = getData ?  "btn-danger":"btn-success" 
        setAnimation(ani)
    },[getData])

    useEffect(() => {
        setNbutton(props.numero)
    }, [props.numero])

    const handleInputChange = evt =>{
        const target = evt.target;
        const name = target.checked;
        console.log(name);
        UpdateData({num: Nbutton, state: name})
        setSense({itsGoing : name,numberOfGuest : sense.numberOfGuest + 1 })
        // const animation = target.checked ? "btn-danger" : "btn-success" 
        // setAnimation(animation)
    }

    return(
        <label className = {`btn ${animation} btn-rounded form-check-label`}>
            <span>ROCIADOR{`${Nbutton}`}</span>
            <input type="checkbox" checked = {getData} name="isGoing" className="form-check-input input-button" value={sense.itsGoing} onChange={handleInputChange} autoComplete="off"/>
        </label>
    )
}

export default Input