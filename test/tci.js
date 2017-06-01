var Nightmare = require('nightmare');		
var nightmare = Nightmare({ show: true });

nightmare
  .goto('http://127.0.0.1:5000/faae3f87400f9fb5172743543133a1b6')
  .end()
  .then(function (result) {
    console.log(result);
  })
  .catch(function (error) {
    console.error('Search failed:', error);
  });
