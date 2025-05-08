const fs = require('fs');

async function input_creds() {
  const data = fs.readFileSync('creds.json', 'utf-8');
  const jsonData = JSON.parse(data);

  const response = await fetch("http://127.0.0.1:8000/access_db", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      user: jsonData.user,
      password: jsonData.password,
      database: jsonData.database
    })
  });

  const result = await response.json();
  console.log("Response:", result);
  return result;
}

async function get_movies_rating(is_adult_input, rating_input, limit_input) {
  const response = await fetch("http://127.0.0.1:8000/get_movies_rating", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      is_adult: is_adult_input,
      rating: rating_input,
      limit: limit_input
    })
  });

  const result = await response.json();
  return result;
}

async function main() {
  const credsResponse = await input_creds();
  if (credsResponse.Status === 'Connected') {
    const movies = await get_movies_rating(0, 8.0, 10);
    console.log("Movies:", movies);
  } else {
    console.log("Database connection failed.");
  }
}

main();