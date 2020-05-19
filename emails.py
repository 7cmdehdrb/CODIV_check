import smtplib
from email.mime.text import MIMEText


def sendVerifyEmail(recvEmail, key):

    sendEmail = "3cmdehdrb@gmail.com"
    password = "toaru794312@@"

    smtpName = "smtp.gmail.com"  # smtp 서버 주소
    smtpPort = 587  # smtp 포트 번호

    html = (
        """\
        <h1>HELLO!</h1>
        <br>
        If you want to verify your email and user our service, <br>
        Please Click <a href="http://127.0.0.1:8000/user/verify/%s/">HERE</a> to finish verifing!
        """
        % key
    )

    msg = MIMEText(html, "html")
    # msg = MIMEText(text)  # MIMEText(text , _charset = "utf8")

    msg["Subject"] = "Verify Your Email!"
    msg["From"] = sendEmail
    msg["To"] = recvEmail

    s = smtplib.SMTP(smtpName, smtpPort)  # 메일 서버 연결

    try:

        s.starttls()  # TLS 보안 처리
        s.login(sendEmail, password)  # 로그인
        s.sendmail(sendEmail, recvEmail, msg.as_string())  # 메일 전송, 문자열로 변환해야 합니다.

    finally:

        s.close()  # smtp 서버 연결을 종료합니다.


def sendEmail(recvEmail, title, content):

    sendEmail = "3cmdehdrb@gmail.com"
    password = "toaru794312@@"

    smtpName = "smtp.gmail.com"  # smtp 서버 주소
    smtpPort = 587  # smtp 포트 번호

    text = content
    msg = MIMEText(text)  # MIMEText(text , _charset = "utf8")

    msg["Subject"] = title
    msg["From"] = sendEmail
    msg["To"] = recvEmail

    s = smtplib.SMTP(smtpName, smtpPort)  # 메일 서버 연결

    try:

        s.starttls()  # TLS 보안 처리
        s.login(sendEmail, password)  # 로그인
        s.sendmail(sendEmail, recvEmail, msg.as_string())  # 메일 전송, 문자열로 변환해야 합니다.

    finally:

        s.close()  # smtp 서버 연결을 종료합니다.
