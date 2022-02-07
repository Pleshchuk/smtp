# SMTP client python library
In this repository you can find SMTP client python library which simplify usage of python smtplib library

# Usage
To use SMTP python clien library just copy the file smtp.py into directory with your program and import it from there
Just use the next syntax for that
```
from smtp import *
```

After that you can define your method by using 
```
smtp = Smtp(<server_name>)
```

There are the next setters and getters to use

```smtp.set_sender(<sender_name>)``` - to define sender name

```smtp.set_recipients(<recipients>)``` - to define recipients (it should be commaseparated)

```smtp.set_server(<server_name>)``` - to set server name

```smtp.set_port(<port_number>)``` - to set smtp port number (default is 25)

```smtp.set_subject(<subject>)``` - to set subject name

```smtp.get_sender()``` - to get sender name

```smtp.get_recipients (<recipients>)``` - to get list of recipients

Also, you can see there log method for printing logs to the screen and method for sending email

```smtp.send_email(<severity>, <log_message>)```

```smtp.send_email(<email_body>)```

