# smart-light-alert
Smart Light Alert is an easy to use digital reminder system to remind a user to turn off their lights. 

The program is designed to run on any raspberry pi with an internet connection and requires an LDR in a voltage divider with a 1k resitor and a digital PIR sensor to be connected to its GPIO (note: the LDR voltage divider must be connected to the pi via a MCP3008 analogue to digital convertor as the pi doesn't have an ADC built in).

The program uses the voltage across the LDR to detect whether a light is on in the room and the PIR to detect if there is a person in the room. If both of these values are false for a significant amount of time then an email is sent to the user to alert them that they left a light on.


# How to use:
Enter your user's email in the receiver_email variable definition
Enter your project's email address and password in the relevant variables 
