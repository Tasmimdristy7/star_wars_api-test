# Star Wars API Testing Project

This project contains automated tests for the Star Wars API (SWAPI), focusing on validating the responses from various endpoints such as planets, characters, and starships. It utilizes Python and pytest to ensure that the API delivers accurate data structures and behaves as expected.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What you need to install the software:

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the Repository**



## Running the Tests

After cloning the repository, setting up your virtual environment, and installing the dependencies, you're ready to run the automated tests for this project. Follow these steps:

1. **Navigate to the Project Directory**

    Ensure you're in the root directory of the project where the `pytest` tests are located.

    ```bash
    cd path/to/star_wars_api
    ```

2. **Activate the Virtual Environment**

    Before running the tests, make sure your virtual environment is activated. This ensures you're using the correct Python and dependencies versions for the project.

    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
    - On Windows:
      ```cmd
      venv\Scripts\activate
      ```

3. **Run the Tests**

    With your virtual environment activated, use `pytest` to run all tests:

    ```bash
    pytest
    ```

    This command will discover and execute all test files within the project directory that follow the `test_*.py` naming convention.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

## Acknowledgments

- Thanks to the Star Wars API (SWAPI) for providing a fun and accessible API to work with.
- Appreciation for the pytest team for their excellent testing framework.
