const http = require('http');

const server = http.createServer(function(req, res){
    res.setHeader('Content-type', 'index.html');
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.writeHead(200) 

    let dataobj = {'id':123, "name":"Bob"}
    let data = JSON.stringify(dataobj)
    res.end(data)
});


server.listen(5000, function(){
    console.log("Listening on port 5000")

});
