import smtplib as sm
 
sender_email = "codejammer874@gmail.com"
rec_email = 'ygaurav874@gmail.com'

server = sm.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()

server.login(sender_email, 'messi@10')
server.sendmail(sender_email, rec_email, 'Subject: Hello \n\n Testing Time')

server.quit()


 
print("Email has been to the ", rec_email)