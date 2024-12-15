# TodoApp with Virtual Environment (FBV)

A simple Django-based Todo application built with function-based views (FBV). This project demonstrates the basics of Django, including CRUD operations, search functionality, and task completion status.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete tasks
- **Task Status**: Mark tasks as complete or incomplete
- **Search Functionality**: Search for tasks by title
- **Virtual Environment**: Organized with virtual environment support

## Getting Started

### Prerequisites

- **Python 3.x** installed on your machine
- **Git** for cloning the repository
- A **virtual environment** setup

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/shahramsamar/TodoApp_with_virtual_env_FBV.git
    cd TodoApp_with_virtual_env_FBV
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run database migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the app in your browser:**
   Visit [http://localhost:8000](http://localhost:8000) to view the app.

### Usage

- **Homepage**: Displays the list of tasks.
- **Add Task**: Use the "Create New Task" button to add a task.
- **Edit Task**: Click on a task's "Edit" link to update details.
- **Delete Task**: Confirm deletion of a task or choose "Delete All Tasks" to remove all tasks.
- **Search Tasks**: Use the search bar to find tasks by title.

## Project Structure

- `todo/`: Main application directory containing views, models, and templates.
- `templates/todo/`: HTML files for task management pages.
- `static/`: Static assets (CSS, JavaScript).
- `requirements.txt`: List of dependencies for the project.

## Contributing

Contributions are welcome! Feel free to submit a pull request to enhance functionality or fix bugs.
![Alt](https://repobeats.axiom.co/api/embed/eabe6508a91fa38b4ace0060919094363916f544.svg "Repobeats analytics image")
