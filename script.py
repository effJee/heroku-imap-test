import imapclient

print("Connecting...")
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
print("Connected")
