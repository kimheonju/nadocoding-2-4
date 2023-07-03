import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "test mail" # 제목
msg["From"] = EMAIL_ADDRESS  # 보내는 사람
msg["To"] = "godp4785@gmail.com" # 받는 사람

# 만약 여러 명에게 메일을 보낼 때
# msg["To"] = "godp23@naver.com", "godp23@naver.com"
# to_list = ["godp23@naver.com", "godp23@naver.com"]
# msg = ", ".join(to_list)

# # 참조
# msg["Cc"] = "godp23@naver.com"

# # 비밀참조
# msg["Bcc"] = "godp23@naver.com"


msg.set_content("테스트 본문입니다") #본문

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
    