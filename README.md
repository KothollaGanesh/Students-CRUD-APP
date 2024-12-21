
# Student CRUD Application

This project is a simple **Student CRUD (Create, Read, Update, Delete)** application built using **Django** and **MySQL**. It allows users to manage student data such as personal details, courses, and assignments.

## Overview

This project provides a web-based interface to manage student information. The system supports the following features:

- Add new students.
- View all students.
- Update existing student information.
- Delete student records.

The backend is built with Django, and the data is stored in a MySQL database. The application uses basic CRUD operations to handle the data.

## Features

1. **CRUD Operations**
   - **Create:** Add a new student to the database with their details.
   - **Read:** Display a list of all students in the database.
   - **Update:** Modify the information of an existing student.
   - **Delete:** Remove a student record from the database.

2. **Role Management**
   - Basic CRUD functionality for managing student data.

3. **User Interface**
   - Simple and clean user interface for viewing and updating student information.

4. **Database Integration**
   - The student data is stored and managed in a MySQL database.

## Technologies Used

- **Backend Framework:** Django (4.1.6)
- **Database:** MySQL
- **Programming Language:** Python 3.x
- **Build Tool:** Django Development Server

## Setup Instructions

### 1. Prerequisites

Before you begin, ensure you have the following installed:

- **Python**: Version 3.x or higher
- **Django**: Version 4.1.6 or higher
- **MySQL**: For database management
- **Postman**: For API testing (optional but recommended)

### 2. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/YourUsername/Student-CRUD-Project.git
cd Student-CRUD-Project
```

## 3. Configure the Database

### Create a MySQL Database

First, you need to create a new MySQL database. To do so, run the following SQL command:

```sql
CREATE DATABASE studentdb;
```

## 4. Update Database Configuration

In the `settings.py` file, update the following **database configuration** to connect the application to your MySQL database:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Use MySQL backend
        'NAME': 'studentdb',                   # Name of your database
        'USER': 'your_username',               # Your MySQL username
        'PASSWORD': 'your_password',           # Your MySQL password
    }
}
```
## 5. Install Dependencies

Install the required Python dependencies using **pip**:

```bash
pip install -r requirements.txt
```
## 6. Migrate the Database

Run the migrations to set up the **database tables**:

```bash
python manage.py migrate
```
## 7. Run the Application

To start the **development server**, run:

```bash
python manage.py runserver
```
The application will be accessible at http://127.0.0.1:8000/.

## Data Initialization

Insert initial data into the **students_data** table (optional):

```sql
INSERT INTO students_data (first_name, last_name, course, fee, assignment1, assignment2, assignment3, assignment4, institute, location)
VALUES ('John', 'Doe', 'Computer Science', 1500, 85, 90, 88, 92, 'XYZ University', 'New York');
```
## Endpoints

### Home Page
- **Method**: GET  
- **URL**: `http://127.0.0.1:8000/`  
- **Access**: Public (no authentication required)  
- **Response**: Displays the list of all students.

### Add Student
- **Method**: GET  
- **URL**: `http://127.0.0.1:8000/add_student`  
- **Access**: Public (no authentication required)  
- **Response**: Displays the form to add a new student.

### Update Student
- **Method**: GET  
- **URL**: `http://127.0.0.1:8000/update_student/<id>`  
- **Access**: Public (no authentication required)  
- **Response**: Displays the form to update an existing student's details.

### Delete Student
- **Method**: GET  
- **URL**: `http://127.0.0.1:8000/Delete_Student/<id>`  
- **Access**: Public (no authentication required)  
- **Response**: Deletes the student record with the given ID.




## Project Structure

The project directory structure is as follows:


### Explanation:
- **curdapp/**: The main Django application folder.
- **migrations/**: Contains the database migration files.
- **models.py**: Defines the database models for students.
- **views.py**: Handles the logic for student views.
- **urls.py**: Defines the URL routes for the app.
- **templates/**: Contains the HTML templates for the views.
- **db.sqlite3**: The SQLite database file.
- **manage.py**: The script used to manage the Django application.
- **requirements.txt**: Contains the Python dependencies needed for the project.

# Key Files

- **views.py**: Contains the views for handling CRUD operations.
- **models.py**: Defines the `StudentsData` model for storing student information.
- **urls.py**: Defines the URL routing for the views.
- **templates/**: Contains the HTML templates for the frontend.



# Key Learnings

- Built a **CRUD** application using **Django**.
- Integrated **MySQL** for data storage.
- Used Django’s built-in **forms** and **views** for easy implementation.
- Developed a simple yet effective **user interface** for managing student records.

# Conclusion

This project demonstrates a simple implementation of a **CRUD** application for managing **student data**. By using **Django** and **MySQL**, the application allows users to **add**, **view**, **update**, and **delete** student information efficiently. The system is designed to be easily extendable.



