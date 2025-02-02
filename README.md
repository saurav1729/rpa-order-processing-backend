# UiPath Email Automation

## Overview
This project automates email processing using UiPath and Flask. It allows companies to integrate their email accounts with UiPath bots to fetch incoming emails and process them.

## Setup

1. Clone this repository.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables for:
    - `SECRET_KEY`
    - `SQLALCHEMY_DATABASE_URI`
    - `ORCHESTRATOR_API_KEY`
    - `GEMINI_API_KEY`

4. Run the app:
    ```bash
    python app.py
    ```

## API Routes

- `POST /auth/register`: Register a new user.
- `POST /auth/login`: Login a user.
- `POST /connections/create`: Create a new email connection.
- `POST /emails/process`: Process an incoming email.

## Notes
- Ensure UiPath Orchestrator API key and Gmail OAuth token are set correctly.
