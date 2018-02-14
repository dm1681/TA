# the purpose of this script is to send emails on the behalf of
# Thoroughbred Analytics on a weekly basis.

# GMAIL HAS EXTRA SECURITY YOU HAVE TO TURN OFF AND ON
# TO USE THIS SCRIPT, ALLOW LESS SECURE APPS TO ACCESS ACCOUNT
# AS WELL AS THE DISPLAY UNLOCK CAPTCHA.

# ToDo:
# create a new email template

# the problem with the mailchimp template is that there are redirects
# and other imbeded links that we still want to use,
# but that route to their site or use their assets.

# what do we do after timeout? timeout for subject-request --> default subject-request
# timeout for confirmation? send out default or do not send at all????

import numpy as np
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config
import pdb
### PROCEDURE ###

# an id specific to this email
email_id = "%06i"%(np.random.randint(0,999999))
print("Email ID: %s"%email_id)
# here is the body
html_string = config.html
html = MIMEText(html_string, 'html')

# now lets get subject and title from decider (Kevin)
bFound, subject, request_email_uid = config.get_subject(email_id)

msg = MIMEMultipart('alternative')
msg['From'] = config.username
msg['Subject'] = subject
msg.attach(html)

# lets confirm with kevin that it works
confirmation, subject = config.confirmation(email_id, bFound, subject, request_email_uid, msg)
msg['Subject'] = subject
#pdb.set_trace()

if confirmation == False:
    print('Confirmation == False\nAborting...')
    sys.exit()

for email in config.recipients:
    print('Sending Finalized Email to: %s'%(email), end='\r')
    msg['Bcc'] = email
    config.send_email(email, msg.as_string())
