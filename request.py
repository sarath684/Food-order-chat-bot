import requests

# Replace with your actual ngrok URL
ngrok_url = "https://6581-219-91-176-123.ngrok-free.app"

# Define the headers, including the ngrok-skip-browser-warning header
headers = {
    "ngrok-skip-browser-warning": "any_value",
    "Content-Type": "application/json"
}

# Define the payload mimicking the Dialogflow webhook request structure
payload = {
    "queryResult": {
        "intent": {
            "displayName": "track.order"
        },
        "parameters": {},
        "outputContexts": []
    }
}

try:
    # Send the POST request to the ngrok URL
    response = requests.post(ngrok_url, json=payload, headers=headers)

    # Print the status code and raw response text for debugging
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        try:
            # Attempt to parse the JSON response
            response_json = response.json()
            print(response_json)
        except ValueError as e:
            # Handle JSON decoding errors
            print(f"JSON decode failed: {e}")
    else:
        # Handle unexpected status codes
        print(f"Unexpected status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    # Handle request-related exceptions (e.g., network issues, timeout)
    print(f"Request failed: {e}")

except Exception as e:
    # Handle any other unexpected exceptions
    print(f"Unexpected error occurred: {e}")
