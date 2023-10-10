# Import necessary modules
from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low
import requests

# Define a data model for the message
class Message(Model):
    message: str

# Create a temperature monitoring agent
temperature_agent = Agent(
    name="temperature_agent",
    port=8000,
    seed="temperature_secret_phrase",
    endpoint=["http://127.0.0.1:8000/submit"],
)

# Fund the agent if it has low funds
fund_agent_if_low(temperature_agent.wallet.address())

# Get the city for temperature surveillance from the user
selected_location = input("Enter the city you want to put in surveillance: ")

# Define the user's desired temperature range
desired_min_temp = int(input("Enter your desired minimum temperature: "))
desired_max_temp = int(input("Enter your desired maximum temperature: "))

# Create the URL for the weather API
url = f'https://api.openweathermap.org/data/2.5/weather?q={selected_location}&appid="INSERT_YOUR_API_KEY_HERE"'

# Initialize temperature_celsius to a default value
temperature_celsius = 0

try:
    # Send a GET request to the weather API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract and calculate the temperature in Celsius
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15  # Convert to Celsius

    else:
        print(f"Request failed with status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")

# Store the current temperature in Celsius
current_temperature = temperature_celsius

# Define a function to monitor the temperature
def monitor_temperature():
    if current_temperature < desired_min_temp:
        return (f"Temperature in {selected_location} is below the desired minimum ({desired_min_temp}°C) and it is {current_temperature}.")
    elif current_temperature > desired_max_temp:
        return (f"Temperature in {selected_location} is above the desired maximum ({desired_max_temp}°C) and it is {current_temperature}.")
    else:
        return (f"Temperature in {selected_location} is within the desired range ({desired_min_temp}-{desired_max_temp}°C) and it is {current_temperature}.")

# Define an asynchronous function to notify the user via SMS
async def notify_user(message):
    servicePlanId = "INSERT_YOUR_SERVICE_PLAN_ID_HERE"
    apiToken = "INSERT_YOUR_API_TOKEN_HERE"
    sinchNumber = "INSERT_YOUR_SINCH_NUMBER_HERE_WITH_COUNTRY_CODE"
    toNumber = "INSERT_RECEIVERS_NUMBER_HERE_WITH_COUNTRY_CODE"
    url = "https://us.sms.api.sinch.com/xms/v1/" + servicePlanId + "/batches"

    payload = {
        "from": sinchNumber,
        "to": [
            toNumber
        ],
        "body": message
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + apiToken
    }
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

# Schedule the temperature monitoring at regular intervals
@temperature_agent.on_interval(period=20.0)  # Check every 20 seconds (adjust as needed)
async def temperature_monitor(ctx: Context):
    temperature_status = monitor_temperature()
    ctx.logger.info(temperature_status)
    if "below" in temperature_status or "above" in temperature_status:
        await notify_user(temperature_status)

# Run the temperature monitoring agent
if __name__ == "__main__":
    temperature_agent.run()
