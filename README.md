
# Snippet Manager 🧑‍💻

## Overview
**Snippet Manager** is a robust, command-line interface (CLI) application tailored for developers to store, manage, and organize their code snippets across multiple programming languages. Designed with simplicity, functionality, and security in mind, Snippet Manager allows developers to quickly save, retrieve, and manage their code snippets, keeping them productive and organized. The application also supports exporting all snippets to a well-formatted PDF file, making sharing and offline access convenient.

## Key Features
- **User Authentication**
  - Secure registration and login system with password hashing.
  - Password reset feature using a security question.
  
- **Snippet Management**
  - Add, view, update, delete, and search code snippets.
  - Organize snippets by language, tags, and description for easy retrieval.
  
- **PDF Export**
  - Export all snippets into a downloadable PDF file, complete with snippet details, for offline viewing or sharing.

- **Security**
  - Passwords are hashed and stored securely.
  - Security question available for account recovery.

## Screenshots

Below are some screenshots showcasing the core features of the Snippet Manager:

1. **Login Screen**  
   ![Login Screen](https://github.com/AbhishekKumar0313/Snippet-Manager/blob/main/Code%20Snippet%20Organizer/Screenshot%202024-11-14%20215733.png)
   _Login page for user authentication._

2. **Snippet Addition**  
   ![Add Snippet](https://github.com/AbhishekKumar0313/Snippet-Manager/blob/main/Code%20Snippet%20Organizer/Screenshot%202024-11-14%20215842.png)
   ![Add Snippet](https://github.com/AbhishekKumar0313/Snippet-Manager/blob/main/Code%20Snippet%20Organizer/Screenshot%202024-11-14%20215904.png)
   _Add new code snippets with programming language, tags, and description._

4. **Export Snippets to PDF**  
   ![Export to PDF](https://github.com/AbhishekKumar0313/Snippet-Manager/blob/main/Code%20Snippet%20Organizer/Screenshot%202024-11-14%20221315.png)
   ![Export to PDF](https://github.com/AbhishekKumar0313/Snippet-Manager/blob/main/Code%20Snippet%20Organizer/Screenshot%202024-11-14%20221334.png)
   _Generate a PDF containing all saved snippets._
5. **File Structure**
   ![Json str](https://github.com/AbhishekKumar0313/Snippet-Manager/blob/main/Code%20Snippet%20Organizer/Screenshot%202024-11-14%20215932.png)
   ![Json str](https://github.com/AbhishekKumar0313/Snippet-Manager/blob/main/Code%20Snippet%20Organizer/Screenshot%202024-11-14%20215942.png)

6. **Exist**
   ![Exist](https://github.com/AbhishekKumar0313/Snippet-Manager/blob/main/Code%20Snippet%20Organizer/Screenshot%202024-11-14%20221350.png)
## Getting Started

### Prerequisites
- **Python 3.7+**: Make sure Python is installed on your system.
- **Pip**: Python's package installer.

### Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd snippet-manager
   ```

2. **Install Required Packages**
   Install necessary dependencies with:
   ```bash
   pip install fpdf passlib
   ```

3. **Run the Application**
   Launch Snippet Manager with:
   ```bash
   python main.py
   ```

## Usage

### Authentication
- **Register:** Sign up with a unique username and secure password.
- **Login:** Log in with your credentials to access your saved snippets.
- **Password Reset:** If you forget your password, answer a security question to reset it.

### Snippet Operations
- **Add Snippet:** Provide a programming language, tags, a description, and the code content.
- **View Snippets:** List all snippets or search by language, tag, or keyword in the description.
- **Update Snippet:** Modify an existing snippet's details.
- **Delete Snippet:** Remove a snippet permanently.
- **Search Snippets:** Quickly find snippets using keywords, tags, or language.

### Export to PDF
Generate a PDF file containing all saved snippets with a title, language, description, and code content. This feature is useful for backing up, sharing, or viewing snippets offline.

#### Example Workflow

```bash
# Start the app
python main.py

# Register a new account
-> Register
Username: johndoe
Password: ******

# Login
-> Login
Username: johndoe
Password: ******

# Add a new snippet
-> Add Snippet
Language: Python
Tags: web scraping, requests
Description: A simple web scraping snippet to fetch HTML content.
Code:
import requests
response = requests.get('https://example.com')
print(response.text)

# Export snippets to PDF
-> Export to PDF
PDF generated: snippets.pdf
```

## Project Structure
- **`main.py`**: Main application script containing the core logic and functions.
- **`User_details.json`**: JSON file that securely stores user account details, including hashed passwords.
- **`Snippets.json`**: JSON file where user-created snippets are stored.
- **`utils/pdf_generator.py`**: Utility for creating a downloadable PDF file containing all snippets.

## Configuration and Customization
- **Password Hashing Algorithm**: Uses `passlib` with `PBKDF2_SHA256` for secure password hashing. This can be customized in `main.py`.
- **JSON File Paths**: Modify the paths to `User_details.json` and `Snippets.json` if required.
- **PDF Styling**: Update font and formatting in `utils/pdf_generator.py` to personalize PDF output.

## Security
- **Password Hashing**: User passwords are securely hashed with `PBKDF2_SHA256` using `passlib`, ensuring no plaintext passwords are stored.
- **Security Questions**: Users are prompted to set a security question, used for account recovery.
- **Encrypted Storage**: Consider implementing further encryption for `User_details.json` if storing sensitive data.

## Dependencies
- **fpdf**: For generating PDFs to export code snippets.
- **passlib**: Used to hash passwords for secure authentication.

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Contribution Guidelines
We welcome contributions to make Snippet Manager better!

1. **Fork the Repository**: Create a fork to add your enhancements or fix issues.
2. **Create a Branch**: Work on a feature branch (`feature/YourFeatureName`).
3. **Commit Changes**: Ensure commits are clear and concise.
4. **Push the Branch**: Push your changes to your fork.
5. **Submit a Pull Request**: Provide a detailed description of the changes.

### Reporting Issues
To report a bug or request a feature, please open an issue with relevant details and steps to reproduce (if reporting a bug).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note:** Replace the image paths (e.g., `path_to_login_screenshot.png`) with actual paths to the screenshots you've captured for your application.

Let me know if you need further refinements or additional details!
