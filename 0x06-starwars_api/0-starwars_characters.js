#!/usr/bin/node
const { argv, exit } = require('process');
const request = require('request');

class HTTPError extends Error {
  constructor (statusCode, message) {
    super(message);
    this.statusCode = statusCode;
  }
}

const getRequest = async (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        if (response.statusCode >= 400) {
          const message = JSON.parse(body).detail;

          reject(new HTTPError(response.statusCode, message));
        }

        resolve(JSON.parse(body));
      }
    });
  });
};

const main = async () => {
  if (argv.length !== 3) {
    console.log(`Usage: ${argv[1]} movieId`);
    exit(1);
  }

  const movieId = argv[2];
  const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  try {
    const movie = await getRequest(movieUrl);
    const charactersUrls = movie.characters;

    const characters = await Promise.all(
      charactersUrls.map((charactersUrl) => getRequest(charactersUrl))
    );

    for (const character of characters) {
      console.log(character.name);
    }
  } catch (error) {
    if (error instanceof HTTPError) {
      console.log(error.statusCode, error.message);
    } else {
      console.error(error);
      exit(1);
    }
  }
};

main();
