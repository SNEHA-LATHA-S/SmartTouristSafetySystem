let latitude = ""
let longitude = ""

function getLocation(){

    if(navigator.geolocation){

        navigator.geolocation.getCurrentPosition(

            function(position){

                latitude = position.coords.latitude
                longitude = position.coords.longitude

                document.getElementById("location")
                .innerHTML = `
                    Latitude: ${latitude}<br>
                    Longitude: ${longitude}
                `
            },

            function(){

                alert("Location permission denied")
            }
        )

    }else{

        alert("Geolocation not supported")
    }
}

getLocation()

async function sendSOS(){

    const response = await fetch('/sos', {

        method: 'POST',

        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({

            tourist_id: "T001",

            latitude: latitude,

            longitude: longitude,

            emergency_type: "Emergency"
        })
    })

    const data = await response.json()

    alert(data.message)
}