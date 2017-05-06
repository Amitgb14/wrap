
var command = require('./command');

var express = require('express');
var bodyParser = require('body-parser');

var app = express();
var router = express.Router();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

router.get('/', function(request, response){
  response.end('Hello there from express.');
});


router.get('/get/:id', function(request, response){
  command.read(request.params.id, function(err, result) {
    response.send(result);
  });
});


router.post('/create', function(request, response){
  var result = command.create(request.body.csr_text, request.body.id, request.body.duration);
  response.end(result);
});

app.use('/api', router);

app.listen(1337, function(){
  console.log('Listening 1337.');
});
