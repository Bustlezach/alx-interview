#!/usr/bin/node

function ordered (characters, idx) {
  if (idx >= characters.length) {
    return;
  }
  request(characters[idx], function (err, response, body) {
    if (err) {
      console.log(err);
    } else if (response.statusCode === 200) {
      const person = JSON.parse(body);
      console.log(person.name);
      return ordered(characters, ++idx);
    } else {
      console.log(`error ocurred, Status code: ${response.statusCode}`);
    }
  });
}

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const value = process.argv[2];
request(url + value, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const jans = JSON.parse(body);
    ordered(jans.characters, 0);
  } else {
    console.log(`error ocurred, Status code: ${response.statusCode}`);
  }
});