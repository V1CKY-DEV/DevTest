# DevTest File Upload Project

This Django project is a web-based application that allows users to upload CSV and Excel files, processes these files to generate summary statistics, and emails the summary to specified recipients.

## Features

- **File Upload**: Users can upload CSV or Excel files through a web interface.
- **FilePond Integration**: The project uses FilePond for a sleek file upload experience.
- **Summary Generation**: After uploading, the application processes the file and generates summary statistics using Pandas.
- **Email Notification**: The summary statistics are sent to specified email addresses.
- **Responsive Design**: The interface is styled with Bootstrap for responsive and modern UI.

## Preview

You can view a live preview of the application [here](https://burhanfarooq.pythonanywhere.com/).

## Requirements

- Python 3.x
- Django 3.x or later
- Pandas
- FilePond
- SweetAlert2
- Bootstrap 4.5

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/V1CKY-DEV/devtest-upload.git
    cd devtest-upload
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add the following:
    ```
    recipient1=recipient1@example.com
    recipient2=recipient2@example.com
    ```

5. **Run migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Start the development server**:
    ```bash
    python manage.py runserver
    ```

## Usage

1. **Upload a File**:
    - Navigate to `http://127.0.0.1:8000/` in your browser.
    - Use the file input to select and upload a CSV or Excel file.

2. **View Summary**:
    - After uploading, a summary of the file's content will be displayed on the page.
    - The summary is also emailed to the specified recipients.

3. **Handle Errors**:
    - If there is an error during file upload or processing, an error message will be displayed using SweetAlert2.

## Project Structure

- `devapp/views.py`: Contains the logic for handling file uploads, generating summaries, and sending emails.
- `devapp/templates/devapp/home.html`: The main template extending from `base.html` where the file upload form is rendered.
- `static/css/style.css`: Custom styles for the project.
- `uploads/`: Directory where uploaded files are temporarily stored.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any inquiries or issues, please contact Burhan Farooq Dar at `vickymasoodi12@gmail.com`.
