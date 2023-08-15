import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


SENDER_EMAIL = "testdomsaitov123@yandex.ru"
PASSWORD = "cjiuuitudkuqhzot"
SUBJECT = "Поздравляем. ура"
MESSAGE = "У одного из вашего поста 100 просмотров"


def sent_mail():
    email = "yaroslav66@list.ru"
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['Subject'] = SUBJECT
    msg.attach(MIMEText(MESSAGE, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.yandex.ru', 465) as server:
            server.login(SENDER_EMAIL, PASSWORD)
            msg['To'] = email  # почта на которую отправляем
            server.sendmail(SENDER_EMAIL, email, msg.as_string())  # подключаемся к сервреу

            print(f"Отправили письмо на {email}")  # сообщение об успешной отправки

    except Exception as e:  # обработка ошибки
        print(f"Письмо не отправлено {e}")  # сообщение с ошибкой
