# Hack_ai_temperature_monitor
This repository hosts a Temperature Monitoring Agent designed to monitor temperature levels in a specified location. If the temperature deviates from the user's desired range, the agent will send a text message notification. This project was created specifically for the Hack.ai Hackathon organized by Techfest IIT Bombay and Fetch.ai.
# Steps to be followed
## 1) API keys
 You need two API keys before running the agent: <br />
 **1. OpenWeatherMap API:** Get an API key from OpenWeatherMap by signing up at [OpenWeatherMap API](https://openweathermap.org/api). <br />
 **2. Sinch SMS API Key:** Sign up for an account on [Sinch](https://www.sinch.com/). After logging in, navigate to the "API" section to create an API token. Ensure you have a Sinch number to send SMS notifications from. <br />
## 2) Download required libraries
Download the uagents and requests library
```shell
pip install uagents
pip install requests
```
## 3) Run the agent
Before running the code put your weather api key, sinch api token, sinch number, sinch service plan id and the receiver's number. Then run the main.py file.
```shell 
python main.py
```
# Example
Here's an example of how to use the Temperature Monitoring Agent:

- **Run the agent using the provided instructions.**
- **Enter the city name you want to monitor (e.g., "Mumbai"). *First letter of city name should be capital.***
- **Enter your desired minimum temperature (e.g., 20°C).**
- **Enter your desired maximum temperature (e.g., 30°C).**
- **The agent will periodically(each 20 seconds. You can change the code for different interval) check the temperature in the selected city.**
- **If the temperature falls below or rises above your desired range, you will receive a text message notification.** <br />
<hr />
Now you can chill until you get sms regarding unfavourable temperatres.







