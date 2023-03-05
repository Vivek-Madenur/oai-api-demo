# Sample web app that uses OpenAI api

This app is a simple web application that allows users to ask a question and receive a response powered by OpenAI's API.

## Installation

To install the app, follow these steps:

- Clone the repository
- Install the required dependencies: pip install -r requirements.txt


## Usage

To use this app, you need to have an API key for OpenAI. Follow these steps to add your API key as an environment variable:

Set OPENAI_API_KEY environment variable
- Log in to your OpenAI account and navigate to the API keys - page.
- Create a new API key if you haven't already.
- Copy the API key to your clipboard.
- Open a terminal or command prompt window and enter the - following command: export OPENAI_API_KEY=your-api-key
    - Replace your-api-key with the API key you copied earlier.
- Press Enter to set the environment variable.

Now you can start the app by running the following command:

`python app.py`

or 

`flask run`

Then, navigate to http://localhost:5000 in your web browser to access the application.


## Folder Structure

- `app.py`: This is the main Python file that runs the Flask application.
- `templates/`: This folder contains the HTML templates used to generate the web pages.
