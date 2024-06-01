# Light-Detection-with-Buzzer
This project was made with the aim of detecting light every 20 seconds and turning on buzzer if there is or there isn't light in the room followed by alert messages to the owner through sms and email. This project would be helpful for agricultural purposes (especially indoor agriculture/greenhouse farming etc) as plants need sunlight to grow and this device can detect whether the plant is getting sufficient sunlight and if not send alerts to the owner. It can also be used for security purposes as it can detect whether there is or there isn't light in the room.

# Software Programming
Step 1: First the Bolt module is to be linked to the Bolt Cloud. For reference click here.

Step 2:

API key and Device ID must be saved from your Bolt Cloud by logging in to your Bolt Cloud, click here to login to your bolt cloud.

SID, Auth Token and the Number given by twilio should be saved from your twilio account, click here to login to your twilio account.

Mailgun API key and Sandbox URL must be saved from your mailgun account, click here to login to your mailgun account.

Step 3: Login into Digital Ocean Ubuntu server using PuTTY by entering the droplet IP address and password from your digital ocean account, click here to access your account.

Step 4: Create a python file in to save our Mailgun and Twilio Credentials called as conf.py, type- sudo nano conf.py to create it. Add the following credentials and save the file by pressing CTRL+X keys followed by “y” key and finally press the Enter key.

 check this link for the full documentation https://projectsubmission.boltiot.com/?p=13874&preview=true
