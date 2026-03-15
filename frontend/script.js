let radarChart;

function simulate() {

    const data = {
        sleep: parseInt(document.getElementById("sleep").value),
        study: parseInt(document.getElementById("study").value),
        screen: parseInt(document.getElementById("screen").value),
        exercise: parseInt(document.getElementById("exercise").value),
        stress: parseInt(document.getElementById("stress").value)
    };

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {

        const ctx = document.getElementById("radarChart").getContext("2d");

        if (radarChart) radarChart.destroy();

        radarChart = new Chart(ctx, {
            type: "radar",
            data: {
                labels: ["Focus", "Energy", "Productivity", "Burnout"],
                datasets: [{
                    label: "Future Metrics",
                    data: [
                        result.focus,
                        result.energy,
                        result.productivity,
                        result.burnout
                    ],
                    backgroundColor: "rgba(0,198,255,0.4)",
                    borderColor: "#00c6ff"
                }]
            }
        });

        document.getElementById("advice").innerText = result.advice;
    });
}

function sendMessage() {

    const input = document.getElementById("chatInput");
    const message = input.value;

    fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {

        const chat = document.getElementById("chatMessages");

        chat.innerHTML += "<div>You: " + message + "</div>";
        chat.innerHTML += "<div>AI: " + data.reply + "</div>";

        input.value = "";
        chat.scrollTop = chat.scrollHeight;
    });
}