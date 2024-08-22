# Project Template Overview

This repository provides a template to kickstart your project using the following tech stack:

- **Python**: Leverage the most extensive library ecosystem for developing machine learning and deep learning applications.

- **[FastAPI](https://fastapi.tiangolo.com)**: A modern, fast, and lightweight framework for building APIs with Python.

- **[SQLModel](https://sqlmodel.tiangolo.com)**: An ORM that combines the best features of SQLAlchemy and Pydantic, allowing for seamless database management and built-in data validations.

- **[SQLAlchemy Admin](https://github.com/aminalaee/sqladmin)**: Powered by Tablier, this is the simplest and most recommended way to set up an admin panel for your FastAPI-based API.

## Getting Started

To run the project locally, follow these steps:

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the FastAPI development server:
   ```bash
   fastapi dev src/main.py
   ```

<img width="1023" alt="image" src="https://github.com/user-attachments/assets/96fa82e2-6f40-41a5-9e2d-b683c9a98fe2">

## Project Structure

- `src/models`: Define your data models here.
- `src/admin`: Configure SQLAlchemy Admin in this directory.
- `src/utils`: Place global utility functions and helpers here.
