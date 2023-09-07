#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const movieUrl = `${url}${process.argv[2]}`;

function getFilms (err, _, body) {
  if (!err) {
    const films = JSON.parse(body);
    const characters = films.characters;
    if (characters && characters.length > 0) {
      processCharacters(characters, 0, characters.length);
    }
  } else {
    console.error(err);
  }
}

function processCharacters (characters, index, size) {
  if (index === size) {
    return;
  }
  const url = characters[index];
  request(url, (err, _, body) => {
    if (!err) {
      const respBody = JSON.parse(body);
      console.log(respBody.name);
      index++;
      processCharacters(characters, index, size);
    } else {
      console.error(err);
    }
  });
}

request(movieUrl, getFilms);
