# HNG12 

## Stage 1 Task

### Description
This API classifies numbers based on their mathematical properties and fetches a fun fact from the Numbers API.

### Features
- Checks if a number is prime, perfect, or an Armstrong number.
- Determines if a number is odd or even.
- Returns the sum of its digits.
- Fetches a fun fact.

### API Endpoint
**GET** `/api//number-properties/?number={integer}`

#### Example Request

#### Example Response
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
## Stage 0 Task

### Description
This project is a simple API designed to return specific details such as my email, current UTC datetime, and my GitHub URL in a JSON format. Here we see how to handle GET requests in a Django API with a dynamic response.

### Setup Instructions
To run this project locally, follow the steps below:

1. Make sure you have Python 3.8 or later
2. Clone the Repository  
``` git clone https://github.com/Miife/HNG12.git ```  
``` cd HNG12 ```

3. Set Up Virtual Environment (optional but recommended)  
``` python -m venv NameOfVirtualenv ```  
On Windows, ``` NameOfVirtualenv\Scripts\activate ```

4. Install Dependencies  
``` pip install -r requirements.txt ```

5. Run the Development Server  
``` python manage.py runserver ```  
By default, the API will be accessible at http://localhost:8000/

### API Documentation
#### Endpoint URL
GET /  
This endpoint is mapped to the root URL (/) and is associated with the my_info view function.


#### Request Format
This endpoint accepts a GET request. No request body is required.

#### Response Format (200 OK)
```
{
  "email": "my-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/myusername/my-repo"
}
```
- email: My email address.
- current_datetime: Dynamically generated UTC datetime in ISO 8601 format.
- github_url: My GitHub URL.

#### Example Usage
To use the API, simply send a GET request to the following URL:  
http://localhost:8000/

The response will return the JSON format as shown above with the dynamically generated current UTC datetime.

### Backlink
https://hng.tech/hire/python-developers
