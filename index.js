const http = require('http');
const port = process.env.PORT || 3333;
const server = http.createServer((req, res) => {
  res.end('Assistant Copropriété 10M prêt sur le port ' + port);
});
server.listen(port, () => {
  console.log('Serveur IA actif sur le port ' + port);
});
