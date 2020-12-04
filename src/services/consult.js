
import firebase from 'firebase'
import {DB_CONFIG} from './firebaseKey'
import 'firebase/database'


const config = firebase.initializeApp(DB_CONFIG)
const db = config.database()

export function nValFuntion(){
    const baseNum = db.ref('quiz').once("value",(snap) =>{
        const nVal = snap.val()
        return nVal.nDatos
    })
    return {baseNum}
}

export default function getData(){
    return db 
}

