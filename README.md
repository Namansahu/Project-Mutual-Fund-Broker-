# Project-Mutual-Fund-Broker-
This project is a backend-focused application designed for a mutual fund brokerage firm. It provides functionalities for user management, mutual fund data retrieval via RapidAPI, and an optional frontend interface

1. Project Architecture
Backend
Framework: FastAPI is used for its simplicity, speed, and support for modern Python features like type hints.
Database: SQLAlchemy ORM is used to handle database interactions with SQLite as the default database.
API Integration: Integration with the RapidAPI mutual fund endpoint allows fetching open-ended schemes based on fund family.
Security: Passwords are hashed using Passlib’s bcrypt for secure storage.
Testing: FastAPI’s TestClient and pytest ensure the application’s endpoints work correctly.
Frontend (Optional)
Framework: React is used to demonstrate the client-server interaction. Users can register, log in, and fetch mutual fund data through a simple UI.
Purpose: The frontend acts as a lightweight interface for users to interact with the backend API.
2. Features Implementation
User Management
Register: Users can create accounts by providing an email and password.
The password is hashed using bcrypt before being stored in the database.
Duplicate email checks ensure uniqueness.
Login: Users log in using their credentials.
Password verification is performed using bcrypt’s hash comparison.
Mutual Fund Data Integration
RapidAPI Integration:
The external API is accessed using the requests library.
The API key and fund family name are passed as parameters.
Only open-ended schemes are fetched based on the family parameter.
Error Handling:
If the API call fails or no data is found, the backend returns appropriate error messages (e.g., 404 No funds found).
Portfolio Management
Users’ investments can be tracked via the Portfolio table in the database. Although this is currently a placeholder, it can be extended to handle CRUD operations for portfolio tracking.
3. Code Breakdown
Database
Schema:
User table for storing user credentials.
Portfolio table for storing user investments.
Migration: Alembic manages schema changes over time.
Routing
/register: Accepts user email and password, hashes the password, and stores it in the database.
/login: Verifies user credentials against stored data.
/funds: Fetches mutual fund schemes from RapidAPI based on the provided fund family.
API Service Layer
A dedicated service (services/rapidapi_integration.py) is used to interact with the external RapidAPI. This separation ensures modular and testable code.
Environment Variables
.env file stores sensitive data like the database URL and RapidAPI key.
python-dotenv loads these variables securely.
4. Frontend
The React frontend is minimalistic, focusing on user registration and data retrieval.
It interacts with the backend API through HTTP requests (fetch).
Users can:
Register with email and password.
Fetch mutual fund data by providing a fund family name.
5. Deployment
The backend can be deployed on platforms like Heroku, AWS, or Azure.
The frontend can be deployed on Vercel or Netlify.
The API URLs in the frontend need to be updated to the production backend URL during deployment.
6. Testing
FastAPI’s TestClient enables end-to-end (E2E) testing of the backend.
Example tests:
test_register: Ensures user registration works as expected.
test_login: Verifies login functionality.
Mock API responses can simulate the RapidAPI calls for testing purposes.
7. Key Considerations
Scalability: SQLAlchemy can easily switch to more robust databases like PostgreSQL or MySQL for larger-scale deployments.
Security:
Password hashing ensures sensitive information is secure.
Environment variables keep sensitive keys out of the codebase.
Modularity: The separation of services, routes, and models ensures maintainable and testable code.
8. Enhancements
Add JWT-based authentication for secure session handling.
Expand portfolio functionality to allow CRUD operations.
Implement WebSocket for real-time updates of mutual fund values.
Improve error handling with custom exception classes.
