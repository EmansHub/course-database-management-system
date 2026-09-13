# Course Database Management System

A command-line course database management system developed as part of a **Database II course**. The project uses Python and SQLite to create and manage a database of courses.

## Technologies

* Python
* SQLite

## Features

* Create a `Courses` database table
* View all courses
* Add new courses
* Delete courses
* Update course information
* View a specific course by course code
* Store course code, title, semester, year, and grade

## Database Structure

The `Courses` table contains:

* **Code** — Course code and primary key
* **Title** — Course title
* **Semester** — Semester in which the course was taken
* **Year** — Year the course was taken
* **Grade** — Course grade

## How to Run

Make sure Python is installed, then run the Python file from the terminal:

```bash
python3 filename.py
```

The program creates `project.db` automatically when it is run for the first time.

Follow the menu displayed in the terminal to view, insert, delete, update, or search for courses.
