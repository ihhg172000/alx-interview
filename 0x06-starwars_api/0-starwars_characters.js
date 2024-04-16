#!/usr/bin/node
const request = require('request');

const getRequest = async (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, request, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

const main = async () => {
  const movieId = process.argv[2];
  const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  const movie = await getRequest(movieUrl);
  const charactersUrls = movie.characters;

  const characters = await Promise.all(
    charactersUrls.map((charactersUrl) => getRequest(charactersUrl))
  );

  for (const character of characters) {
    console.log(character.name);
  }
};

main();
