# HNG12 - Stage 0 Task

## Description
This project is a simple API designed to return user-specific details such as email, current UTC datetime, and GitHub URL in a JSON format. Here we see how to handle GET requests in a Django API with a dynamic response.

## Setup Instructions
To run this project locally, follow the steps below:

### Prerequisites
1. Python 3.8 or later
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

## API Documentation
### Endpoint URL
GET /
This endpoint is mapped to the root URL (/) and is associated with the my_info view function.


### Request Format
This endpoint accepts a GET request. No request body is required.

### Response Format (200 OK)
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
- email: The user's email address.
- current_datetime: Dynamically generated UTC datetime in ISO 8601 format.
- github_url: The user's GitHub URL.

### Example Usage
To use the API, simply send a GET request to the following URL:
http://localhost:8000/

The response will return the JSON format as shown above with the dynamically generated current UTC datetime.

## Backlink
https://hng.tech/hire/python-developers