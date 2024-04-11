import pytest
import requests
from os import getenv

class TestPlanets:
    @pytest.fixture(scope="class")
    def session(self, request):
        """Create a session to be used in all tests within this class."""
        request.cls.session = requests.Session()
        request.cls.base_url = getenv('SWAPI_BASE_URL', 'https://swapi.dev/api')
    
    @pytest.mark.usefixtures("session")
    class TestWithSession:
        @pytest.mark.parametrize("planet_id, expected_name", [
            (1, 'Tatooine'),
            (2, 'Alderaan'),
            # Add more planets as needed
        ])
        def test_planet_details(self, planet_id, expected_name):
            """Test fetching details for various planets."""
            response = self.session.get(f"{self.base_url}/planets/{planet_id}/")
            data = response.json()

            assert response.status_code == 200, "Expected status code to be 200"
            assert data['name'] == expected_name, f"Expected planet's name to be {expected_name}"
            assert 'population' in data, "Expected response to include the planet's population"

        def test_invalid_planet(self):
            """Test fetching details for a non-existent planet to check error handling."""
            response = self.session.get(f"{self.base_url}/planets/999/")
            assert response.status_code == 404, "Expected status code to be 404"
