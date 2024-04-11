# tests/test_characters.py
import pytest
import requests
from config import BASE_URL

class TestCharacters:
    @pytest.fixture(scope="class")
    def session(self, request):
        request.cls.session = requests.Session()
        request.cls.base_url = BASE_URL

    @pytest.mark.usefixtures("session")
    class TestWithSession:
        @pytest.mark.parametrize("character_id, expected_name", [
            (1, 'Luke Skywalker'),
            (2, 'C-3PO'),
            # Add more characters as needed
        ])
        def test_character_details(self, character_id, expected_name):
            """Test fetching details for various characters."""
            response = self.session.get(f"{self.base_url}/people/{character_id}/")
            assert response.status_code == 200, "Expected status code to be 200"
            data = response.json()
            assert data['name'] == expected_name, f"Expected character's name to be {expected_name}"
