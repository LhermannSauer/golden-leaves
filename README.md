# Budget Management Application

A Python-based backend web application for managing personal or family budgets. The app allows users to track expenses, manage savings, set budget goals, and view financial insights. Built with a focus on simplicity, performance, and scalability, this app uses a modern tech stack designed for professional deployment.

## Tech Stack

- **Backend**: Python, Flask
- **Database**: PostgreSQL (recommended for professional deployment due to stability, scalability, and performance)
- **ORM**: SQLAlchemy
- **API**: Flask-Smorest (for OpenAPI documentation)
- **Data Validation**: Marshmallow (for data serialization/deserialization and validation)
- **Caching**: Redis (to speed up responses by caching frequently requested data)
- **Authentication**: Flask-JWT-Extended for traditional auth and OAuth integration (Google, Facebook, etc.)
- **Data Migrations**: Alembic (for database versioning and migrations)
- **Testing**: PyTest (for unit and integration tests)
- **Task Queue**: Celery (for background task processing, if needed)
- **Configuration Management**: Python Decouple (for environment-specific settings)
- **Currency Conversion**: Integrate with third-party API (like Fixer.io or ExchangeRate-API) for currency conversion
- **Docker**: Docker and Docker Compose (for containerization and easy setup)
- **Development Tools**: Flask-DebugToolbar (for debugging in development), Pre-commit (for code quality checks)

## Features

- **User Authentication**: Secure registration, login, and OAuth-based authentication.
- **Expense Tracking**: Log and categorize expenses by date, category, and amount.
- **Budget Goals**: Set monthly, quarterly, or yearly budget goals.
- **Savings Management**: Track savings and view progress toward goals.
- **Financial Insights**: Generate visual reports to help understand spending habits.
- **Recurring Expenses**: Manage and track recurring expenses like subscriptions or bills.
- **Notifications**: Email alerts for budget limits or reminders for bills.
- **Currency Conversion**: Automatic conversion of expenses in different currencies.
- **Caching**: Leverage Redis to cache frequently accessed data, improving app performance.
- **Data Export/Import**: Import and export data in CSV or JSON format.
- **API Documentation**: Auto-generated API documentation using OpenAPI.

## Installation

### Prerequisites

- Python 3.8+
- Docker (for containerization)
- PostgreSQL (if not using Docker)
- Redis (if not using Docker)

### Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/LhermannSauer/golden-leaves.git
   cd golden-leaves
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install backend dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:

   Create a `.env` file in the root directory to manage configuration:

   ```
   FLASK_ENV=development
   DATABASE_URL=postgresql://user:password@localhost:5432/budget_db
   REDIS_URL=redis://localhost:6379/0
   SECRET_KEY=your_secret_key
   OAUTH_CLIENT_ID=your_oauth_client_id
   OAUTH_CLIENT_SECRET=your_oauth_client_secret
   CURRENCY_API_KEY=your_currency_api_key
   ```

5. **Run database migrations**:

   ```bash
   flask db upgrade
   ```

6. **Run the application**:

   ```bash
   flask run
   ```

### Docker Setup (Alternative)

If you prefer using Docker for easier setup:

1. **Build and run containers**:

   ```bash
   docker-compose up --build
   ```

2. The application will be accessible at `http://localhost:5000`.

## Usage

- **API Endpoints**: Use the OpenAPI documentation available at `http://localhost:5000/api/docs` for detailed API usage.
- **Environment Management**: Use environment-specific `.env` files for development, testing, and production.
- **Tests**: Run the tests using `pytest`:

  ```bash
  pytest
  ```

## Directory Structure

```
budget-management-app/
│
├── app/                     # Application module
│   ├── api/                 # API-related files (Blueprints, routes)
│   ├── models/              # Database models
│   ├── schemas/             # Marshmallow schemas for data validation
│   ├── services/            # Business logic and helper functions
│   ├── utils/               # Utility functions
│   └── extensions/          # Flask extensions setup (db, cache, auth, OAuth)
│
├── migrations/              # Database migrations
├── tests/                   # Unit and integration tests
├── .env.example             # Example environment configuration file
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile               # Dockerfile for building the app image
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
