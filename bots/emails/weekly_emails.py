# the purpose of this script is to send emails on the behalf of
# Thoroughbred Analytics on a weekly basis.

# GMAIL HAS EXTRA SECURITY YOU HAVE TO TURN OFF AND ON
# TO USE THIS SCRIPT, ALLOW LESS SECURE APPS TO ACCESS ACCOUNT
# AS WELL AS THE DISPLAY UNLOCK CAPTCHA.

import numpy as np
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config

### PROCEDURE ###

# an id specific to this email
email_id = "%06i"%(np.random.randint(0,999999))
print("Email ID: %s"%email_id)
# here is the body
html_string = config.html
html = MIMEText(html_string, 'html')

# now lets get header info
bFound, subject, request_email_uid = config.get_header_info(email_id)

msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = config.username
msg.attach(html)
# lets confirm with kevin that it works
config.confirmation(email_id,bFound, subject, request_email_uid, msg)

for email in config.recipients:
    print('Sending Finalized Email to: %s'%(email), end='\r')
    msg['Bcc'] = email
    config.send_email(email, msg.as_string())
