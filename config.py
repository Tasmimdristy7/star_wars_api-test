import os

# Set default values for your environment variables
os.environ.setdefault('SWAPI_BASE_URL', 'https://swapi.dev/api')

# Then define variables to export the settings
BASE_URL = os.getenv('SWAPI_BASE_URL')
