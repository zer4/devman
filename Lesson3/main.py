import os
import smtplib

sender_email = "zpticin@mail.ru"
recipient_email = "zer4@mail.ru"
website = 'https://dvmn.org/referrals/2qHCiY1vLEF83N2STRVZu2oxwK3ur3jAEiTwTvIb/'
friend_name = 'Василий'
my_name = 'Сашок'

letter = f"""\
From: {sender_email}
To: {recipient_email}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, {friend_name}! {my_name} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {website}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {website}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.\
"""

letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.mail.ru:465')
server.login(os.environ['SMTP_LOGIN'], os.environ['SMTP_PASSWORD'])
server.sendmail(sender_email, recipient_email, letter)
server.quit()