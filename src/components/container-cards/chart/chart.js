import React,{useState,useEffect} from 'react'
import { Line }  from 'react-chartjs-2';

// import anychart from 'anychart'

const initialize = <Line data = {{
    labels : ['antes','','','','','','','','','Ahora'],
    datasets : [{
        labels : 'ADC',
        fill: false,
        lineTension: 0.1,
        backgroundColor: 'rgba(75,192,192,0.4)',
        borderColor: 'rgba(75,192,192,1)',
        borderCapStyle: 'butt',

        data : [0,0,0,0,0,0,0,0,0,0],
    }]
}}/>

function StreamSchart(props){

    const [stateBar, setstateBar] = useState(initialize)

    useEffect(() => {
        buildchart()
        // eslint-disable-next-line
    }, []) 

    const buildchart = () =>{

        setInterval(function(){
            // var oldDataSet = stateBar.datasets[0];
    
            // var newDataSet = {
            //     ...oldDataSet
            // };
            // newDataSet.data = props.arrayLol;
    
            // var newState = {
            //     ...initialize,
            //     datasets: [newDataSet]
            // };

            console.log(props); 

            setstateBar(<Line className="graf-adc" key = {props.arrayLol} data = {{
                labels : ['antes','','','','','','','','','Ahora'],
                datasets : [{
                    labels : 'ADC',
                    fill: false,
                    lineTension: 0.1,
                    backgroundColor: 'rgba(75,192,192,0.4)',
                    borderColor: 'rgba(75,192,192,1)',
                    borderCapStyle: 'butt',
                    borderDash: [],
                    data : props.arrayLol,
                }]
            }}
            options = {{
                tooltips:{mode:'nearest'},
                hover: {mode : null},
                animation : {duration : 100}
            }}
            />)// console.log("nuevo data set")
            
        },1000)
    }


    return(
    <div className = "grafancho ml-auto mr-auto">
        {stateBar}
    </div>
    )
}

export default StreamSchart
