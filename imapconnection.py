import imaplib

imap = imaplib.IMAP4_SSL("imap.example.com")
imap.login("username@example.com", "password")

imap.select("INBOX")
