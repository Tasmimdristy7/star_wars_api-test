# tests/test_starships.py
import pytest
import requests
from config import BASE_URL

class TestStarships:
    @pytest.fixture(scope="class")
    def session(self, request):
        request.cls.session = requests.Session()
        request.cls.base_url = BASE_URL

    @pytest.mark.usefixtures("session")
    class TestWithSession:
        @pytest.mark.parametrize("starship_id, expected_name", [
            (2, 'CR90 corvette'),
            (3, 'Star Destroyer'),
            # Add more starships as needed
        ])
        def test_starship_details(self, starship_id, expected_name):
            """Test fetching details for various starships."""
            response = self.session.get(f"{self.base_url}/starships/{starship_id}/")
            assert response.status_code == 200, "Expected status code to be 200"
            data = response.json()
            assert data['name'] == expected_name, f"Expected starship's name to be {expected_name}"
