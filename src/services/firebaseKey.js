// import firebase from 'firebase'

// var admin = require("firebase-admin");

// var serviceAccount = require("../services/key/key.json");

// admin.initializeApp({
//     credential: admin.credential.cert(serviceAccount),
//     databaseURL: "https://test-java-python.firebaseio.com/"
// });

// const db = admin.database();

// export default function getDataFire(){
//     return(
//         db.ref('quiz').on("value")
//         .then((snapshot)=>{
//             var dataRes = snapshot.value()
//             return dataRes
//         })
//     )
// }


export const DB_CONFIG = {
    apiKey: "AIzaSyC7Sdn3R-fW5KS-2ucCwzpGnB0HYKElHDM",
    authDomain: "test-java-python.firebaseapp.com",
    databaseURL: "https://test-java-python.firebaseio.com",
    projectId: "test-java-python",
    storageBucket: "test-java-python.appspot.com",
    messagingSenderId: "167375922955",
    appId: "1:167375922955:web:6ba473481c885a4da2e40e"
} 