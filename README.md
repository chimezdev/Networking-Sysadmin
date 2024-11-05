
# SSH/ROOT ALERT SCRIPT

The "rootalert folder" contains python script that sends sms alert when a user ssh into this machine or becomes a root user

## INSTALLATION

## Setup Environment
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Run
Using rsync, copy this project directory to your target linux server. I have provisioned an Amazon EC2 Linux server for this. Keep the project dir in the /root
  
Use the secrets.env file in the project directory to pass your secrets and reference it in the rootalert.service systemd unit file.
```
VONAGE_API_KEY=YOUR_VONAGE_ACC_API_KEY
VONAGE_SECRET=ACCOUNT_API_SECRET
TARGET_PHONE_NUMBER=RECEIVER_PHONE_NUMBER
SOURCE_NUMBER=SOURCE
```
## Ubuntu server setup
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install virtualenv python3-virtualenv

# copy this repo over, adjust paths in sshalert.service
# copy sshalert.service to /etc/systemd/system/ into whichever target directory you want (probably multi-user)
systemctl daemon-reload
systemctl start sshalert
systemctl enable sshalert
```

