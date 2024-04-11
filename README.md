Star Wars API Testing Project
This project contains automated tests for the Star Wars API (SWAPI), focusing on validating the responses from various endpoints such as planets, characters, and starships. It utilizes Python and pytest to ensure that the API delivers accurate data structures and behaves as expected.

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
What you need to install the software:

Python 3.8 or higher
pip (Python package manager)
Installation
Clone the Repository

bash
Copy code
git clone https://your-repository-url.git
cd star_wars_api
Setup a Virtual Environment (Recommended)

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies

Copy code
pip install -r requirements.txt
Running the Tests
To run the automated tests for this system, execute:

Copy code
pytest
Ensure you're in the project's root directory before running the tests. This command will execute all tests located in the tests/ directory.

