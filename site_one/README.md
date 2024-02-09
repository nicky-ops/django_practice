# Polls App

## Introduction
The polls app is a simple Django application that allows the admin to create, and users to vote on polls.

## Installation
To install the polls app, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/polls-app.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Open a terminal command prompt and navigate to the root direcory of the project `/site_one`
3. Run database migrations: `python manage.py migrate`
4. Run the following commands in your terminal: `python manage.py createsuperuser`
5. Enter a username, email(optional) and password when prompted and create the superuser.

## Usage
To use the polls app, follow these steps:

1. Start the development server: `python manage.py runserver`
2. Access the app in your browser as a user at `http://localhost:8000/polls`
3. Vote on existing polls by selecting an option and clicking on the "Vote" button
4. To create new polls:
    1. log in as admin at `http://localhost:8000/admin` and use the credentials created earlier to log in.
    2.  Navigate to "Polls > Questions > Add" and create a new poll.


## API Reference
The polls app provides the following API endpoints:

- `GET /api/polls`: Get a list of all polls
- `GET /api/polls/{poll_id}`: Get details of a specific poll
- `POST /api/polls`: Create a new poll
- `POST /api/polls/{poll_id}/vote`: Vote on a poll

## Contributing
If you would like to contribute to the polls app, please follow these guidelines:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit them: `git commit -m "Add your changes"`
4. Push your changes to your forked repository: `git push origin feature/your-feature`
5. Open a pull request to the main repository

## License
The polls app is licensed under the MIT License. See the [LICENSE](/LICENSE) file for more details.
