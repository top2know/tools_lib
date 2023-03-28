import smtplib
from email.mime.text import MIMEText

import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
# https://yandex.ru/support/mail/mail-clients/others.html
# Пароль - пароль приложения (для Яндекса)

# Возможно попадание в спам на этапе отправки и бан аккаунта на 24 часа
# Поэтому рекомендуется использование тестовых аккаунтов
# Хотя кто не рискует, тот не пьет шампанское =)

# Почта должна хоститься на Яндексе, для gmail инструкция https://support.google.com/mail/answer/7126229?hl=ru


def send_email(email_to, subject, text):
    msg = MIMEText(text)
    email = EMAIL
    password = PASSWORD

    server = smtplib.SMTP('smtp.yandex.ru', 587)
    server.ehlo()
    server.starttls()
    server.login(email, password)
    server.set_debuglevel(1)  # Необязательно; так будут отображаться данные с сервера в консоли

    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = email_to

    server.sendmail(email, [email_to], msg.as_string())
    server.quit()
