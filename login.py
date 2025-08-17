#!/usr/bin/env python3
import requests
import re
import os

def perform_login():
    url = 'https://client.webhostmost.com/login'
    login_action = 'https://client.webhostmost.com/dologin.php'
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')

    if not username or not password:
        print("Error: USERNAME or PASSWORD environment variables are not set.")
        return

    session = requests.Session()
    
    # Get the login page to extract the CSRF token
    response = session.get(url)
    if response.status_code != 200:
        print(f"Failed to access login page. Status code: {response.status_code}")
        return

    # Extract the token using regex
    token_match = re.search(r'name="token" value="([a-f0-9]+)"', response.text)
    if not token_match:
        print("Failed to find CSRF token in the login page.")
        return

    token = token_match.group(1)

    # Prepare login data
    data = {
        'username': username,
        'password': password,
        'token': token,
    }

    # Post the login request
    login_response = session.post(login_action, data=data, allow_redirects=True)
    
    # Check if login was successful
    if 'clientarea.php' in login_response.url:
        print("Login successful!")
    elif 'incorrect=true' in login_response.url:
        print("Login failed: Incorrect username or password.")
    else:
        print(f"Unexpected response after login. URL: {login_response.url}")

if __name__ == "__main__":
    perform_login()
