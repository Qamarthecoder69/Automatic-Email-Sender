import openai,smtplib,ssl
from email.message import EmailMessage

#INPUT
user_email_type=input("Enter what kind of email u want to write: ")
user_name=input("Enter ur name :")
boss_name=input("Enter ur Boss name :")
user_email=input("Enter ur email: ")
user_email_passowrd="eygf oejv ogab akxp"
boss_email=input("Enter boss email: ")

openai.api_key="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"

def chat(prompt):
    response=openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role":"user","content":prompt}])
    return response.choices[0].message.content.strip()

def send_email(user_email,boss_email,subject,content):
    em=EmailMessage()
    em['From']=user_email
    em['To']=boss_email
    em['Subject'] = subject
    em.set_content(content)
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as sm:
        sm.login(user_email,user_email_passowrd)
        sm.sendmail(user_email,boss_email,em.as_string())

if __name__ == '__main__':
    content=chat(f"{user_email_type} and insted of YOUR NAME write {user_name} and instead of BOSS NAME write {boss_name}")
    subject=chat(f"Write a subject that fits this email profile, email {content} ")
    send_email(user_email,boss_email,subject,content)




