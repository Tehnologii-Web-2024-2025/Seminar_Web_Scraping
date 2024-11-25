let button = document.querySelector('#send_request')
button.addEventListener('click', function () {
    console.log("Click")
    fetch('http://localhost:3000/send_status')
        .then(response => response.json())
        .then(data => console.log(data))


})

let start_scraper = document.querySelector("#start_scraping")
start_scraper.addEventListener('click', function () {
    fetch('http://127.0.0.1:5000/start_scraping')
        .then(response => response.json())
        .then(data => {
            console.log(data)
        })


})

let get_data = document.querySelector('#get_data')
get_data.addEventListener('click', function () {
    fetch('http://localhost:3000/get_data')
        .then(response => response.json())
        .then(data => {
            const titles = data.titles;

            titles.map(title => {
                let table_body = document.querySelector('tbody')
                let cell = document.createElement('tr')
                cell.innerHTML = title

                table_body.appendChild(cell)
            })
        })
})



