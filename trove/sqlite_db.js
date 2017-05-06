
var sqlite3_db = "/home/aghadge/my/sec/wrapdigi/jupiter/db.sqlite3";
var sqlite3 = require('sqlite3').verbose();

exports.read = function(id, callback) {
  var db = new sqlite3.Database(sqlite3_db);
  console.log("Fetching db........");
  db.get("SELECT certificate_text from certificate_useractivatecertificate where id=?", id, function(err, row) {
    if(row != undefined) {
      callback(err, row.certificate_text);
    }
    else {
      callback(err, "404");
    }
    });
  db.close();
  return;
};
