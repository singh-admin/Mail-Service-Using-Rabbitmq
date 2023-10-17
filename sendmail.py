import json
import smtplib
from email.message import EmailMessage
import os

file_path = os.path.join(os.path.dirname(__file__), 'backendcred.json')
dlog_cred = json.load(open(file_path))

mail_path = os.path.join(os.path.dirname(__file__), 'mailformat.json')
mail_format = json.load(open(mail_path))

smtp_username = dlog_cred.get('SMTP_CRED').get('SMTP_EMAIL_USERNAME')  # SMTP USERNAME
test_from_mail = dlog_cred.get('SMTP_CRED').get('FROM_EMAIL')
smtp_password = dlog_cred.get('SMTP_CRED').get('SMTP_EMAIL_PASSWORD') # SMTP PASSWORD
sf_ehost = dlog_cred.get('SMTP_CRED').get('SMTP_EMAIL_HOST')
sf_eport = dlog_cred.get('SMTP_CRED').get('SMTP_EMAIL_PORT')
msg = EmailMessage()


class SendEmail:
    sf_signature = """<p>{body}</p>
    <hr style='border-width:0;height:1px;color:#404040;background-color:#404040;'>
    <p style="color:#404040"> Thank you, <br> Test </p>"""

    def __init__(self, to, cc=""):
        del msg['From']
        del msg['To']
        del msg['Subject']
        del msg['Cc']
        msg['From'] = test_from_mail
        msg['To'] = to
        msg['Cc'] = cc

    # Request to Change Password
    @staticmethod
    def test_mail(emailid, name):
        print("yaha tak", name)
        subbody = mail_format.get('EMAIL_FORMAT').get('NOTIFY')
        msg['Subject'] = subbody[0]
        print(subbody[1], "subbody[1]")
        msg.set_content(SendEmail.sf_signature.format(body=subbody[1].format(name)),
                        subtype='html')





    @staticmethod
    def send():
        smtp = smtplib.SMTP(host=sf_ehost, port=sf_eport)
        smtp.starttls()
        smtp.login(smtp_username, smtp_password)
        smtp.send_message(msg)
        smtp.quit()
