### Author: Alex Gowler ###

# Imports libraries
import gpiozero as gpio
import ssl # Secure Sockets Layer
from smtplib import SMTP_SSL # Simple Message Transfer Protocol SSL version only
from email.mime.text import MIMEText
from time import sleep

# Sets up email protocols
port = 465 # For SSL
password = "*" # The email adresses password, blurred out in coursework evidence for security
# Creates a secure SSL context
context = ssl.create_default_context()
test = "This is an automatic test email sent when booting up your Smart Light Alert system" 
receiver_email = "*" #user email address
sender_email = "*" # email made for project

# A function to send email whenever I call it. Email's message is the variable
# placed in the brackets when the function is called
def alert(message):
    #using with means the connection to the server is automatically closed 
    with SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password) # Logs into gmail server
        server.sendmail(sender_email, receiver_email, message) # Sends the email to the set address


alert(test)



# GPIO 
ldr = gpio.MCP3008(5) # Light Dependant Resistor connected to the MCP3008 Analogue to Digital converter.
pir = gpio.MotionSensor(7)

while True: # Infinite loop
    while pir.value == 0 and ldr.voltage > 2: #value of 2V chosen as threshold as when lights on value is typically 1.2V & lights off 
        print("")
        print("PIR: ",pir.value, "  LDR: ", ldr.voltage)
        for i in range (1,90):
            sleep(1)
            print(i)
        alert("User, you left your lights on. Turn them off to avoid wasting energy")
