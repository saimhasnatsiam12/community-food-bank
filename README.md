# Community Food Bank Management System

A Django-based Community Food Bank Management System designed to register families, manage food inventory, distribute food packs, and maintain distribution records.

## Student Information

- **Student Name:** Siam
- **Project Name:** Community Food Bank Management System
- **Programming Language:** Python
- **Backend Framework:** Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** Configured through environment variables

## Features

- Register new families with unique Family IDs.
- Validate family names and member counts.
- Prevent duplicate family registration.
- Add food packs to available inventory.
- Distribute food packs to registered families.
- Prevent distribution when available stock is insufficient.
- Maintain distribution history.
- Display total families, available food packs, and distributed packs.
- Generate food bank reports.
- Responsive dashboard with a modern glassmorphism UI.

## Project Structure

```text
community-food-bank/
│
├── app/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── configaretion/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── javascript/
│       └── script.js
│
├── tamplates/
│   ├── base.html
│   ├── index.html
│   ├── families.html
│   ├── add_food.html
│   ├── distribute.html
│   └── report.html
│
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.12 or compatible version supported by the selected Django release.
- pip
- Git

All required Python packages are listed in `requirements.txt`.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/saimhasnatsiam12/community-food-bank.git
```

### 2. Navigate to the project directory

```bash
cd community-food-bank
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 5. Install all required packages

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file in the project root directory.

Add the required environment variables according to `configaretion/settings.py`.

For example:

```env
SECRET_KEY=your-secret-key
DEBUG=True
```

Configure your database variables according to the database backend used in the project.

**Important:** Never upload your actual `.env` file or secret credentials to GitHub.

### 7. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Start the development server

```bash
python manage.py runserver
```

Open the application in your browser:

http://127.0.0.1:8000/

## Object-Oriented Programming (OOP)

The project demonstrates the following OOP concepts:

### Family Class
Represents a registered family and stores its Family ID, name, and number of members.

### FoodBank Class
Manages food bank operations, including family registration, adding food packs, and distributing food.

### Constructors and Methods
Constructors initialize object attributes, while methods perform the required operations.

## Python Data Structures

The project demonstrates four fundamental Python data structures:

| Data Structure | Purpose |
|---|---|
| List | Stores distribution history |
| Set | Maintains unique family IDs |
| Tuple | Represents individual distribution records |
| Dictionary | Stores and retrieves families using their IDs |

## Input Validation

- Duplicate Family IDs are rejected.
- Family member counts must be positive.
- Food pack quantities must be positive.
- Unregistered families cannot receive food.
- Insufficient stock does not allow partial distribution.
- Invalid menu choices and nonnumeric input should be handled safely.

## Author

**Siam**

GitHub: https://github.com/saimhasnatsiam12

## License

This project was created for educational and academic purposes.

---

**Community Food Bank Management System**

Built with Python and Django.
