#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}/`;
request(url, async function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      try {
        const res = await new Promise((resolve, reject) => {
          request(character, (error, response, body) => {
            if (error) {
              reject(error);
            } else {
              resolve(JSON.parse(body).name);
            }
          });
        });
        console.log(res);
      } catch (err) {
        console.error('error:', err);
      }
    }
  }
});
