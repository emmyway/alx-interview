#!/usr/bin/node

const request = require('request');
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

// Fetch movie data from the Star Wars API
request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;

    // Array to hold the character names in the correct order
    const promises = characters.map(url => {
      return new Promise((resolve, reject) => {
        request(url, (err, res, bod) => {
          if (!err && res.statusCode === 200) {
            resolve(JSON.parse(bod).name);
          } else {
            reject(err);
          }
        });
      });
    });

    // Resolve all promises and log the characters in order
    Promise.all(promises)
      .then(names => {
        names.forEach(name => console.log(name));
      })
      .catch(error => console.log(error));
  } else {
    console.log(error);
  }
});
