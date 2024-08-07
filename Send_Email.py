import smtplib

sender = input("Your email: ")
password = input("Your password: ")
receiver = input("receiver: ")
subject = input("Subject: ")
body = input("Body: ")

print("\nLoading...")

message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")