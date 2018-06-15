# connect to server
import lib.outlook as outlook
from private_credentials import EMAIL_USER, EMAIL_PASSWORD

mail = outlook.Outlook()
mail.login(EMAIL_USER, EMAIL_PASSWORD)
mail.inbox()
unread = mail.unread()

if unread.is_multipart():
    msg = unread.get_payload(0).get_payload()
else:
    print(unread.get_payload())
subj, fro = unread['subject'], unread['from']

print(fro)
print(subj)
print(msg)
