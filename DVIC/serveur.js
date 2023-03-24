const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const http = require('http');
const cors = require('cors');
const port = 3000;
const ip = require("ip")
let note = 0;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cors());

app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
    next();
});

console.log(ip.address())

app.post('/play', (req, res) => {
    console.log("reponse : ",req.body);
    note = req.body
    res.send({ "status": "ok" });   
})

app.get('/play', (req, res) => {
    console.log("reponse : ",req.body);
    let tempnote = note
    note = 0
    res.send({"msg":tempnote});   
    
});


app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`));
