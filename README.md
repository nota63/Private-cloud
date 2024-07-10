
# Private Cloud Project

Private Cloud is a robust Django-based web application designed to manage various cloud functionalities including contacts, emails, addresses, images, feedback, passwords, tasks, and Python code snippets.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

### Contacts Management

- **Add and View Contacts:**
  - Capture and store contact information including name, relation, and contact number.
  - Notify users upon successful contact addition.

- **Delete Contacts:**
  - Remove unwanted contacts from the database.
  - Confirmation messages for successful deletions.

- **Export Contacts:**
  - Download all contacts as a CSV file for external use.

### Email Cloud

- **Store Private Emails:**
  - Securely store personal email addresses for future reference.
  - Notifications for successful email storage.

- **View Emails:**
  - Browse through saved email entries.
  - Search functionality to find specific emails.

- **Delete Emails:**
  - Remove emails from the database.
  - Confirmation messages for successful deletions.

- **Export Emails:**
  - Download all email entries in CSV format.

### Address Management

- **Add and View Addresses:**
  - Record and display physical addresses including city, pin code, colony, house number, district, state, and country.

- **Delete Addresses:**
  - Delete unwanted addresses.
  - Confirmation messages for successful deletions.

- **Export Addresses:**
  - Export all addresses as a CSV file.

### Image Cloud

- **Upload Images:**
  - Upload and store images securely.
  - Title and description fields for better organization.

- **View Images:**
  - Browse uploaded images.
  - Search images by title.

- **Delete Images:**
  - Remove images from the database.

### Feedback System

- **Collect User Feedback:**
  - Gather feedback from users including name, email, comments, rating, and recommendations.
  - Notification upon receiving feedback.

### Password Manager

- **Store and Manage Passwords:**
  - Store passwords securely with associated platforms and usernames/emails.
  - Encryption and secure storage mechanism.

- **View Passwords:**
  - Browse stored passwords.
  - Search passwords by platform.

- **Delete Passwords:**
  - Delete stored passwords.
  - Confirmation messages for successful deletions.

- **Export Passwords:**
  - Export all passwords to a CSV file.

### Task Management

- **Manage Tasks:**
  - Organize tasks with dates, times, descriptions, and priority levels.
  - Notification reminders for upcoming tasks.

- **View Tasks:**
  - View tasks categorized by date and priority.
  - Search tasks by title or description.

- **Delete Tasks:**
  - Remove tasks from the system.
  - Confirmation messages for successful deletions.

- **Export Tasks:**
  - Download all tasks in CSV format.

### Python Code Scripts

- **Store and Share Code Snippets:**
  - Add code snippets with titles, descriptions, Python versions, required libraries, and actual code.
  - Repository for storing and sharing reusable code.

- **View Code Snippets:**
  - Browse through available code snippets.
  - Search snippets by title or description.

- **Delete Code Snippets:**
  - Remove code snippets from the repository.
  - Confirmation messages for successful deletions.

## Installation

Follow these steps to set up and run Private Cloud locally:

1. **Clone the repository:**
git clone <repository_url>
cd private-cloud

markdown
Copy code

2. **Install dependencies:**
pip install -r requirements.txt

markdown
Copy code

3. **Database setup:**
- Configure your database settings in `settings.py`.
- Apply migrations:
  ```
  python manage.py migrate
  ```

4. **Create a superuser:**
python manage.py createsuperuser

markdown
Copy code

5. **Run the development server:**
python manage.py runserver

markdown
Copy code

6. **Access the application:**
- Open your web browser and navigate to `http://localhost:8000`.

## Usage

1. **Login** using your admin credentials.
2. Navigate through different sections (Contacts, Email, Address, etc.) to manage respective functionalities.
3. Upload images, manage feedback, passwords, tasks, and view Python code snippets.
4. Utilize search and export functionalities for efficient data management.

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request with your enhancements.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
