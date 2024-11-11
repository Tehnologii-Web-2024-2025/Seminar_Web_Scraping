const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();

app.use(cors())
app.use(bodyParser.json())

app.get('/send_status', (req, res) => {
    console.log("Primesc Click");
    res.status(200).send({ msg: "Dau click" })
})

app.listen(3000, () => {``
    console.log('server running on port 3000');
})

