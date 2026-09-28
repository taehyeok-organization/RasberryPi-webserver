let n = 0;

const num = document.getElementById("num");
const numInput = document.getElementById("numInput");
const increase = document.getElementById("increase");

increase.addEventListener("click", function () {
    n = n + 1;

    num.innerHTML = n;
    numInput.value = n;
});
