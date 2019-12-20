import smtplib

s = smtplib.SMTP()

s.connect('email-smtp.us-east-1.amazonaws.com', 587)

s.starttls()

s.login('AKIA2ZAO4EI4LJMGV65J', 'BMyZi5QtQ9abF7ijBDEYigJEBBgtD0U2ZAFgezXAZOzA')

msg = 'From: mohamedjaffar450@gmail.com\nTo: mjaff420@gmail.com\nSubject: Test Mail\n\nThis is a Test Email.'

s.sendmail('mohamedjaffar450@gmail.com', 'mjaff420@gmail.com', msg)