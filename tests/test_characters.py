import pytest
import requests
from os import getenv
from config import BASE_URL

class TestCharacters:
    @pytest.fixture(scope="class")
    def setup_session(self, request):
        """Fixture to initialize a requests Session for use in all tests in this class."""
        session = requests.Session()
        request.cls.session = session
        request.cls.base_url = getenv('SWAPI_BASE_URL', BASE_URL)

    @pytest.mark.usefixtures("setup_session")
    class TestWithSession:
        @pytest.mark.parametrize("character_id, expected_name", [
            (1, 'Luke Skywalker'),
            (2, 'C-3PO'),
           
        ])
        def test_character_details(self, character_id, expected_name):
            """Test fetching details for various characters."""
            response = self.session.get(f"{self.base_url}/people/{character_id}/")
            assert response.status_code == 200, "Expected status code to be 200"
            data = response.json()
            assert data['name'] == expected_name, f"Expected character's name to be {expected_name}"
