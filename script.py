from os import environ  # for heroku
import imapclient
# import rconfig  # for local tests

print("Connecting...")
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
print("Connected")

print("Logging in...")

# heroku login
imapObj.login(environ.get('USERNAME_KEY'), environ.get('PASSWORD_KEY'))

# local login
# imapObj.login(rconfig.address, rconfig.password)

print("Logged in")
