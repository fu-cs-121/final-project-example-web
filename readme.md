# Journal Application Project

A simple journal application that demonstrates the separation of business logic from user interfaces. This project shows how to structure a Python application with a clean separation of concerns, allowing for multiple interfaces (CLI and web) while maintaining a single core business logic.

## Project Structure

```
project_folder/
    ├── core.py          # Core business logic
    ├── test.py          # Tests for core functionality
    ├── main.py          # Command-line interface
    ├── web.py           # Flask web interface
    ├── templates/       # HTML templates for web interface
    │   └── index.html
    └── README.md        # This file
```

## How the Code Works Together

The project is organized to keep the core functionality separate from the user interfaces. Here's how the different components interact:

- **core.py**: Contains the `Journal` and `JournalEntry` classes, which implement the business logic for managing journal entries. This includes adding entries, retrieving entries, and saving/loading entries to/from a file.

- **main.py**: A command-line interface that allows users to interact with the journal through the terminal. It imports the `Journal` class from `core.py` and uses it to perform actions based on user input.

- **web.py**: A Flask web application that provides a web interface for the journal. It also imports the `Journal` class from `core.py` and uses it to handle web requests.

- **templates/index.html**: The HTML template used by the web interface to display journal entries and provide a form to add new entries.

By separating the business logic from the user interfaces, we ensure that the core functionality is consistent across both the CLI and web interfaces. Any changes to the business logic only need to be made in `core.py`, and both interfaces will automatically use the updated logic.

## Setup

To set up the project, follow these steps:

1. **Create a Virtual Environment**:

   - Open the command palette in VSCode by pressing `Ctrl/Cmd + Shift + P`.
   - Type `Python: Create Environment` and press Enter.
   - Choose the options as prompted. If done successfully, you should see a `.venv` folder in the root directory.

2. **Activate the Virtual Environment**:

   - VSCode automatically activates the selected virtual environment in the integrated terminal.
   - Open a new terminal in VSCode by going to Terminal > New Terminal.
   - The terminal should now display that the virtual environment is activated, showing (.venv) at the beginning of the command line.

3. **Install Dependencies**:

   - Install Flask by running:
     ```bash
     pip install flask
     ```

## Running the Tests

To run the tests for the core functionality, execute the following command in the terminal:

```bash
python test.py
```

## Running the Command-Line Interface

To run the command-line interface, execute:

```bash
python main.py
```

## Running the Web Interface

To run the web interface:

1. Start the Flask application by running:

   ```bash
   python web.py
   ```

2. Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## License

This project is open source and available for educational purposes.
