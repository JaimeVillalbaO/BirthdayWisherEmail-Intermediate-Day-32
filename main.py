import random
import datetime 
import smtplib
import pandas as pd

now = datetime.datetime.now()
now_day = now.day
now_month = now.month

file = pd.read_csv('birthdays.csv')
file_dict = file.to_dict(orient='records')
for i in file_dict:
    if int(i['day']) == now_day and int(i['month']) == now_month:
        number_letter = random.randint(1,3)
        with open(f'./letter_templates/letter_{number_letter}.txt') as letter_file:
            letter = letter_file.read()
            new_letter = letter.replace('[NAME]', i['name'])
        my_email = 'jaimevillalbaoyola@gmail.com'
        password = 'sjgwizpxcgmesaps'
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls() #make the conection secure
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, 
                                to_addrs='cryptobluewolf@gmail.com', 
                                msg=f"Subject:Happy birthday\n\n{new_letter}"
                                )
    

