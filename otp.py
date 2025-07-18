from twilio.rest import Client
import random
account_sid = ' '
auth_token = ' '
twilio_number = ' '
ph_no=''
password=1234
attempts=0
max_attempts=5
while True:
    a=int(input("Enter the password:"))
    attempts+=1
    if a==password:
        print("password correct")
        print("Generating OTP")
        i=str(random.randint(100000,999999))
        try:
            x=Client(account_sid,auth_token)
            msg=x.messages.create(
                body=f"OTP is:{i}",
                from_=twilio_number,
                to=ph_no
            )
        except Exception as e:
            print(f"failed to send OTP;{e}")
        try: 
            y=int(input("Enter the OTP:"))
            if y==i:
                print("Logged in")
            else:
                print("Incorrect OTP,Failed to login") 
            break              
        except Exception as e:
            print(f"Error occured:{e}")
            break
    elif attempts==max_attempts:
        print("Too many failed attempts")
        break
    else:
        print(f"Incorrect password,attempts left={max_attempts-attempts}")
        
        
        
        