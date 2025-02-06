import requests

def is_prime(n):
    """A function to check if a number is prime."""
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%1==0:
            return False
    return True

def is_armstrong(n):
    """A function to check if a number is an Armstrong number."""
    fig = [int(i) for i in str(n)]
    return sum(i** len(fig) for i in fig) == n

def is_perfect(n):
    """A function to check if a number is perfect."""
    return n>1 and sum(i for i in range(1,n) if n%i==0)==n

def digit_sum(n):
    """A function to return the sum of digits."""
    return sum(int(i) for i in str(n))

def fun_fact(n):
    """A function to fetch a fun fact from Numbers API."""
    url = f"http://numbersapi.com/{n}/math?json"
    try:
        response = requests.get(url, timeout=2)
        if response.status_code == 200:
            return response.json().get("text", "No fact found.")
    except requests.RequestException:
        return "Could not fetch a fun fact."
    return "No fact available."

def number_properties(n):
    """A funtion to return its properties"""
    properties = []
    if is_armstrong(n):
        properties.append("armstrong")
    properties.append("odd" if n%2 else "even")
    return {
        "number": n,
        "is_prime": is_prime(n),
        "is_perfect": is_perfect(n),
        "properties": properties,
        "digit_sum": digit_sum(n),
        "fun_fact": fun_fact(n),
        }




