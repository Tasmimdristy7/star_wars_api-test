import pytest
import requests
from os import getenv
from config import BASE_URL

class TestStarships:
    @pytest.fixture(scope="class")
    def setup_session(self, request):
        """Setup a requests Session and define base URL for all class tests."""
        session = requests.Session()
        request.cls.session = session
        request.cls.base_url = BASE_URL

    @pytest.mark.usefixtures("setup_session")
    class TestWithSession:
        @pytest.mark.parametrize("starship_id, expected_name", [
            (2, 'CR90 corvette'),
            (3, 'Star Destroyer'),
            # Add more starships as needed
        ])
        def test_starship_details(self, starship_id, expected_name):
            """Test fetching details for various starships from the SWAPI."""
            response = self.session.get(f"{self.base_url}/starships/{starship_id}/")
            assert response.status_code == 200, "Expected status code to be 200"
            data = response.json()
            assert data['name'] == expected_name, f"Expected starship's name to be {expected_name}"

            # Example of extending test coverage:
            assert 'model' in data, "Expected 'model' field in the response"
