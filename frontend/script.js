button = document.querySelector('#send_request')
button.addEventListener('click', function () {
    console.log("Click")
    fetch('http://localhost:3000/send_status')
        .then(response => response.json())
        .then(data => console.log(data))
})