# Imports
import imaplib 
import email
from datetime import datetime

# Connect to IMAP server
imap = imaplib.IMAP4_SSL("imap.server.com")
imap.login("username@email.com", "password")
imap.select("INBOX")

# Email Parser Class
class EmailParser:

  # Initialize with email message  
  def __init__(self, message):
    self.msg = email.message_from_string(message)

  # Parse sender from email
  def parse_sender(self):
    return self.msg['From'] 
  
  # Parse date from email
  def parse_date(self):
    return self.msg['Date']

  # Parse subject 
  def parse_subject(self):
    return self.msg['Subject']

  # Parse body
  def parse_body(self):
    if self.msg.is_multipart():
      return self.msg.get_payload(0).get_payload()
    else:
      return self.msg.get_payload()
      
# Rules Engine Classes
class SenderRule:

  # Initialize rule with sender  
  def __init__(self, sender):
    self.sender = sender

  # Check if sender matches    
  def apply(self, email):
    if self.sender in email.parse_sender():
      return 'Important from ' + self.sender
    return None

class KeywordRule:

  # Initialize rule with keyword
  def __init__(self, keyword):
    self.keyword = keyword

  # Check if keyword in body
  def apply(self, email):
    if self.keyword in email.parse_body():
      return 'Important keyword ' + self.keyword
    return None
    
# Create rule instances  
rules = [
  SenderRule("important@company.com"),
  KeywordRule("urgent"),
  KeywordRule("critical"),
]

# Classify emails
def classify_email(email):
  for rule in rules:
    label = rule.apply(email)
    if label:
      return label
  return 'Not important'

# Get unseen emails and classify  
status, data = imap.search(None, 'UNSEEN')

for num in data[0].split():
  _, msg = imap.fetch(num, '(RFC822)')
  email = EmailParser(msg[0][1])

  label = classify_email(email)

  print('Message %s labeled as: %s' % (num, label))

  # Mark email as read
  imap.store(num, '+FLAGS', '\\Seen')
