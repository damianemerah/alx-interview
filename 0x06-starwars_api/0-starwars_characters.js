#!/usr/bin/node
const request = require('request');

function getFilms () {
  const url = 'https://swapi-api.alx-tools.com/api/films';
  if (process.argv.length > 2) {
    request(`${url}/${process.argv[2]}`, (err, _, body) => {
      if (err) console.log(err);
      const { characters } = JSON.parse(body);
      const characterNames = characters.map(url =>
        new Promise((resolve, reject) => {
          request(url, (promiseErr, _, characterReqBody) => {
            if (promiseErr) reject(promiseErr);
            resolve(JSON.parse(characterReqBody).name);
          });
        })
      );
      Promise.all(characterNames)
        .then((name) => console.log(name.join('\n')))
        .catch(err => console.log(err));
    });
  }
}

getFilms();
