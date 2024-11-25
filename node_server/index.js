const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const fs = require('fs');


const app = express();

app.use(cors())
app.use(bodyParser.json())

app.get('/send_status', (req, res) => {
    console.log("Primesc Click");
    res.status(200).send({ msg: "Dau click" })
})

app.post('/send_data', (req, res) => {
    let data = req.body;
    console.log(data);

    fs.writeFileSync(`data-${new Date().toISOString()}.json`, JSON.stringify(data), err => {
        if (err) {
            console.log(err);
            res.status(500).send({ msg: "failed to save file!" })
        }
    });
})

app.get('/get_data', (req, res) => {
    let data = fs.readFileSync(`../parser/parsed_data_2024-11-18 18:46:50.384333.json`);
    console.log(data);
    res.status(200).send(data);
})

app.listen(3000, () => {
    console.log('server running on port 3000');
})

