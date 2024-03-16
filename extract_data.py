import csv
import requests
import json

with open('config.json') as config_file:
    config = json.load(config_file)

url = config['url']

querystring = config['querystring']

headers=config['headers']

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    data = response.json()['data']['flights']['days']
    
    # Define CSV filename
    csv_filename = 'flight_data.csv'
    
    # Specify required field names for CSV
    field_names = ['day', 'group', 'price']
    
    # Write data to CSV file with specified field names
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        for entry in data:
            writer.writerow({'day': entry['day'], 'group': entry['group'], 'price': entry['price']})
    
    print(f"Data fetched successfully and written to '{csv_filename}'")
else:
    print("Failed to retrieve data. Status code:", response.status_code)
