# UiPath Email Automation

## Overview
This project automates email processing using UiPath and Flask. It allows companies to integrate their email accounts with UiPath bots to fetch incoming emails and process them.

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/saurav1729/rpa-order-processing-backend.git
cd rpa-order-processing-backend
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the project root directory and add the necessary variables:

```env
SECRET_KEY=your_secret_key_here
DATABASE_URL=your_database_url_here
PORT=your_port_here
GEMINI_API_KEY=your_gemini_api_key_here
CLIENT_ID=your_client_id_here
CLIENT_SECRET=your_client_secret_here
REDIRECT_URI=your_redirect_uri_here
AUTH_URL=your_auth_url_here
TOKEN_URL=your_token_url_here
```

### 4. Run the Application
```bash
python app.py
```

## API Routes

### Authentication
- `POST /auth/register` - Register a new company.
- `POST /auth/login` - Login a user.
- `GET /auth/google` - Initiate Google OAuth authentication.
- `GET /auth/google/callback` - Handle Google OAuth callback.

### Company Management
- `POST /company/add_user` - Add a new user under a company.
- `DELETE /company/delete_user/<user_id>` - Delete a user from a company.
- `PUT /company/update_user/<user_id>` - Update user details.
- `GET /company/users` - Fetch all users belonging to a company.

### Email Connections
- `POST /company/addConnection` - Create a new email connection.
- `DELETE /company/Connections/<id>` - Delete an existing email connection.
- `PUT /company/Connections/<id>` - Update an email connection.

### Email Processing
- `POST /emails/process` - Process an incoming email.

## Notes
- Ensure that the UiPath Orchestrator API key and Gmail OAuth token are set correctly.
- The application supports OAuth authentication via Google for secure email access.
- Database connection is established using PostgreSQL hosted on Render.

## License
This project is open-source and can be used under the specified license.

