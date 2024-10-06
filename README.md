# Recap YouTube

Welcome to the Recap YouTube project! This project is designed to summarize and present YouTube video information in a concise and user-friendly manner using FastAPI, Jinja2, and HTMX. Below is an overview of the project's structure, complexities, solutions, and challenges.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Components](#components)
  - [Database Handler](#database-handler)
  - [Views](#views)
  - [Models](#models)
  - [Configuration](#configuration)
- [Challenges and Solutions](#challenges-and-solutions)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started, clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/faisal-fida/Recap-YouTube.git
cd Recap-YouTube
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
npm install
```

## Usage

To run the project locally, use the following command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Components

### Database Handler

The `DBHandler` class in `app/db.py` manages the in-memory database operations for summary items. It provides methods for adding, retrieving, and removing summary items. This class uses Python's `dataclasses` and `uuid` modules for easy data handling.

### Views

#### Home View

The `home_view` function in `app/views/home.py` renders the home page using Jinja2 templates. It uses FastAPI's `APIRouter` for route management and `HTMLResponse` for rendering HTML content.

#### Summary View

The `summary` function in `app/views/summary.py` handles the form submission for YouTube video URLs, processes the video ID, and fetches or generates the video summary. It uses SQLAlchemy for database interactions and FastAPI's dependency injection for database sessions.

### Models

The `Summary` model in `app/models/summary.py` defines the schema for the summary table in the database. It includes fields for `id`, `title`, `content`, `summary`, and `image`.

### Configuration

The configuration settings in `app/core/config.py` load environment variables using Starlette's `Config` class. It sets up the Jinja2 templates directory and other project-level settings such as `DATABASE_URL`, `SECRET_KEY`, and `DEBUG`.

## Challenges and Solutions

### Dynamic Data Fetching

**Challenge**: Fetching and updating data dynamically from YouTube and managing it in the database.
**Solution**: Utilized FastAPI's asynchronous capabilities and SQLAlchemy's async ORM for efficient data handling and storage.

### State Management

**Challenge**: Managing complex state with nested objects and arrays for summary items.
**Solution**: Used Python's `dataclasses` and `uuid` modules to simplify data handling and ensure unique identifiers for each summary item.

### Error Handling

**Challenge**: Handling errors gracefully during data fetching and form submissions.
**Solution**: Implemented custom exception handling in FastAPI and used conditional rendering to display appropriate messages during error states.
