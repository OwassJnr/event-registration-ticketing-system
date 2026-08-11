const API_BASE_URL =
"https://knpn96h9b4.execute-api.eu-west-1.amazonaws.com/prod";

let eventsCache = [];

document.addEventListener("DOMContentLoaded", () => {
    loadEvents();

    document
        .getElementById("registerBtn")
        .addEventListener("click", registerUser);
});

async function loadEvents() {

    const eventsList =
        document.getElementById("eventsList");

    try {

        const response =
            await fetch(`${API_BASE_URL}/events`);

        const events =
            await response.json();

        eventsCache = events;

        eventsList.innerHTML = "";

        events.forEach(event => {

            const available =
                Number(event.registeredCount) <
                Number(event.capacity);

            eventsList.innerHTML += `
                <div class="event-row">

                    <div class="event-name">
                        ${event.name}
                    </div>

                    <div class="event-date">
                        ${formatDate(event.date)}
                    </div>

                    <div class="badge ${
                        available
                            ? "available"
                            : "limited"
                    }">
                        ${
                            available
                                ? "Available"
                                : "Limited"
                        }
                    </div>

                </div>
            `;
        });

    } catch(error){

        showMessage(
            "Unable to load events.",
            "error"
        );

        console.error(error);
    }
}

async function registerUser(){

    const email =
        document.getElementById("email")
        .value
        .trim();

    const eventName =
        document.getElementById("eventName")
        .value
        .trim();

    if(!email || !eventName){

        showMessage(
            "Please enter Event Name and Email Address.",
            "error"
        );

        return;
    }

    const selectedEvent =
        eventsCache.find(
            e =>
                e.name.toLowerCase() ===
                eventName.toLowerCase()
        );

    if(!selectedEvent){

        showMessage(
            "Event not found.",
            "error"
        );

        return;
    }

    try{

        document.getElementById(
            "registerBtn"
        ).innerText = "Registering...";

        const response =
            await fetch(
                `${API_BASE_URL}/register`,
                {
                    method:"POST",
                    headers:{
                        "Content-Type":"application/json"
                    },
                    body:JSON.stringify({
                        eventId:selectedEvent.eventId,
                        name:"Participant",
                        email:email
                    })
                }
            );

        const result =
            await response.json();

        showMessage(
            result.message ||
            "Registration successful.",
            "success"
        );

        document
            .getElementById("email")
            .value = "";

    } catch(error){

        showMessage(
            "Registration failed.",
            "error"
        );

        console.error(error);

    } finally{

        document.getElementById(
            "registerBtn"
        ).innerText = "Register →";
    }
}

function showMessage(message,type){

    const div =
        document.getElementById("message");

    div.className = type;

    div.innerHTML = message;

    setTimeout(() => {
        div.innerHTML = "";
        div.className = "";
    },5000);
}

function formatDate(dateString){

    const date =
        new Date(dateString);

    return date.toLocaleDateString(
        "en-GB",
        {
            day:"numeric",
            month:"short",
            year:"numeric"
        }
    );
}