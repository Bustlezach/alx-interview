#!/usr/bin/node
/* 
  This script prints all characters of a Star Wars movie.
  API_URL: https://swapi-api.alx-tools.com/api/
*/

if (process.argv.length < 3) {
  process.exit(1);
} 


const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`; 

const request = require('request');
const characters = [];

request.get(url, function(error, response, body){
  if(error) {
    return error;
  }
  if(response.statusCode === 200) {
    // console.log("SUCCESS");
  }
  const data = JSON.parse(body);
  if(data.hasOwnProperty("characters")) {
    const result = data.characters;
    result.forEach((line) => {
      characters.push(line);
    })
    characters.map((URL) => {
      request.get(URL, function(err, res, body) {
        const person = JSON.parse(body);
        console.log(person.name);
      })
    })
  } else {
    return "characters not found";
  }
});




  // .then((response) => {
  //   if (response.status === 200) {
  //     return response.json();
  //   } else {
  //     throw new Error("Something went wrong on API server.");
  //   }
  // })
  // .then((data) => console.log(data))
  // .catch((error) => console.error(error))
  // .finally();
