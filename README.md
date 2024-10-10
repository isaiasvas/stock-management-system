# Stock Management System

A web-based stock management system for small businesses, built with Django. This system allows you to manage inventory, cash flow, and accounts payable in a simple and intuitive interface.

## Features

- Manage stock levels
- Track cash flow (incomes and expenses)
- Manage accounts payable/receivable

## Technologies

- Django
- Bootstrap (for responsive design)
- PostgreSQL (or SQLite for development)

## Installation

To get a local copy up and running, follow these simple steps.

### Prerequisites

- Python 3.x installed
- Git installed

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/seu-usuario/stock-management-system.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd stock-management-system
   ```

3. **Create and activate a virtual environment**:
   - On macOS/Linux:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

4. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations** (to set up the database schema):
   ```bash
   python manage.py migrate
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. Open your browser and go to `http://localhost:8000` to see the app running.

## Usage

Once the development server is running, you can access the system through the browser. Here's a summary of the main features you can expect:

- **Stock Management**: Add, update, and delete items from your stock.
- **Cash Flow**: Record incomes and expenses to track your financial situation.
- **Accounts Payable/Receivable**: Keep track of upcoming bills and payments.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
