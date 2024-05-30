# Student Grade Management System

This project demonstrates a simple Student Grade Management System using Python and MySQL. It includes the creation of a MySQL database and table, the insertion of student records, and the assignment of grades based on their scores using MySQL triggers.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Trigger Details](#trigger-details)
- [Code Explanation](#code-explanation)
- [Contribution](#contribution)
- [License](#license)
- [Contact](#contact)

## Introduction

The Student Grade Management System is designed to automatically assign grades to students based on their scores upon insertion into the database. This is achieved through the use of a MySQL trigger, which evaluates the score and sets the appropriate grade before the record is finalized in the database.

This project serves as an educational tool to demonstrate the integration of Python with MySQL, the use of database triggers, and basic CRUD operations.

## Features

- Create and initialize a MySQL database and table.
- Insert student records with automatic grade assignment.
- Use of MySQL triggers to manage business logic within the database.
- Simple Python script for managing database operations.

## Prerequisites

Before running this project, ensure you have the following installed on your system:

- Python 3.x
- MySQL Server
- `mysql-connector-python` module

## Installation

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/your-username/student-grade-management.git
    cd student-grade-management
    ```

2. **Install Python Dependencies:**

    ```sh
    pip install mysql-connector-python
    ```

3. **Set Up MySQL:**

    - Ensure your MySQL server is running.
    - Create a MySQL user and grant necessary permissions if needed.

## Usage

1. **Configure Database Connection:**

   Open the `main.py` file and update the MySQL connection details:

    ```python
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password',
        database='mahasiswa_db'
    )
    ```

2. **Run the Script:**

    ```sh
    python main.py
    ```

    This will execute the script to create the database, table, and trigger, and insert sample records.

3. **Verify Data:**

   After running the script, you can verify the data using MySQL Workbench or any other MySQL client by querying the `mahasiswa` table.

## Database Schema

The database consists of a single table named `mahasiswa` with the following schema:

- `id` (INT): Auto-incremented primary key.
- `NIM` (VARCHAR): Student's identification number.
- `Nama` (VARCHAR): Student's name.
- `Nilai` (FLOAT): Student's score.
- `Grade` (CHAR): Assigned grade based on the score.

## Trigger Details

The grades are assigned according to the following score ranges:
A: 90-100
A-: 85-89.99
B+: 80-84.99
B: 75-79.99
B-: 70-74.99
C+: 65-69.99
C: 60-64.99
C-: 55-59.99
D: 45-54.99
E: 0-44.99

