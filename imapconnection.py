import imaplib

imap = imaplib.IMAP4_SSL("imap.server.com")
imap.login("user@email.com", "password")

imap.select("INBOX")

# Search for emails from specific sender
status, data = imap.search(None, 'FROM "sender@email.com"') 

for num in data[0].split():
    # Fetch email by ID
    status, data = imap.fetch(num, '(RFC822)')
    
    # Parse email content
    email = parse_email(data[0][1]) 
    
    # Apply rules
    label = apply_rules(email)
    
    # Update email flags on server
    imap.store(num, '+FLAGS', '\\Important')
