import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "bhavyakasibhotla16@gmail.com"
    password = "tmie rfpx xphb pazz"
    receiver = "bhavyakasibhotla16@gmail.com"
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)

message=""
send_email(message)
