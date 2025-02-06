# Number Classification API 

## Overview
This API classifies numbers based on their mathematical properties and fetches a fun fact from the Numbers API.

## Features
- Checks if a number is prime, perfect, or an Armstrong number.
- Determines if a number is odd or even.
- Returns the sum of its digits.
- Fetches a fun fact.

## API Endpoint
**GET** `/api/classify-number?number={integer}`

### Example Request

### Example Response
```
{
  "number": 2,
  "is_prime": true,
  "is_perfect": false,
  "properties": [
    "armstrong",
    "even"
  ],
  "digit_sum": 2,
  "fun_fact": "2 is the smallest and the first prime number, and the only even one (for this reason it is sometimes called \"the oddest prime\")."
}
```