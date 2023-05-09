import conf #conf is the python file with credentials
from boltiot import Bolt, Sms, Email
import json, time
mybolt=Bolt(conf.API_KEY, conf.DEVICE_ID)
sms= Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)
mail= Email(conf.MAILGUN_API_KEY, conf.SANDBOX_URL, conf.SENDER_EMAIL, conf.REC)
while True:
 print("Reading sensor value")
 response=mybolt.analogRead('A0') #reading the value from LDR
 data=json.loads(response)
 print("Sensor value is " + str(data['value']))
 try:
   sensor_value=int(data['value'])
   threshold=input("Enter 'B' to sense brightness or 'D' to sense darkness in the room= ") #input from user is taken as B or D
   while True: 
    if threshold=='B': #executes if the user input is B
      if sensor_value>500: #this part executes if the light is turned on
        x=mybolt.digitalWrite('0','HIGH') 
        print(x) #the buzzer is turned on
        print("Sending SMS and Email to owner now")
        response1=sms.send_sms("The light has been turned ON") #the sms is sent
        response2=mail.send_email("ALERT!","The light has been turned ON") #the email is sent
        response2_text=json.loads(response2.text)
        print("Response recieved from mailer is: " + str(response2_text['message']))
        print("Status of SMS is " + str(response1.status))
        time.sleep(20)
      else: #this part executes when the light is turned off
        y=mybolt.digitalWrite('0','LOW')
        print(y) #buzzer is turned off
        time.sleep(20)
    if threshold=='D': #executes if the user input is D
      if sensor_value<500: #this executes if the light is turned off
        x=mybolt.digitalWrite('0','HIGH') 
        print(x) #the buzzer is turned on
        print("Sending SMS and Email to owner now")
        response1=sms.send_sms("The light has been turned OFF") #sms is sent
        response2=mail.send_email("ALERT!","The light has been turned OFF") #email is sent
        response2_text=json.loads(response2.text)
        print("Response recieved from mailer is: " + str(response2_text['message']))
        print("Status of SMS is " + str(response1.status))
        time.sleep(20)
      else: #this executes if the light is turned on
        y=mybolt.digitalWrite('0','LOW')
        print(y) #buzzer is turned off
        time.sleep(20)
    else: #executes if the user input is not B or D and the loop is started again
      print('Invalid input, please try again')
      break
 except Exception as e:
   print("Error",e)