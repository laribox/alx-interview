#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const characters = JSON.parse(body).characters;
  
  characters.forEach(characterUrl => {
    request(characterUrl, (err, res, charBody) => {
      if (err) {
        console.error(err);
        return;
      }
      const characterName = JSON.parse(charBody).name;
      console.log(characterName);
    });
  });
});

