import requests

# GitHub Settings
repo_owner = ''  # Your GitHub username
repo_name = ''  # The repository where issues will be created
token = ''   # GitHub personal access token
api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues'

# Sprint tasks
sprints = {
    "Sprint 1: Project Setup & Authentication": [
        "Initialize the project (Node.js, Express, MySQL, Bootstrap, Vanilla JS).",
        "Set up a Git repository for version control.",
        "Design database schema (users, calculations, reports).",
        "Implement user registration & login with password hashing.",
        "Set up session management (stay logged in).",
        "Create a basic UI with a login & registration form.",
        "Build the backend API for authentication.",
        "Test login/logout functionality."
    ],
    "Sprint 2: Core Functionality - Calculations & Storage": [
        "Create the input form for reinforcement details.",
        "Implement validation for user input (e.g., bar size, spacing).",
        "Develop backend logic for reinforcement calculations.",
        "Store user calculations in the database.",
        "Create API routes for CRUD operations (Create, Read, Update, Delete).",
        "Build the frontend for displaying saved calculations.",
        "Allow users to edit and delete calculations."
    ],
    "Sprint 3: Visualization & UI Improvements": [
        "Generate a simple visual representation of reinforcement.",
        "Improve UI styling with Bootstrap.",
        "Implement a user dashboard for managing calculations.",
        "Add loading animations for calculations.",
        "Ensure mobile responsiveness.",
        "Set up navigation (dashboard, login, contact).",
        "Allow users to view their calculation history."
    ],
    "Sprint 4: Admin Panel & Issue Reporting": [
        "Create secure admin login.",
        "Build an admin dashboard.",
        "Allow admin to view & manage users.",
        "Implement a 'Contact Us' form.",
        "Add issue reporting (users can submit bug reports).",
        "Store issue reports in the database.",
        "Notify admin via email when an issue is reported.",
        "Admin can mark issues as resolved."
    ],
    "Sprint 5: Security, Performance, & Testing": [
        "Prevent SQL injection (use prepared statements).",
        "Implement rate limiting for security.",
        "Secure API routes with authentication middleware.",
        "Enable HTTPS for secure communication.",
        "Optimize database queries for faster performance.",
        "Write unit tests for backend calculations.",
        "Test UI on different browsers and devices.",
        "Fix any major bugs found during testing."
    ],
    "Sprint 6: Deployment & Final Refinements": [
        "Deploy the application (e.g., DigitalOcean, AWS).",
        "Set up a database backup system.",
        "Implement logging for debugging.",
        "Fix UI/UX issues based on feedback.",
        "Add a dark mode toggle (if time allows).",
        "Allow users to export calculations as a PDF.",
        "Conduct final tests & ensure everything works smoothly.",
        "Prepare documentation (setup guide, API endpoints, etc.)."
    ]
}

# Create an issue for each task in each sprint
def create_issue(task_title):
    data = {
        "title": task_title,
        "body": f"Task: {task_title} - Please work on this task.",
        "labels": ["task"]
    }
    headers = {
        'Authorization': f'token {token}'
    }
    response = requests.post(api_url, json=data, headers=headers)
    
    if response.status_code == 201:
        print(f"Successfully created issue: {task_title}")
    else:
        print(f"Failed to create issue: {task_title} - {response.status_code}")

# Loop through sprints and create issues
for sprint, tasks in sprints.items():
    for task in tasks:
        create_issue(task)
