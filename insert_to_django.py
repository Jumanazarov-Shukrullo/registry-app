import json
import os
import sys
from datetime import datetime
import django

# Find the project directory and add it to sys.path
project = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(project)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'registry_licences_api.settings'

# Setup Django
django.setup()

# Import the Table model from data_table.models
from data_table.models import Table


# Function to load data from a JSON file
def load_data_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data


# Function to insert data into the database
def insert_data_to_database(data):
    for item in data:
        # Create a new Table instance with data from the JSON
        table_instance = Table(
            fullname=item['fullname'],
            abbreviated_name=item['abbreviated_name'],
            licence_number=item['licence_number'],
            inn=item['inn'],
            date_of_registration=datetime.strptime(item['date_of_registration'], '%Y-%m-%d') if item['date_of_registration'] else None,
            address=item['address'],
            deadline=datetime.strptime(item['deadline'], '%Y-%m-%d') if item['deadline'] else None,
            status=item['status'],
            termination_date=datetime.strptime(item['termination_date'], '%Y-%m-%d') if item['termination_date'] else None
        )
        # Save the Table instance to the database
        table_instance.save()


def main():
    # JSON file containing the data
    json_file = 'data.json'
    # Load data from the JSON file
    data = load_data_from_json(json_file)
    # Insert data into the database
    insert_data_to_database(data)


if __name__ == "__main__":
    main()
