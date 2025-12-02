# Secret Santa Distributor

A script for assigning players to each other for the Christmas game Secret Santa, and then distributing those assignments via email. Ensuring that no assignment is shared, and no-one is assigned themselves.

Environment variables `EMAIL_ADDRESS` and `EMAIL_PASSWORD` need to be defined, as the email address, and email password respectively. 

> [!WARNING]
> At the current time the only configured SMTP server is `smtp.gmail.com`, and for that you might likely need to setup an "App Password" with your google account.

To run the script in bash, execute the following command: `python secret_santa_distributor.py example_emails.csv`, where `example_emails.csv` is the csv containing the players information.

CSV should be stored in the following schema:
```csv
chad, chadwick@gmail.com
stacey, stacey440@hotmail.com
bart, bartholemew3@gmail.com
```