
var exec = require('execSync');
var fs = require('fs');
const util = require('util');

var db = require('./sqlite_db.js');
var command = JSON.parse(fs.readFileSync('./commands.json', 'utf8'));

var password = "amitg.b91";
var ca_conf = "/home/aghadge/ssl/ca/sub-ca/sub-ca.conf"
exports.read = function(id, callback) {

        db.read(id, function(err, row) {
          var result;
          var sql_result = row;
          if(sql_result == "404") {
            result =  {"status" : 404, "output" : "Not found!"};
            callback(err, result);
            return;
          }

          var cert_file = 'cert_'+id+'.crt'
          var data = fs.writeFileSync(cert_file, sql_result, 'utf8');
          console.log('Reading certificate...');
          var cmd = command["read"]+cert_file;
          var output = exec.exec(cmd);

          if(output.code == 0) {
            result = {"status": output.code, "output": output.stdout};
          }
          else {
            result = {"status": output.code, "output": output.stderr};
          }
          exec.exec("rm "+cert_file);
          callback(err, result);
        });

}


exports.create = function(csr_text, id, duration, callback) {
    var v = command["create"];
    var csr_file = "csr_file";
    fs.writeFileSync(csr_file+".csr", csr_text, 'utf8');

    var cmd = util.format(command["create"], ca_conf, duration, csr_file, csr_file, password);
    console.log(cmd);
    var output = exec.exec(cmd);

    var result = {"status": output.code, "output": output.stdout};

    console.log(result);
}
