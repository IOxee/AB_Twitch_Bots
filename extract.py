import requests
import json
import os
import time

# Read the configuration file
with open("config/config.json") as config_file:
    config = json.load(config_file)

# Make the GET request to the TwitchInsights API
response = requests.get('https://api.twitchinsights.net/v1/bots/all')
response_json = json.loads(response.text)

# Calculate recent activity based on configuration
current_time = time.time()
hasRecentlyActivity = current_time - config["hasRecentlyActivity"]

# Filter bots based on recent activity
bots = response_json['bots']
bot_names = [bot[0] for bot in bots if bot[2] > hasRecentlyActivity]

# Sort bot names alphabetically
bot_names.sort()

# Write the bot names to a temporary file
with open('content/temp_file', 'w') as f:
    for name in bot_names:
        f.write(name + '\n')

# Read the contents of the whitelist file and store it in a set
with open(config["whitelist"], 'r') as f:
    whitelist = set(f.read().splitlines())

# Read the contents of the temporary file and store them in another set
with open('content/temp_file', 'r') as f:
    bot_names = set(f.read().splitlines())

# Find bots that are in bot_names but not in the whitelist
unknown_bots = bot_names - whitelist

# Write the results to an output file
with open('content/output_file', 'w') as f:
    f.write('\n'.join(sorted(unknown_bots)))

# Remove the temporary file
os.remove('content/temp_file')
