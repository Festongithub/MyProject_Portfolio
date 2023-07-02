const http = require('http')
const fs = require('fs')
const { error } = require('console')
const port = 5500

const server = http.createServer(function(req, res){
    res.writeHead(200, {'Content-Type': 'text/html'})
    fs.readFile('index.html', function(error, data){
    if(error){
        res.writeHead(404)
        res.write('Error: File Not found')
    } else{
        res.write(data)
    }
    res.write("data")
})
    res.end()
})

server.listen(port, function(error){
    if(error){
        console.log("Something is not right!", error)
    }
    else{
        console.log("server is listening to port", port)
    }
})