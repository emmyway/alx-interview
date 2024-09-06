#!/usr/bin/node

// Import the request module
const request = require('request');

// Access the Movie ID from command-line arguments
const movieId = process.argv[2];

// Verify that a Movie ID has been provided
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Define the URL to fetch movie details using the Movie ID
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Make a request to the Star Wars API for the movie details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie:', error);
    return;
  }

  // Parse the API response body as JSON
  const movieData = JSON.parse(body);

  // Extract the list of character URLs from the movie data
  const characters = movieData.characters;

  // For each character URL, make another request to fetch character details
  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error fetching character:', error);
        return;
      }

      // Parse the character data and print the name
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
