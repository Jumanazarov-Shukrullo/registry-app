import json
import os
import sys
from datetime import datetime
import django

project = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(project)
os.environ['DJANGO_SETTINGS_MODULE'] = 'registry_licences_api.settings'


django.setup()
from data_table.models import Table


def load_data_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data


def insert_data_to_database(data):
    for item in data:
        table_instance = Table(
            fullname=item['fullname'],
            abbreviated_name=item['abbreviated_name'],
            licence_number=item['licence_number'],
            inn=item['inn'],
            date_of_registration=datetime.strptime(item['date_of_registration'], '%Y-%m-%d') if item[
                'date_of_registration'] else None,
            address=item['address'],
            deadline=datetime.strptime(item['deadline'], '%Y-%m-%d') if item['deadline'] else None,
            status=item['status'],
            termination_date=datetime.strptime(item['termination_date'], '%Y-%m-%d') if item[
                'termination_date'] else None
        )
        table_instance.save()


def main():
    json_file = 'data.json'
    data = load_data_from_json(json_file)
    insert_data_to_database(data)


if __name__ == "__main__":
    main()
