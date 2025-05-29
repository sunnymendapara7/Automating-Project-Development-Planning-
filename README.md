# Project Development & Planning Automation using Python

## Project Overview
This project automates key aspects of the software development lifecycle using Python programming and AI/ML techniques. The goal is to streamline Jira ticket creation, GitHub repository setup, test case generation, and integration with minimal manual intervention.

## What This Project Does
- **Automatically create Jira tickets** for project requirements extracted from a document.
- **Set up a GitHub repository** with branches corresponding to each Jira ticket.
- **Generate test cases using AI (Groq API)** based on Jira ticket details.
- **Link test cases back to Jira tickets** as comments.
- **Automate the entire pipeline** with a single script.

---

## Step-by-Step Process Explanation

### Step 1: Jira Ticket Creation
- Using `main_task1.py`, the project extracts tasks and subtasks from a requirement document and creates corresponding Jira tickets.
- Tickets are created under a user-specified Jira project on the configured Jira server (e.g., `https://your-domain.atlassian.net`).
- Ticket details (e.g., ticket key, summary) are saved in `ticket_keys.json` for use in subsequent steps.

### Step 2: GitHub Repository Setup
- The `main_task2.py` script creates a GitHub repository (configured via environment variables) under the user's GitHub account.
- It initializes the repository with essential project files and creates feature branches for each Jira ticket (e.g., `feature/<ticket-key>`).
- Files such as `main_task1.py`, `main_task2.py`, `main_task3.py`, `requirements.txt`, and `.gitignore` are uploaded to the `main` branch.

### Step 3: Test Case Generation & Linking
- The `main_task3.py` script reads Jira ticket details from `ticket_keys.json` and generates test cases using the Groq API.
- Test cases are saved in `all_test_cases.txt` and linked back to their respective Jira tickets as comments.
- The Groq API is used for AI-driven test case generation, with retry logic to handle API failures and a fallback mechanism for manual test case creation.

### Step 4: Automation
- The `main.py` script automates the entire pipeline.
- It sequentially runs `main_task1.py` (Jira ticket creation), `main_task2.py` (GitHub repository setup), and `main_task3.py` (test case generation and linking).
- Finally, it ensures all project files are uploaded to the GitHub repository.

---

## 🛠️ Libraries & Technologies Used

| Library               | Purpose                                                  |
|-----------------------|----------------------------------------------------------|
| `jira`                | Interacting with Jira API for ticket creation and updates|
| `PyGithub`            | Managing GitHub repository and branches                  |
| `groq`                | AI-driven test case generation via Groq API              |
| `python-docx`         | Generating test case documentation in Word format        |
| `pandas`              | Data manipulation (if needed for future enhancements)    |
| `python-dotenv`       | Loading environment variables from `.env` file           |
| `subprocess`          | Running task scripts sequentially in automation          |

---

## Project Setup and Running Instructions

### Prerequisites
- Python 3.7 or higher installed
- Jira account with API token (`https://your-domain.atlassian.net`)
- GitHub account with Personal Access Token (PAT) with `repo` scope
- Groq API key for test case generation

### Installation Guide

---

## 1. Clone the Repository

```bash
git clone https://github.com/sunnymendapara7/Automating-Project-Development-Planning-.git
cd Automating-Project-Development-Planning

## 📦 Project Setup Instructions for Development Automation

### 2. Install Required Python Libraries

Ensure Python 3.8+ is installed. Then install dependencies:

```bash
pip install -r requirements-pip.txt
```

The `requirements-pip.txt` file includes all necessary libraries:

```text
PyPDF2==3.0.1
python-docx==1.1.2
jira==3.8.0
spacy==3.7.6
transformers==4.44.2
python-dotenv==1.0.1
PyGithub==2.3.0
groq==0.8.0
httpx==0.27.0
```

If you encounter issues, ensure your virtual environment is activated:

```bash
# Create and activate virtual environment (if not already done)
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

---

### 3. Prepare the Environment File

Create a `.env` file in the root directory and add your credentials:

```env
JIRA_SERVER=https://your-domain.atlassian.net
JIRA_EMAIL=your-email@example.com
JIRA_API_TOKEN=your-jira-api-token
JIRA_PROJECT_KEY=project-key
GITHUB_TOKEN=your-github-pat
GITHUB_USERNAME=username
GITHUB_REPO=Repo-Name
GROQ_API_KEY=your-groq-api-key
```

🔐 **Token Help:**

* **JIRA\_API\_TOKEN:** Generate at [https://id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
* **GITHUB\_TOKEN:** Create a Personal Access Token with `repo` scope at [https://github.com/settings/tokens](https://github.com/settings/tokens)
* **GROQ\_API\_KEY:** Obtain from [https://console.groq.com/keys](https://console.groq.com/keys)

---

### 4. Automate the Full Development Pipeline

This script handles Jira ticket creation, GitHub repository setup, test case generation, and linking:

```bash
python main.py
```

The script will:

* Run `main_task1.py` to create Jira tickets
* Run `main_task2.py` to set up the GitHub repository and branches
* Run `main_task3.py` to generate test cases and link them to Jira
* Upload all files to GitHub:

  * `main.py`, `main_task1.py`, `main_task2.py`, `main_task3.py`
  * `test_cases.docx`, `ticket_keys.json`, `requirement_docs.txt`
  * `requirements-pip.txt`, `.gitignore`

---

### 5. Monitor Results

Track the project progress:

* `ticket_keys.json` → Jira ticket details
* `test_cases.docx` → Generated test cases
* GitHub Repository → [https://github.com/username/projectname](https://github.com/sunnymendapara7/sentiment-analysis-system)
* Jira Project → [https://sunnymendapara09.atlassian.net/projects/SAS](https://sunnymendapara09.atlassian.net/projects/SAS) (check ticket comments for test cases)

#### ✅ Expected Output from `main.py`

```text
Running Task 1: Automating Jira Ticket Creation
Created ticket: SAS-33
...
Created ticket: SAS-39
Tickets saved to ticket_keys.json

Running Task 2: Automating GitHub Repository Creation
Repository already exists: https://github.com/sunnymendapara7/sentiment-analysis-system
...
Repository setup complete

Running Task 3: Automating Test Case Creation
Linked test case to SAS-33
...
Linked test case to SAS-39
Test cases saved to test_cases.docx

Updating GitHub Repository with All Files
Updated main.py in repository
Updated main_task1.py in repository
...
Updated .gitignore in repository

Automation Complete!
```

---

### 🙌 Thank You!

Thank you for checking out this **Project Development & Planning Automation** project!

Feel free to ⭐️ the repository, contribute, or raise issues.

📬 For questions or collaboration, reach out to me at:
**[sunnymendapara09@gmail.com](mailto:sunnymendapara09@gmail.com)**
