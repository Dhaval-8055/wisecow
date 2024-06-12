import psutil
import logging
from datetime import datetime
import time  # Import the time module

logging.basicConfig(filename='system_health.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

CPU_THRESHOLD = 80 
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
PROCESS_COUNT_THRESHOLD = 150 

def log_alert(message):
    """Log the alert message to the console and log file."""
    print(message)
    logging.info(message)

def check_cpu_usage():
    """Check CPU usage and log an alert if it exceeds the threshold."""
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_alert(f'High CPU usage detected: {cpu_usage}%')

def check_memory_usage():
    """Check memory usage and log an alert if it exceeds the threshold."""
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        log_alert(f'High memory usage detected: {memory_usage}%')

def check_disk_space():
    """Check disk space usage and log an alert if it exceeds the threshold."""
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        log_alert(f'Low disk space available: {100 - disk_usage}% available, {disk_usage}% used')

def check_running_processes():
    """Check the number of running processes and log an alert if it exceeds the threshold."""
    process_count = len(psutil.pids())
    if process_count > PROCESS_COUNT_THRESHOLD:
        log_alert(f'High number of running processes detected: {process_count}')

def main():
    """Main function to check system health."""
    while True:
        check_cpu_usage()
        check_memory_usage()
        check_disk_space()
        check_running_processes()

        time.sleep(60)

if __name__ == '__main__':
    main()
