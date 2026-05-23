function showAlert(){

    alert("🚨 Emergency SOS Alert Sent Successfully!");

    let now = new Date();

    let time = now.toLocaleTimeString();

    liveSOSAlert =
    "🚨 <b>HIGH ALERT</b><br>" +
    "Emergency SOS Triggered<br>" +
    "<small>Time: " + time + "</small>";

    updateAlerts();
}
function updateDashboard(){

    let tourists = 120;
    let alerts = 3;
    let status = 92;

    document.getElementById("tourists").innerHTML = tourists;
    document.getElementById("alerts").innerHTML = alerts;
    document.getElementById("status").innerHTML = status + "%";
}
updateDashboard();

let liveSOSAlert = "";
function updateAlerts(){

    const alertsList = [
        liveSOSAlert,
        "🚨 SOS Alert: Tourist needs help in Zone A",
        "⚠️ Medical emergency reported near waterfall",
        "🚨 Lost tourist detected in forest area",
        "⚠️ Suspicious movement in restricted zone",
        "🚨 All tourists safe in Zone C"
    ];

    let container = document.getElementById("alertContainer");

    container.innerHTML = "";

    alertsList.forEach(alert => {

    if(alert === "") return;
        let div = document.createElement("div");
        div.className = "alert-box";
        div.innerHTML = alert;
        container.appendChild(div);
    });
}
updateAlerts();


updateDashboard();
function registerTourist(){

    let name = document.getElementById("name").value;

    let email = document.getElementById("email").value;

    let location = document.getElementById("location").value;

    if(name == "" || email == "" || location == ""){

        alert("⚠ Please fill all details!");

    }

    else{

    alert("✅ Tourist Registered Successfully!");

    document.getElementById("name").value = "";

    document.getElementById("email").value = "";

    document.getElementById("location").value = "";

}

}
function showDateTime(){

    let now = new Date();

    document.getElementById("datetime").innerHTML =
    now.toLocaleString();

}

showDateTime();
setInterval(showDateTime, 1000);
updateDashboard();


updateAlerts();


/* CHART CODE */

const ctx = document.getElementById('alertChart');

if(ctx){

    new Chart(ctx, {

        type: 'bar',

        data: {

            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],

            datasets: [{

                label: 'Emergency Alerts',

                data: [5, 8, 3, 10, 6],

                borderWidth: 1

            }]
        },

        options: {

            responsive: true,

            scales: {

                y: {

                    beginAtZero: true

                }
            }
        }
    });
}
function toggleDarkMode(){

    document.body.classList.toggle("dark-mode");
}
function updateWeather(){

    const temps = ["28°C", "30°C", "26°C", "29°C"];

    let randomTemp =
    temps[Math.floor(Math.random() * temps.length)];

    let weather =
    document.getElementById("weatherTemp");

    if(weather){

        weather.innerHTML = randomTemp;
    }
}

updateWeather();

