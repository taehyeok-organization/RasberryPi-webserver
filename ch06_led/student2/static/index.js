const led = document.getElementById("led");
const on = document.getElementById("on");
const off = document.getElementById("off");

// ON 버튼
on.addEventListener("click", function () {
    fetch("/on", { method: "POST" })
        .then(response => {
            if (!response.ok) {
                throw new Error("HTTP error " + response.status);
            }
            led.src = "/static/on.png";
        })
        .catch(error => {
            alert(error.message);
        });
});

// OFF 버튼
off.addEventListener("click", function () {
    fetch("/off", { method: "POST" })
        .then(response => {
            if (!response.ok) {
                throw new Error("HTTP error " + response.status);
            }
            led.src = "/static/off.png";
        })
        .catch(error => {
            alert(error.message);
        });
});
