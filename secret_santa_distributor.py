import os
import sys
import smtplib
import argparse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv
import random

parser = argparse.ArgumentParser(description='''
    Takes a text file as an argument containing comma seperated key value pairs: Name, Email. 
    The script will then randomly assign recipients to each other, ensuring no-one has the same recipient, nor is assigned to themselves.
    ''')
parser.add_argument('players', help="Path to text file with Name, Email pairs")
    

def send_email(server, distributor_email, recipient_email, assignment):
    # Construct email
    msg = MIMEMultipart()
    msg['From'] = distributor_email
    msg['To'] = recipient_email
    msg['Subject'] = "🎅 Your Secret Santa Assignment 🎄"

    body = f"""
        Hi!

        You are the Secret Santa for: {assignment}

        Merry Christmas! 🎄

        ---
        This is an automated Secret Santa assignment email.
        """
            
    msg.attach(MIMEText(body, 'plain'))
    
    # Send email
    server.send_message(msg)
    print(f"Email sent to {recipient_email}")


if __name__ == '__main__':
    args = parser.parse_args()
    if not args.players:
        parser.print_help()
        sys.exit(1)
    
    with open(args.players, 'r') as f:
        reader = csv.reader(f)
        players = {row[0].strip(): row[1].strip() for row in reader}

    givers = list(players)
    recipients = list(players)

    # Keep shuffling until valid assignment
    while True:
        random.shuffle(recipients)
        if all(givers[i] != recipients[i] for i in range(len(givers))):
            break
    senders = [ players[i] for i in givers ]

    # Configure SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    distributor_email = os.environ.get('EMAIL_ADDRESS')
    sender_password = os.environ.get('EMAIL_PASSWORD')
    if not distributor_email or not sender_password:
        print('Environment variables for EMAIL_ADDRESS and EMAIL_PASSWORD are not defined.')
        sys.exit(1)

    try:
        # Connect to server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(distributor_email, sender_password)

        for i in range(0, len(players)):
            send_email(server, distributor_email, recipient_email=senders[i], assignment=recipients[i])
    except Exception as e:
        print(f"Error sending emails: {e}")