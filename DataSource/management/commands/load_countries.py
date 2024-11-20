import json
from DataSource.models import Country
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Load countries from a JSON file and save to the database'


    """
        For Insurt Data Run >> python manage.py load_countries
    """
    

    def handle(self, *args, **kwargs):
        # File path to the JSON data
        file_path = 'JsonData/countries.json'

        try:
            # Open and load JSON data
            with open(file_path, 'r') as file:
                countries_data = json.load(file)

            # Iterate over the country data and save to the database
            for country_data in countries_data:
                country_name = country_data['name']
                short_name = country_data.get('code', None)

                # Create the Country instance and save it
                country = Country(name=country_name, short_name=short_name)
                country.save()

            self.stdout.write(self.style.SUCCESS('Successfully imported countries into the database'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Error decoding JSON'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))
