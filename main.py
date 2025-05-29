import os
import logging
from dotenv import load_dotenv
from main_task1 import main as main_task1
from main_task2 import main as main_task2
from main_task3 import main as main_task3

# Setup logging
logging.basicConfig(
    filename='jira_and_llm_tasks.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_REPO = os.getenv('GITHUB_REPO')
JIRA_URL = os.getenv('JIRA_URL')  # e.g., https://your-domain.atlassian.net
JIRA_EMAIL = os.getenv('JIRA_EMAIL')
JIRA_API_TOKEN = os.getenv('JIRA_API_TOKEN')
JIRA_PROJECT_KEY = os.getenv('JIRA_PROJECT_KEY')
DEFAULT_ISSUE_TYPE = os.getenv('DEFAULT_ISSUE_TYPE', 'Task')
DEFAULT_SUBTASK_ISSUE_TYPE = os.getenv('DEFAULT_SUBTASK_ISSUE_TYPE', 'Subtask')

def validate_env_vars():
    """Validate required environment variables."""
    required_vars = {
        'GROQ_API_KEY': GROQ_API_KEY,
        'GITHUB_TOKEN': GITHUB_TOKEN,
        'GITHUB_USERNAME': GITHUB_USERNAME,
        'GITHUB_REPO': GITHUB_REPO,
        'JIRA_URL': JIRA_URL,
        'JIRA_EMAIL': JIRA_EMAIL,
        'JIRA_API_TOKEN': JIRA_API_TOKEN,
        'JIRA_PROJECT_KEY': JIRA_PROJECT_KEY
    }
    missing = [key for key, value in required_vars.items() if not value]
    if missing:
        error_msg = f"Missing environment variables: {', '.join(missing)}"
        logging.error(error_msg)
        print(f"ERROR: {error_msg}")
        return False
    if not JIRA_URL.startswith(('http://', 'https://')):
        error_msg = f"Invalid JIRA_URL: {JIRA_URL}. Must start with http:// or https://"
        logging.error(error_msg)
        print(f"ERROR: {error_msg}")
        return False
    return True

def run_automation():
    """Run all tasks in sequence."""
    logging.info("Starting task automation")
    print("Starting task automation...")

    # Validate environment variables
    if not validate_env_vars():
        logging.error("Environment variable validation failed. Aborting.")
        print("Aborting due to invalid environment variables.")
        return

    # Step 1: Run main_task1 (Jira ticket creation)
    try:
        logging.info("Executing Task 1: Jira ticket creation")
        print("\n=== Task 1: Creating Jira tickets ===")
        main_task1()
        if not os.path.exists('ticket_keys.json'):
            logging.error("Task 1 failed: ticket_keys.json not created")
            print("ERROR: Task 1 failed - ticket_keys.json not created")
            return
        logging.info("Task 1 completed successfully")
        print("Task 1 completed successfully")
    except Exception as e:
        logging.error(f"Task 1 failed: {str(e)}")
        print(f"ERROR: Task 1 failed - {str(e)}")
        return

    # Step 2: Run main_task2 (GitHub repository setup)
    try:
        logging.info("Executing Task 2: GitHub repository setup")
        print("\n=== Task 2: Setting up GitHub repository ===")
        main_task2()
        logging.info("Task 2 completed successfully")
        print("Task 2 completed successfully")
    except Exception as e:
        logging.error(f"Task 2 failed: {str(e)}")
        print(f"ERROR: Task 2 failed - {str(e)}")
        return

    # Step 3: Run main_task3 (Test case generation)
    try:
        logging.info("Executing Task 3: Test case generation")
        print("\n=== Task 3: Generating test cases ===")
        main_task3()
        if not os.path.exists('all_test_cases.txt'):
            logging.error("Task 3 failed: all_test_cases.txt not created")
            print("ERROR: Task 3 failed - all_test_cases.txt not created")
            return
        logging.info("Task 3 completed successfully")
        print("Task 3 completed successfully")
    except Exception as e:
        logging.error(f"Task 3 failed: {str(e)}")
        print(f"ERROR: Task 3 failed - {str(e)}")
        return

    logging.info("All tasks completed successfully")
    print("\nAll tasks completed successfully!")

if __name__ == '__main__':
    run_automation()