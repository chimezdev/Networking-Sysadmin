
import os
import time
import vonage
import logging
import subprocess, select
from datetime import datetime

# access required env vars
try:
    vonage_api_key = os.getenv("VONAGE_API_KEY")
    vonage_secret = os.getenv("VONAGE_SECRET")
    target_phone_number = os.getenv("TARGET_PHONE_NUMBER")

    # check if all required variables are present
    if not all([vonage_api_key, vonage_secret, target_phone_number]):
        raise ValueError("One or more required variable is missing")
except Exception as err:
    logging.critical(f"Environment variable missing: {err}")
    print(f"Environment variable missing: {err}")
    exit(1)

# initialize vonage client
client = vonage.Client(key=vonage_api_key, secret=vonage_secret)
sms = vonage.Sms(client)

def poll_logfile(filename):
    # Polls the /var/log/auth log for ssh logins or sudo commands.
    with subprocess.Popen(["tail", "-F", "-n", "0", filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
    
        # a poll object to check for new data in the logfile
        poller = select.poll()
        poller.register(process.stdout) # Register the process'stdout' with the poller

        while True:
            # poll for new data with a 1-second timeout
            if poller.poll(1000):
                logline = process.stdout.readline()
                if logline:
                    process_log_entry(logline)
            time.sleep(1)

def process_log_entry(logline):
    
    # check for a local sudo command
    if all(x in logline for x in ["sudo", "COMMAND"]):
        send_sms(logline)
    # check for ssh login
    elif all(x in logline for x in ["ssh", "Accepted"]):
        send_sms(logline)
    return

# send message
def send_sms(log):
    response = sms.send_message(
        {
            "from": "VonageAPI",  # Replace with your sender ID or virtual number
            "to": target_phone_number,
            "text": log,
        }
    )

    if response["messages"][0]["status"] == 0:
        logging.info("Message sent to {} at {}".format(target_phone_number, datetime.now))
        return("Message sent to {} at {}".format(target_phone_number, datetime.now))
    else:
        logging.error("Error: failed to send message: {}".format(response["messages"][0]))
        return("Error: failed to send message: {}".format(response["messages"][0]))

# If our program is being run as main
if __name__ == "__main__":
    # poll the auth.log file
    poll_logfile("/var/log/auth.log")



# Success
{'message-count': '1', 'messages': [{'to': target_phone_number, 'message-id': '0418c4d7-0afb-4544-87e6-*', 'status': '0', 'remaining-balance': '1.70769000', 'message-price': '0.29231000', 'network': '621*'}]}

# Error
{'message-count': '1', 'messages': [{'status': '2', 'error-text': 'Missing api_key'}]}
