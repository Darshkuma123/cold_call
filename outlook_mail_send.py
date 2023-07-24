import smtplib
import csv

def send_email():
    smtpobj= smtplib.SMTP('smtp-mail.outlook.com',587)
    frommail=""
    password=""
    smtpobj.starttls()
    cold_call_info= open("~/cold_call_info.csv")
    cold_call_details= csv.reader(cold_call_info)
    check_connection=smtpobj.login(frommail,password)
    if(str(check_connection).split(',')[-1].__contains__("Authentication successful")):
        for call in cold_call_details:
            if cold_call_details.line_num==1:
                continue
            message = """Subject:"""+call[3]+"""

            my name"""+call[1]+""" from company"""+call[2]+"""
            This is a test e-mail message.
            """
            smtpobj.sendmail(frommail,call[0],message)
    smtpobj.quit()
if(__name__=="__main__"):
    send_email()