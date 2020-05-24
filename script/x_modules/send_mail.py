import smtplib
from email.mime.multipart import MIMEMultipart
from data.script.x_modules import send_mail_config as config

class sendmail():

    config = config.send_main_config

    def mailInit(self,userName,scriptName):
        message = MIMEMultipart()
        message["From"] = self.config.LOGIN
        message["To"] = self.config.LOGIN
        message["Subject"] = "SCA:  {}, SCRIPT:  {}, REASON:  Task Done!".format(userName,scriptName)

        server = smtplib.SMTP(self.config.SMTPSERVER)
        server.starttls()
        server.login(self.config.LOGIN, self.config.PASSWORD)
        sendmail = server.sendmail(message["From"],message["To"],message.as_string())
        server.quit()