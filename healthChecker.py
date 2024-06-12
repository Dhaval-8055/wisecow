import requests
import logging
from datetime import datetime
import time

# Configure logging
logging.basicConfig(filename='application_uptime.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Application URL
APP_URL = 'https://hub.docker.com/'

# Check interval in seconds
CHECK_INTERVAL = 60

def log_status(status):
    """Log the application's status to the console and log file."""
    message = f'Application is {status}'
    print(message)
    logging.info(message)

def check_application_status():
    """Check the application's HTTP status and determine if it is 'up' or 'down'."""
    try:
        response = requests.get(APP_URL)
        if 200 <= response.status_code < 300:
            log_status('up')
        else:
            log_status('down')
    except requests.exceptions.RequestException as e:
        log_status('down')
        logging.error(f'Error checking application status: {e}')

def main():
    """Main function to check application uptime."""
    while True:
        check_application_status()

        # Check every minute
        time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    main()
