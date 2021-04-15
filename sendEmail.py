import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(passFileName):
    subject = "Alert! Somebody's at Door. D1-SF Mayfield Garden"
    body = "Hi, Please refer to the attached Photograph for your reference."
    sender_email = "rohtak.motors@gmail.com"
    #receiver_email = "mohit3wadhwa@gmail.com, sharukh.wadhwa@gmail.com,  madanwadhwa553@gmail.com"
    receiver_email = "mohit3wadhwa@gmail.com"
    #receiver_email2 = "madanwadhwa553@gmail.com"
    #receiver_email3 = "sharukh.wadhwa@gmail.com"
    #password = input("Type your password and press enter:")
    password = 'Infy#123'
    
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails
    
    # Add body to email
    message.attach(MIMEText(body, "plain"))
    filename = passFileName  # In same directory as script
    
    # Open PDF file in binary mode
    with open('/home/pi/Desktop/CCTV/photos/'+filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        
    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)
    
    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        "attachment; filename={}".format(filename),
        )
    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()
    
    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
        
    print("Email sent!..")

#send_email('code.txt')
#send_email('image.jpg')    